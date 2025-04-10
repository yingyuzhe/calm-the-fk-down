# 第2章：面向对象编程基础

## 2.1 类与实例的概念

### 什么是面向对象编程？

面向对象编程（Object-Oriented Programming，简称OOP）是一种编程范式，它使用"对象"来设计应用程序和软件系统。在面向对象编程中，"对象"是某一类事物的具体个体，而"类"则是这些个体的抽象概括。

举例来说：
- "狗"是一个类（Class）
- 你家的宠物狗"旺财"是一个实例/对象（Instance/Object）

### 类（Class）
- 类是一个抽象的概念，定义了一组属性和方法
- 类是对象的蓝图或模板
- 类定义了对象可能具有的属性（数据）和方法（行为）

### 实例/对象（Instance/Object）
- 实例是类的一个具体例子
- 实例具有类定义的属性和方法
- 不同实例可以有不同的属性值，但共享相同的方法

## 2.2 创建第一个类

在Python中，使用`class`关键字定义类：

```python
# 定义一个简单的Dog类
class Dog:
    # 类变量，所有实例共享
    species = "犬科动物"
    
    # 初始化方法（构造函数）
    def __init__(self, name, age):
        # 实例变量，每个实例独有
        self.name = name
        self.age = age
    
    # 实例方法
    def bark(self):
        return f"{self.name}：汪汪！"
    
    def get_info(self):
        return f"{self.name}是一只{self.age}岁的{self.species}"
```

### 创建实例

一旦定义了类，就可以创建该类的实例：

```python
# 创建Dog类的实例
dog1 = Dog("旺财", 3)
dog2 = Dog("小黑", 2)

# 访问实例的属性
print(dog1.name)  # 输出：旺财
print(dog2.age)   # 输出：2

# 调用实例的方法
print(dog1.bark())      # 输出：旺财：汪汪！
print(dog2.get_info())  # 输出：小黑是一只2岁的犬科动物

# 访问类变量
print(dog1.species)  # 输出：犬科动物
print(dog2.species)  # 输出：犬科动物
print(Dog.species)   # 输出：犬科动物（也可以通过类名访问）
```

## 2.3 实例方法与属性

### 实例方法

实例方法是定义在类内部的函数，它们可以访问和修改实例的状态。实例方法的第一个参数总是`self`，表示实例本身。

```python
class Cat:
    def __init__(self, name):
        self.name = name
        self.mood = "平静"
    
    def meow(self):
        print(f"{self.name}：喵~")
    
    def change_mood(self, new_mood):
        self.mood = new_mood
        print(f"{self.name}现在感到{self.mood}")
```

### 实例属性

实例属性是属于每个实例的变量，不同实例的属性值可以不同。

#### 动态添加实例属性

在Python中，可以在类定义之外动态地为实例添加新属性：

```python
# 创建实例
cat1 = Cat("咪咪")

# 动态添加属性
cat1.color = "橘色"
cat1.weight = 4.5

print(f"{cat1.name}是{cat1.color}的，体重{cat1.weight}公斤")
```

## 2.4 构造函数与析构函数

### 构造函数（`__init__`）

`__init__` 方法是Python类的构造函数，在创建实例时自动调用。用于初始化实例的属性：

```python
class Book:
    def __init__(self, title, author, pages):
        print(f"正在创建《{title}》实例")
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
```

### 析构函数（`__del__`）

`__del__` 方法是Python类的析构函数，在实例被销毁时自动调用。可用于释放资源：

```python
class Book:
    # ... (省略之前的代码)
    
    def __del__(self):
        print(f"《{self.title}》实例被销毁")

# 演示
book = Book("Python学习指南", "张三", 300)
# 当book变量超出作用域或被显式删除时，__del__会被调用
del book  # 输出：《Python学习指南》实例被销毁
```

## 2.5 类变量与实例变量的区别

### 类变量

- 定义在类中，但在方法之外
- 被所有实例共享
- 可以通过类名或实例访问
- 适用于所有实例共享的常量或状态

### 实例变量

- 通常在`__init__`方法中定义
- 每个实例有独立的副本
- 只能通过实例访问
- 适用于实例特有的属性

```python
class Student:
    # 类变量
    school_name = "Python编程学校"
    total_students = 0
    
    def __init__(self, name, grade):
        # 实例变量
        self.name = name
        self.grade = grade
        # 修改类变量
        Student.total_students += 1
```

### 类变量的陷阱

当类变量是可变对象（如列表、字典）时要特别小心：

```python
class Course:
    # 类变量是一个列表
    students = []
    
    def __init__(self, name):
        self.name = name
    
    def add_student(self, student):
        self.students.append(student)  # 注意：这会修改类变量

# 创建课程实例
math = Course("数学")
english = Course("英语")

# 添加学生
math.add_student("张三")
english.add_student("李四")

print(math.students)    # 输出：['张三', '李四']
print(english.students) # 输出：['张三', '李四']
print(Course.students)  # 输出：['张三', '李四']
```

正确的做法是将可变对象定义为实例变量：

```python
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []  # 实例变量
    
    def add_student(self, student):
        self.students.append(student)
```

## 2.6 实践案例：创建一个简单的银行账户类

让我们创建一个`BankAccount`类来应用我们学到的概念：

```python
class BankAccount:
    # 类变量
    interest_rate = 0.05  # 5%的利率
    total_accounts = 0
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = BankAccount.total_accounts + 1000
        BankAccount.total_accounts += 1
        print(f"账户 #{self.account_number} 已创建")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"存款 ¥{amount} 成功，当前余额: ¥{self.balance}"
        return "存款金额必须为正数"
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"取款 ¥{amount} 成功，当前余额: ¥{self.balance}"
        return "余额不足或金额无效"
    
    def add_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        return f"已添加利息 ¥{interest:.2f}，当前余额: ¥{self.balance}"
    
    def get_balance(self):
        return f"{self.account_holder}的当前余额: ¥{self.balance}"
    
    def __str__(self):
        return f"账户 #{self.account_number} 持有人: {self.account_holder}, 余额: ¥{self.balance}"
```

### 使用银行账户类

```python
# 创建账户
account1 = BankAccount("张三", 1000)
account2 = BankAccount("李四", 500)

# 操作账户
print(account1.deposit(500))
print(account2.withdraw(200))
print(account1.add_interest())
print(account2.get_balance())

# 打印账户信息
print(account1)
print(account2)

# 查看总账户数
print(f"总账户数: {BankAccount.total_accounts}")
```

## 2.7 课后练习

1. 创建一个`Rectangle`（矩形）类，具有以下功能：
   - 初始化时设置长度和宽度
   - 计算面积和周长的方法
   - 比较两个矩形大小的方法

2. 创建一个`Product`（产品）类，包含：
   - 产品名称、价格和库存量
   - 更新价格和库存的方法
   - 计算总价值（价格×库存）的方法

3. 扩展`BankAccount`类，添加：
   - 账户类型（如"储蓄"、"支票"）
   - 转账方法（从一个账户转账到另一个账户）
   - 每月服务费扣除方法

## 2.8 小结

在本章中，我们学习了：

- 面向对象编程的基本概念：类和实例
- 如何在Python中定义类和创建实例
- 实例方法和属性的使用
- 构造函数和析构函数
- 类变量与实例变量的区别

类和实例是面向对象编程的基础。在下一章中，我们将深入探讨封装和访问控制，学习如何保护类的内部数据和实现。 