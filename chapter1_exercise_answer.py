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
      
      