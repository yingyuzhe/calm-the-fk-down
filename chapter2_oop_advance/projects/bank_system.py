#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
银行账户管理系统

这是一个简单的银行账户管理系统，展示了面向对象编程的实际应用。
系统功能：
- 创建不同类型的银行账户（储蓄账户、支票账户）
- 存款和取款操作
- 转账功能
- 利息计算
- 账户历史记录
- 账户状态报告
"""

import datetime
import uuid
from abc import ABC, abstractmethod


class Transaction:
    """交易记录类"""
    
    def __init__(self, transaction_type, amount, description=""):
        self.transaction_id = str(uuid.uuid4())[:8]  # 生成唯一交易ID
        self.timestamp = datetime.datetime.now()
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
    
    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {self.transaction_type} | ¥{self.amount:.2f} | {self.description}"


class Account(ABC):
    """账户抽象基类"""
    
    def __init__(self, account_number, account_holder, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("初始余额不能为负数")
        
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = initial_balance  # 使用下划线表示受保护属性
        self.date_opened = datetime.datetime.now()
        self.transactions = []
        
        # 记录开户交易
        self._add_transaction("开户", initial_balance, "账户创建")
    
    def _add_transaction(self, transaction_type, amount, description=""):
        """添加交易记录"""
        transaction = Transaction(transaction_type, amount, description)
        self.transactions.append(transaction)
        return transaction
    
    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            raise ValueError("存款金额必须为正数")
        
        self._balance += amount
        self._add_transaction("存款", amount)
        return f"存款 ¥{amount:.2f} 成功，当前余额: ¥{self._balance:.2f}"
    
    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            raise ValueError("取款金额必须为正数")
        
        if amount > self._balance:
            raise ValueError("余额不足")
        
        self._balance -= amount
        self._add_transaction("取款", -amount)
        return f"取款 ¥{amount:.2f} 成功，当前余额: ¥{self._balance:.2f}"
    
    def get_balance(self):
        """获取当前余额"""
        return self._balance
    
    def get_transaction_history(self):
        """获取交易历史"""
        history = []
        for transaction in self.transactions:
            history.append(str(transaction))
        return "\n".join(history)
    
    def transfer(self, target_account, amount):
        """转账到另一个账户"""
        if not isinstance(target_account, Account):
            raise TypeError("目标必须是账户对象")
        
        self.withdraw(amount)
        target_account.deposit(amount)
        
        # 更新交易描述
        self.transactions[-1].description = f"转账到账户 {target_account.account_number}"
        target_account.transactions[-1].description = f"来自账户 {self.account_number} 的转账"
        
        return f"成功从账户 {self.account_number} 转账 ¥{amount:.2f} 到账户 {target_account.account_number}"
    
    def get_account_summary(self):
        """获取账户摘要"""
        summary = []
        summary.append(f"账户摘要 - {self.account_number}")
        summary.append(f"账户持有人: {self.account_holder}")
        summary.append(f"账户类型: {self.__class__.__name__}")
        summary.append(f"开户日期: {self.date_opened.strftime('%Y-%m-%d')}")
        summary.append(f"当前余额: ¥{self._balance:.2f}")
        return "\n".join(summary)
    
    @abstractmethod
    def get_account_type(self):
        """获取账户类型，必须由子类实现"""
        pass
    
    def __str__(self):
        return f"{self.get_account_type()} - {self.account_number} - {self.account_holder} - ¥{self._balance:.2f}"


class SavingsAccount(Account):
    """储蓄账户"""
    
    def __init__(self, account_number, account_holder, initial_balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate
        self.interest_accrued = 0
    
    def get_account_type(self):
        return "储蓄账户"
    
    def accrue_interest(self):
        """计算利息"""
        interest = self._balance * self.interest_rate
        self.interest_accrued += interest
        self._balance += interest
        self._add_transaction("利息", interest, f"利率 {self.interest_rate:.1%}")
        return f"已添加利息 ¥{interest:.2f}，当前余额: ¥{self._balance:.2f}"
    
    def get_account_summary(self):
        """重写账户摘要，添加利息信息"""
        summary = super().get_account_summary()
        summary += f"\n利率: {self.interest_rate:.1%}"
        summary += f"\n累计利息: ¥{self.interest_accrued:.2f}"
        return summary


class CheckingAccount(Account):
    """支票账户"""
    
    def __init__(self, account_number, account_holder, initial_balance=0, overdraft_limit=1000):
        super().__init__(account_number, account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit
        self.overdraft_fee = 10  # 透支费用
    
    def get_account_type(self):
        return "支票账户"
    
    def withdraw(self, amount):
        """重写取款方法，支持透支"""
        if amount <= 0:
            raise ValueError("取款金额必须为正数")
        
        # 检查是否超过透支限额
        if amount > self._balance + self.overdraft_limit:
            raise ValueError(f"超出透支限额，最大可取款金额: ¥{self._balance + self.overdraft_limit:.2f}")
        
        # 如果需要透支
        if amount > self._balance:
            overdraft_amount = amount - self._balance
            fee = self.overdraft_fee
            
            self._balance = 0
            self._balance -= overdraft_amount + fee
            
            self._add_transaction("取款", -amount, "透支取款")
            self._add_transaction("费用", -fee, "透支费用")
            
            return f"取款 ¥{amount:.2f} 成功（含透支 ¥{overdraft_amount:.2f} 和费用 ¥{fee:.2f}），当前余额: ¥{self._balance:.2f}"
        
        # 正常取款
        self._balance -= amount
        self._add_transaction("取款", -amount)
        return f"取款 ¥{amount:.2f} 成功，当前余额: ¥{self._balance:.2f}"
    
    def get_account_summary(self):
        """重写账户摘要，添加透支信息"""
        summary = super().get_account_summary()
        summary += f"\n透支限额: ¥{self.overdraft_limit:.2f}"
        summary += f"\n透支费用: ¥{self.overdraft_fee:.2f}"
        
        # 计算可用余额
        available = self._balance if self._balance >= 0 else 0
        summary += f"\n当前可用余额: ¥{available:.2f}"
        
        # 如果有透支，显示透支金额
        if self._balance < 0:
            summary += f"\n当前透支金额: ¥{abs(self._balance):.2f}"
            summary += f"\n剩余可透支额度: ¥{self.overdraft_limit - abs(self._balance):.2f}"
        else:
            summary += f"\n可透支额度: ¥{self.overdraft_limit:.2f}"
            
        return summary


class Bank:
    """银行类，管理账户"""
    
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.next_account_number = 10000
    
    def create_account(self, account_type, account_holder, initial_balance=0, **kwargs):
        """创建新账户"""
        account_number = f"ACC{self.next_account_number}"
        self.next_account_number += 1
        
        if account_type.lower() == "savings":
            interest_rate = kwargs.get("interest_rate", 0.01)
            account = SavingsAccount(account_number, account_holder, initial_balance, interest_rate)
        elif account_type.lower() == "checking":
            overdraft_limit = kwargs.get("overdraft_limit", 1000)
            account = CheckingAccount(account_number, account_holder, initial_balance, overdraft_limit)
        else:
            raise ValueError("不支持的账户类型")
        
        self.accounts[account_number] = account
        return account
    
    def get_account(self, account_number):
        """获取账户"""
        if account_number not in self.accounts:
            raise ValueError(f"账户 {account_number} 不存在")
        return self.accounts[account_number]
    
    def close_account(self, account_number):
        """关闭账户"""
        if account_number not in self.accounts:
            raise ValueError(f"账户 {account_number} 不存在")
        
        account = self.accounts[account_number]
        del self.accounts[account_number]
        return f"账户 {account_number} 已关闭，最终余额: ¥{account.get_balance():.2f}"
    
    def get_all_accounts(self):
        """获取所有账户"""
        return list(self.accounts.values())
    
    def get_total_deposits(self):
        """获取总存款额"""
        total = 0
        for account in self.accounts.values():
            balance = account.get_balance()
            if balance > 0:
                total += balance
        return total
    
    def apply_interest_to_all_savings(self):
        """给所有储蓄账户计息"""
        results = []
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount):
                results.append(account.accrue_interest())
        return results


# 演示程序
def main():
    # 创建银行
    bank = Bank("Python银行")
    
    # 创建账户
    print("创建账户...")
    savings = bank.create_account("savings", "张三", 5000, interest_rate=0.025)
    checking = bank.create_account("checking", "李四", 3000, overdraft_limit=2000)
    
    print("\n账户信息:")
    print(savings)
    print(checking)
    
    # 存款和取款
    print("\n执行交易...")
    print(savings.deposit(1000))
    print(checking.withdraw(500))
    
    # 转账
    print("\n执行转账...")
    print(savings.transfer(checking, 2000))
    
    # 利息计算
    print("\n计算利息...")
    print(savings.accrue_interest())
    
    # 透支取款
    print("\n测试透支...")
    try:
        print(checking.withdraw(5000))
    except ValueError as e:
        print(f"错误: {e}")
    
    # 查看账户摘要
    print("\n储蓄账户摘要:")
    print(savings.get_account_summary())
    
    print("\n支票账户摘要:")
    print(checking.get_account_summary())
    
    # 查看交易历史
    print("\n储蓄账户交易历史:")
    print(savings.get_transaction_history())
    
    # 银行统计
    print("\n银行统计:")
    print(f"总账户数: {len(bank.get_all_accounts())}")
    print(f"总存款额: ¥{bank.get_total_deposits():.2f}")


if __name__ == "__main__":
    main() 