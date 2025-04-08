#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
高级猜数字游戏
这是一个增强版的猜数字游戏，具有难度级别选择和记录保存功能。
"""

# 导入所需的模块
import random
import time
import json
import os
from datetime import datetime

# 记录文件路径
RECORDS_FILE = "game_records.json"

def clear_screen():
    """清除屏幕"""
    os.system('cls' if os.name == 'nt' else 'clear')
    # 在Windows系统（os.name == 'nt'）上使用cls命令
    # 在其他系统（如Linux、macOS）上使用clear命令

def load_records():
    """从文件加载游戏记录"""
    if os.path.exists(RECORDS_FILE):
        try:
            with open(RECORDS_FILE, 'r', encoding='utf-8') as f:
            #with语句打开文件并自动处理文件关闭
                return json.load(f)
            #json.load 会将json格式转化为python 对象
            #return会立即结束函数，将结果返回到函数调用处。可return多个值，不写return或单写一个return默认返回None。
            #continue会跳过当前循环的剩余语句，继续下一次循环。
        except json.JSONDecodeError:
            print("记录文件损坏，创建新的记录。")
            return []
    return []

def save_record(player_name, difficulty, attempts, duration):
    """保存游戏记录"""
    records = load_records()
    record = {
        "player_name": player_name,
        "difficulty": difficulty,
        "attempts": attempts,
        "duration": duration,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #第一个点号：datetime.now() 含义：类方法调用，调用datetime类的now()方法，返回一个datetime对象.
        #第二个点号：.strftime("%Y-%m-%d %H:%M:%S") 含义：实例方法调用，调用返回的datetime对象/实例的strftime()方法
        #点号用法：访问对象属性 oject.attribuate；调用对象方法 object.method()；访问模块内容 module.function()；访问类成员 class.method()
    }
    records.append(record)
    #append()方法会新增一行填入record，此时并没有逗号产生。
    #而python在显示list的时候，会自动添加逗号。逗号是列表语法的一部分，不是数据的一部分，不要专门添加。
    
    with open(RECORDS_FILE, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
        #json.dump()：将Python对象转换为JSON格式并写入文件
        #第二个参数f：文件对象，用于写入数据
        #ensure_ascii=False：允许输入非ASCII字符，确保中文不会被转换为ASCII码。不为True,中文会被转成unicode
        #indent=2：设置缩进为2个空格，使JSON格式更易读  


def show_records():
    """显示游戏记录"""
    records = load_records()
    #将records数据转换为python对象，方便后续处理。
    if not records:
        #Python中，空列表[]在布尔上下文中被视为False。if records == []: 等价
        print("暂无游戏记录。")
        return
    
    print("\n===== 游戏记录 =====")
    print(f"{'玩家':^10}|{'难度':^8}|{'尝试次数':^8}|{'用时(秒)':^8}|{'日期':^20}")
    #f"..."：f-string格式化字符串。 {内容:对齐方式宽度}：格式化语法
    #^：居中对齐
    #数字：指定宽度（字符数）
    print("-" * 60)
    
    # 按尝试次数排序
    sorted_records = sorted(records, key=lambda x: x['attempts'])
    #sorted(iterable, key=None, reverse=False)
    #iterable：可迭代对象，如列表、元组、字符串等；key：必须是一个函数，不能是数组字符串数字等；reverse=false 代表升序，默认降序。

    #lambda创建匿名函数："lambda 参数1，参数2，参数3……: 表达式"。
    #匿名函数特点： 没有函数名，只有表达式子，自动返回表达结果。不能包含循环、return等语句。

    for record in sorted_records[:10]:  # 只显示前10条记录
        print(f"{record['player_name']:^10}|{record['difficulty']:^8}|{record['attempts']:^8}|{record['duration']:^8.2f}|{record['date']:^20}")
    
    input("\n按回车键继续...")

def select_difficulty():
    """选择游戏难度"""
    clear_screen()
    print("===== 选择难度 =====")
    print("1. 简单 (1-50)")
    print("2. 中等 (1-100)")
    print("3. 困难 (1-200)")
    
    while True:
        try:
            choice = int(input("请选择难度(1-3): "))
            if 1 <= choice <= 3:
                if choice == 1:
                    return "简单", 1, 50
                elif choice == 2:
                    return "中等", 1, 100
                else:
                    return "困难", 1, 200
            else:
                print("请输入1-3之间的数字！")
        except ValueError:
            print("请输入有效的数字！")

def get_player_name():
    """获取玩家姓名"""
    while True:
        name = input("请输入您的名字: ").strip()
        #strip()：去除字符串两端的空白字符（包括空格、制表符、换行符等）。
        if name:
            return name
        print("名字不能为空！")

def advanced_guess_number_game():
    """高级猜数字游戏主函数"""
    clear_screen()
    print("=" * 40)
    print("欢迎来到高级猜数字游戏！")
    print("=" * 40)
    
    # 获取玩家姓名
    player_name = get_player_name()
    
    # 选择难度
    difficulty_name, min_num, max_num = select_difficulty()
    
    clear_screen()
    print(f"您好，{player_name}！")
    print(f"您选择了{difficulty_name}难度。")
    print(f"我已经想好了一个{min_num}到{max_num}之间的数字。")
    print("开始猜测吧！")
    print("=" * 40)
    
    # 生成随机数
    print("正在生成随机数...", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")
    
    secret_number = new_func(min_num, max_num)
    
    # 初始化游戏数据
    attempts = 0
    start_time = time.time()
    #第一个time表示time模块，第二个time表示time模块的time()方法

    # 游戏循环
    while True:
        try:
            guess = int(input(f"请猜一个{min_num}-{max_num}之间的数字: "))
            
            if guess < min_num or guess > max_num:
                print(f"请输入{min_num}-{max_num}之间的数字！")
                continue
                
        except ValueError:
            print("请输入一个有效的数字！")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print(f"猜小了！再试一次。")
        elif guess > secret_number:
            print(f"猜大了！再试一次。")
        else:
            end_time = time.time()
            duration = end_time - start_time
            
            print(f"\n恭喜你，{player_name}！你猜对了！")
            print(f"正确答案是: {secret_number}")
            print(f"你总共猜了 {attempts} 次。")
            print(f"用时: {duration:.2f} 秒")
            
            # 保存记录
            save_record(player_name, difficulty_name, attempts, duration)
            
            # 根据猜测次数给出评价
            if attempts <= 3:
                print("太厉害了！你是猜数字大师！")
            elif attempts <= 6:
                print("不错！你有很好的猜测能力！")
            elif attempts <= 10:
                print("还行，继续练习可以做得更好！")
            else:
                print("加油，下次争取更少的次数猜对！")
                
            break
            # 退出当前的for 或 while 循环结构。 注意if else不是一个循环结构
    
    return play_again()

def new_func(min_num, max_num):
    secret_number = random.randint(min_num, max_num)
    return secret_number

def show_menu():
    """显示主菜单"""
    clear_screen()
    print("=" * 40)
    print("猜数字游戏 - 主菜单")
    print("=" * 40)
    print("1. 开始游戏")
    print("2. 查看记录")
    print("3. 退出游戏")
    print("=" * 40)
    
    while True:
        try:
            choice = int(input("请选择(1-3): "))
            if 1 <= choice <= 3:
                return choice
                #return 会立即结束def函数，将结果返回到函数调用处。所以此处不仅结束了while循环，还结束了show_menu函数。
                #如果这里写的print，那会一直进行while循环。
            else:
                print("请输入1-3之间的数字！")
        except ValueError:
            print("请输入有效的数字！")
        # try 可能出错代码块  except 异常处理代码块

def play_again():
    """询问是否再玩一次"""
    choice = input("\n要再玩一次吗？(y/n): ").lower()
    return choice == 'y' or choice == 'yes'
    # 等价于
    # if choice == 'y' or choice == 'yes':
    #     return True
    # else:
    #     return False

def main():
    """程序入口点"""
    while True:
        choice = show_menu()
        
        if choice == 1:
            if not advanced_guess_number_game():
                break
        elif choice == 2:
            show_records()
        else:
            print("谢谢参与！下次再见！")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n游戏已中断。再见！") 