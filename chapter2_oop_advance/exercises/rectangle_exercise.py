#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
矩形类练习

练习要求：
1. 完成Rectangle类的实现
2. 添加计算面积、周长的方法
3. 添加比较两个矩形大小的方法
4. 测试你的实现
"""

class Rectangle:
    """
    矩形类
    
    属性:
    - length: 长度
    - width: 宽度
    
    方法:
    - area(): 计算矩形面积
    - perimeter(): 计算矩形周长
    - is_square(): 判断是否为正方形
    - __eq__(other): 判断两个矩形是否相等
    - __lt__(other): 比较两个矩形的大小（基于面积）
    - __str__(): 字符串表示
    """
    
    def __init__(self, length, width):
        """
        初始化矩形
        
        参数:
        - length: 长度
        - width: 宽度
        """
        # 添加代码：初始化length和width属性
        pass  # 替换这行代码
    
    def area(self):
        """计算矩形面积"""
        # 添加代码：计算并返回面积
        pass  # 替换这行代码
    
    def perimeter(self):
        """计算矩形周长"""
        # 添加代码：计算并返回周长
        pass  # 替换这行代码
    
    def is_square(self):
        """判断是否为正方形"""
        # 添加代码：判断是否为正方形
        pass  # 替换这行代码
    
    def __eq__(self, other):
        """
        判断两个矩形是否相等
        两个矩形相等：当且仅当长宽都相等（忽略方向）
        """
        # 添加代码：判断self与other是否相等
        pass  # 替换这行代码
    
    def __lt__(self, other):
        """
        比较两个矩形的大小
        self < other：当且仅当self的面积小于other的面积
        """
        # 添加代码：比较self与other的大小
        pass  # 替换这行代码
    
    def __str__(self):
        """返回矩形的字符串表示"""
        # 添加代码：返回矩形的字符串表示
        pass  # 替换这行代码


# 测试代码
if __name__ == "__main__":
    # 创建矩形
    rect1 = Rectangle(5, 3)
    rect2 = Rectangle(4, 4)
    rect3 = Rectangle(3, 5)  # 与rect1尺寸相同但方向不同
    
    # 测试面积和周长
    print(f"矩形1面积: {rect1.area()}, 周长: {rect1.perimeter()}")
    print(f"矩形2面积: {rect2.area()}, 周长: {rect2.perimeter()}")
    
    # 测试是否为正方形
    print(f"矩形1是正方形吗? {rect1.is_square()}")
    print(f"矩形2是正方形吗? {rect2.is_square()}")
    
    # 测试比较
    print(f"矩形1 == 矩形3? {rect1 == rect3}")  # 应为True，因为5x3和3x5是相同的矩形
    print(f"矩形1 < 矩形2? {rect1 < rect2}")    # 取决于面积比较
    print(f"矩形2 < 矩形1? {rect2 < rect1}")    # 与上一行结果相反
    
    # 测试排序
    rectangles = [Rectangle(8, 2), Rectangle(5, 5), Rectangle(6, 3), Rectangle(4, 4)]
    sorted_rectangles = sorted(rectangles)  # 按面积从小到大排序
    print("\n按面积排序后的矩形:")
    for rect in sorted_rectangles:
        print(f"{rect} - 面积: {rect.area()}")


# 参考答案（仅供参考，建议先自己完成再查看）
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def is_square(self):
        return self.length == self.width
    
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return (self.length == other.length and self.width == other.width) or \
               (self.length == other.width and self.width == other.length)
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    def __str__(self):
        return f"矩形({self.length} x {self.width})"
""" 