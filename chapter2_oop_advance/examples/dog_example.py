#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
这是一个演示类和实例基本概念的示例文件
"""

class Dog:
    """
    狗类
    演示了类变量、实例变量和实例方法的使用
    """
    # 类变量，所有实例共享
    species = "犬科动物"
    count = 0
    
    def __init__(self, name, age, breed="未知"):
        """
        初始化方法（构造函数）
        :param name: 狗的名字
        :param age: 狗的年龄
        :param breed: 狗的品种
        """
        # 实例变量，每个实例独有
        self.name = name
        self.age = age
        self.breed = breed
        self.is_sitting = False
        
        # 增加狗的计数
        Dog.count += 1
        print(f"一只新的狗被创建！当前共有{Dog.count}只狗。")
    
    def bark(self):
        """让狗叫"""
        return f"{self.name}：汪汪！"
    
    def sit(self):
        """让狗坐下"""
        if self.is_sitting:
            return f"{self.name}已经是坐着的。"
        else:
            self.is_sitting = True
            return f"{self.name}坐下了。"
    
    def stand(self):
        """让狗站起来"""
        if not self.is_sitting:
            return f"{self.name}已经是站着的。"
        else:
            self.is_sitting = False
            return f"{self.name}站起来了。"
    
    def dog_years(self):
        """计算狗年龄（1人年 = 7狗年）"""
        return self.age * 7
    
    def get_info(self):
        """获取狗的信息"""
        posture = "坐着" if self.is_sitting else "站着"
        return f"{self.name}是一只{self.age}岁的{self.breed}，它是{self.species}，现在正{posture}。"
    
    def __str__(self):
        """打印对象时的字符串表示"""
        return f"狗：{self.name}，{self.age}岁，品种：{self.breed}"
    
    def __del__(self):
        """析构函数，当对象被销毁时调用"""
        Dog.count -= 1
        print(f"{self.name}被送走了，当前还有{Dog.count}只狗。")


# 演示代码
if __name__ == "__main__":
    print("=" * 50)
    print("创建第一只狗")
    dog1 = Dog("旺财", 3, "金毛")
    print(dog1.get_info())
    
    print("\n" + "=" * 50)
    print("创建第二只狗")
    dog2 = Dog("小黑", 2, "哈士奇")
    print(dog2.get_info())
    
    print("\n" + "=" * 50)
    print("让狗执行动作")
    print(dog1.bark())
    print(dog1.sit())
    print(dog1.sit())  # 重复命令
    print(dog2.bark())
    print(dog2.stand())  # 本来就是站着的
    
    print("\n" + "=" * 50)
    print("计算狗年龄")
    print(f"{dog1.name}的人类年龄是{dog1.age}岁，相当于狗的{dog1.dog_years()}岁")
    print(f"{dog2.name}的人类年龄是{dog2.age}岁，相当于狗的{dog2.dog_years()}岁")
    
    print("\n" + "=" * 50)
    print("访问类变量")
    print(f"通过类访问：Dog.species = {Dog.species}")
    print(f"通过实例访问：dog1.species = {dog1.species}, dog2.species = {dog2.species}")
    
    print("\n" + "=" * 50)
    print("修改类变量")
    Dog.species = "驯化犬科动物"
    print(f"修改后，Dog.species = {Dog.species}")
    print(f"所有实例都会看到变化：dog1.species = {dog1.species}, dog2.species = {dog2.species}")
    
    print("\n" + "=" * 50)
    print("动态添加实例属性")
    dog1.favorite_toy = "网球"
    print(f"{dog1.name}最喜欢的玩具是{dog1.favorite_toy}")
    # 注意：dog2没有favorite_toy属性，尝试访问会导致AttributeError
    
    print("\n" + "=" * 50)
    print("对象的字符串表示")
    print(dog1)  # 会调用__str__方法
    print(dog2)  # 会调用__str__方法
    
    print("\n" + "=" * 50)
    print("删除对象")
    print(f"当前狗的数量：{Dog.count}")
    del dog1
    print(f"删除dog1后，当前狗的数量：{Dog.count}")
    
    print("\n" + "=" * 50)
    print("程序结束时，剩余的狗对象会被自动回收") 