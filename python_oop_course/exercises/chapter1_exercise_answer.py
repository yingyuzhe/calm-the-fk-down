#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 首先关闭了lingma的自动代码补全。 Cloud Model Auto Trigger Generate Length = Disabled
# 编写一个函数 `is_leap_year(year)`，判断给定年份是否是闰年。
# - 规则：
#   - 年份能被4整除但不能被100整除，或者能被400整除的是闰年。

def is_leap_year_v1():
   while True:
      year = input("请输入年份：")
      try:
         year = int(year)
      except ValueError:
         print("请输入有效的数字！")
         continue
      if  (year % 4 == 0 and year % 100 !=0) or year % 400 ==0:
         return True
      else:
         return False
#答案评价：
# 函数的用途有多种，一种是面对输入输出，一种是面对程序调用。前者重交互，需要应对输入输出。后者重逻辑，需要方便调用。 
# 因此可以将答案拆成两部分，一部分负责纯逻辑，外部再封装以支持输入输出交互。
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def interactive_leap_year_checker() -> bool:
    """Prompt user for a year and print leap year status."""
    while True:
        try:
            year = int(input("请输入年份："))
            return is_leap_year(year)
        except ValueError:
            print("请输入有效的数字！")

# 编写一个程序，将百分制成绩（0-100）转换为五级制成绩（A、B、C、D、E）。
# - 规则：
#   - 90分及以上：A
#   - 80-89分：B
#   - 70-79分：C
#   - 60-69分：D
#   - 60分以下：E
      
def grade_gen(score):
   if score >=90:
      grade="A"
   elif score >=80:
      grade="B"
   elif score >=70:
      grade="C"
   elif score >=60:
      grade="D"
   else:
      grade="E"
   return grade
def interactive_grade_gen(score):
   while True:
      try:
         score=int(input("please enter score:"))
         return grade_gen(score)
      except ValueError:
         print("please enter valid number")
#interactive_grade_gen 函数的参数 score 未使用，可以直接移除：def interactive_grade_gen()
#可以增加百分制验证：
def interactive_grade_gen():
    while True:
        try:
            score = int(input("please enter score:"))
            if 0 <= score <= 100:
                return grade_gen(score)
            else:
                print("分数必须在 0 到 100 之间！")
        except ValueError:
            print("please enter valid number")

### **2. 循环结构**
#### 练习 2.1：打印九九乘法表
# 使用嵌套循环打印九九乘法表。
# - 示例输出：
#   ```
#   1x1=1
#   1x2=2  2x2=4
#   1x3=3  2x3=6  3x3=9
def print_99():
      for i in range(1,10):
         for j in range(1,10):
            print(f"{j}x{i}={i*j}",end="\t")
            if j>=i:
               print("\n")
               break
#if判断条件可以省略，内层循环 for j in range(1,10) 可以优化为 for j in range(1, i+1)。
#print换行逻辑不清晰，可以加在外层循环中。
def print_99():
    """打印九九乘法表。"""
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i*j}", end="\t")  # 使用制表符对齐
        print()  # 每行结束后换行

#### 练习 2.2：计算阶乘
# 编写一个函数 `factorial(n)`，计算给定正整数 `n` 的阶乘。
# - 示例：
#   ```python
#   print(factorial(5))  # 120
#   print(factorial(0))  # 1
def factorial(n):
   s=1
   for i in range(1,n+1):
      s=s*i
   return s

def interactive_factorial():
   while True:
      try:
         n=int(input("please enter an integer:"))
         if n<0:
            print("please enter an integer larger than 0") 
         else:
            return factorial(n)
      except ValueError:
         print("please enter a valid number")
# 可以利用递归让函数更加简洁：
def factorial_iteral(n):
    """递归计算给定正整数 n 的阶乘。
    Args:
        n (int): 正整数。
    Returns:
        int: n 的阶乘。
    """
    if n < 0:
        raise ValueError("n 必须为非负整数")
    if n == 0 or n == 1:
        return 1
    return n * factorial_iteral(n - 1)

#### 练习 2.3：寻找最大值
# 编写一个程序，让用户输入一组数字（以空格分隔），并找出其中的最大值。
# - 示例：
#   ```
#   输入：3 5 7 2 8
#   输出：8
#   ```

def find_max(list):
   while True:
      try:
         list=input("please enter a set of number seperated by space:")
         list.list()
         return list.max
      except ValueError:
         print("please enter valid number")
# list 参数名与内置类型名称冲突，改为numbers
# .list()方法在python内不存在。 要用split()方法将字符串转换为list然后转为为数字。
# 使用max()函数查找列表的最大值。
# 异常处理增加对空输入和非数字的处理，.list() valueerror不对。
def find_max():
    """从用户输入的一组数字中查找最大值。"""
    while True:
        try:
            # 获取用户输入
            input_str = input("请输入一组数字，用空格分隔：")
            if not input_str.strip():
                #.strip() 的作用是去除字符串 开头和结尾 的空白字符（包括空格、制表符 \t、换行符 \n 等）。
                #not input_str.strip() 能检测是否输入了有效内容，如果均为空字符，input_str.strip()会返回false
                print("输入不能为空！")
                continue
                # 改成break会直接跳出循环，函数终止。
                # 删除continue 导致输入为空时继续执行,max([])会报错进入ValueError段。
                # 删除continue 虽然最终也能提示用户重新输入，但是会抛两次异常，一次在if判断中抛出，一次在except valueerror中抛出。

            # 将输入字符串转换为数字列表
            numbers = [float(num) for num in input_str.split()]
            
            # 返回最大值
            return max(numbers)
        
        except ValueError:
            print("请输入有效的数字！")

### **3. 函数定义**
#### 练习 3.1：计算BMI指数
# 编写一个函数 `calculate_bmi(weight, height)`，根据体重（kg）和身高（m）计算BMI指数，并返回对应的健康状态。
# - BMI公式：`BMI = weight / (height ** 2)`
# - 健康状态：
#   - BMI < 18.5：偏瘦
#   - 18.5 ≤ BMI < 24：正常
#   - 24 ≤ BMI < 28：超重
#   - BMI ≥ 28：肥胖
def calculate_bmi(weight,hight):
   bmi=weight/(hight^2)
   if bmi< 18.5:
      return print(f"your bmi is {bmi} and your body shape is thin")
   elif bmi<=24:
      return print(f"your bmi is {bmi} and your body shape is normal")
   elif bmi<=28:
      return print(f"your bmi is {bmi} and your body shape is fat")
   else:
      return print(f"your bmi is {bmi} and your body shape is pig-like")
def interactive_bmi_calculate():  
   while True:
      try:
         weight=int(input("please entere you weight:"))
         hight=int(input("please entere you hight:"))
         return calculate_bmi
      except ValueError:
         print("please enter a valid weight or hight")
#interactive_bmi_calculate 函数返回的是 calculate_bmi 函数本身，而不是调用它。需要调用 calculate_bmi 并传入参数。
#当前代码使用 hight^2 计算身高的平方，但 ^ 是位运算符，不是幂运算符。正确的幂运算符是 **。
#calculate_bmi 函数直接使用 print 输出结果，而不是返回结果。这限制了函数的复用性。
#hight 拼写错误，应为 height。
def calculate_bmi(weight, height):
    """根据体重和身高计算BMI指数，并返回健康状态。
    Args:
        weight (float): 体重，单位为千克（kg）。
        height (float): 身高，单位为米（m）。
    Returns:
        str: 健康状态描述。
    """
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"你的BMI是{bmi:.2f}，体型偏瘦。"
      # {variable:.nf} 这里n表示保留几位小数，f表示转化为float
    elif 18.5 <= bmi < 24:
        return f"你的BMI是{bmi:.2f}，体型正常。"
    elif 24 <= bmi < 28:
        return f"你的BMI是{bmi:.2f}，体型超重。"
    else:
        return f"你的BMI是{bmi:.2f}，体型肥胖。"

def interactive_bmi_calculate():
    """交互式获取用户输入并计算BMI指数。"""
    while True:
        try:
            weight = float(input("请输入你的体重（kg）："))
            height = float(input("请输入你的身高（m）："))
            if weight <= 0 or height <= 0:
                print("体重和身高必须为正数！")
                continue
            result = calculate_bmi(weight, height)
            return print(result)
        except ValueError:
            print("请输入有效的数字！")


# #### 练习 3.2：字符串反转
# 编写一个函数 `reverse_string(s)`，接受一个字符串并返回其反转后的结果。
# - 示例：
#   ```python
#   print(reverse_string("hello"))  # "olleh"
#   print(reverse_string("Python"))  # "nohtyP"
def reverse_string(strings):
   stringlist=[]
   for i in strings:
      stringlist=stringlist.append(i)
      #stringlist.append(i) 直接修改 stringlist，不需要赋值。stringlist.append(i)就行了
   reversed_string=""
   i=len(strings)
   while i <=len(strings) and i>=1:
      reversed_string=f"{reversed_string}{stringlist[i-1]}"
      i=i-1
   return reversed_string
def interactive_revstr():
   strings=input("please enter a string:")
   return print(reverse_string(strings))
# stringlist.append(i) 错误：会直接修改 stringlist，并返回 None。
# while i <= len(strings) and i >= 1 中的 i 未初始化，i = len(strings) 应在循环外。
# reverse_string 变量名冲突：reverse_string 既是函数名，又是局部变量名，容易引起混淆。
# 代码冗余：使用列表和循环反转字符串的方式过于复杂，Python 提供了更简洁的实现方式。

def reverse_string(s):
    """反转字符串。
    Args:
        s (str): 输入的字符串。
    Returns:
        str: 反转后的字符串。
    """
    return s[::-1]
   #list[start:stop:step] 表示切片器功能，结果会返回一个list
   # start：切片的起始位置（默认为 0）。
   # stop：切片的结束位置（默认为序列的长度）。
   # step：切片的步长（默认为 1）。-1表示从尾部倒着遍历。

def interactive_revstr():
    """交互式获取用户输入并反转字符串。"""
    s = input("请输入一个字符串：")
    reversed_str = reverse_string(s)
    print(f"反转后的字符串是：{reversed_str}")

#### 练习 3.3：统计字符频率
# 编写一个函数 `count_characters(s)`，统计字符串中每个字符出现的次数，并返回一个字典。
# - 示例：
#   ```python
#   print(count_characters("hello"))
#   # 输出：{'h': 1, 'e': 1, 'l': 2, 'o': 1}

def count_char(strings):
   for i in strings:
      count=0
      for j in strings:
         if j==i:
            count+=1
         else:
            continue
      print(f"{i}:{count}",end=";")
# 没有返回一个字典
# 双重循环增加了事件复杂度O(n^2)，可以通过使用字典来优化，将时间复杂度降低到 O(n)。
# 代码没有处理字符串为空的情况。
def count_characters(s: str) -> dict:
    """统计字符串中每个字符出现的次数，并返回一个字典。"""
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            #会直接在空字典中新建“键”，并给键赋值1
    return char_count


### **5. 挑战题**
#### 练习 5.1：打印菱形图案
# 编写一个程序，根据用户输入的行数，打印一个菱形图案。
# - 示例：
#   ```
#   输入：5
#   输出：
#       *
#      ***
#     *****
#      ***
#       *

def print_diamond():
   n=get_pnumber("please enter an integer")
   for i in range(1,n+1):
      mid=n//2
      space_number=abs(mid-i+1)
      star_number=n-2*space_number
      print(f" "*{space_number}"*"*{star_number}" "*{space_number})
      #不需要使用f string。


def get_pnumber(prompt):
   while True:
      try:
         number=int(input(prompt))
         if number <=0:
            print("number smaller than zero,please retry")
         else:
            return number
      except ValueError:
         print("please enter an integer")
# 字符串格式化错误：print(f" "*{space_number}"*"*{star_number}" "*{space_number}) 这行代码的字符串格式化语法错误，会导致程序无法正常运行。
# 奇数行数处理：代码假设用户输入的 n 是奇数，但未对偶数输入进行处理，可能会导致菱形图案不完整或错误。
# 异常处理不足：get_pnumber 函数虽然处理了非整数输入和负数输入，但未处理用户输入为0的情况，这可能导致程序逻辑错误。
def print_diamond():
    n = get_pnumber("please enter an integer: ")
    mid = n // 2
    for i in range(1, n + 1):
        space_number = abs(mid - i + 1)
        star_number = n - 2 * space_number
        print(" " * space_number + "*" * star_number + " " * space_number)
        # 注意这里的字符串拼接直接用了+号,字符相加的效果就是拼接
        # print("".join([" " * space_number, "*" * star_number, " " * space_number]))
        # 也可以使用join方法进行字符串拼接，提高性能

def get_pnumber(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Number must be greater than zero, please retry.")
            else:
                return number
        except ValueError:
            print("Please enter a valid integer.")

