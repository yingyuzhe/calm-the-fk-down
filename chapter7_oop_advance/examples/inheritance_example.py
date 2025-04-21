#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
继承示例 - 动物类层次结构
演示Python中类继承的基本概念
"""

class Animal:
    """动物基类"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"动物{name}被创建")
    
    def eat(self, food):
        return f"{self.name}正在吃{food}"
    
    def sleep(self):
        return f"{self.name}正在睡觉"
    
    def make_sound(self):
        return f"{self.name}发出了声音"
    
    def __str__(self):
        return f"{self.name}，{self.age}岁"


class Mammal(Animal):
    """哺乳动物类，继承自Animal"""
    
    def __init__(self, name, age, fur_color):
        # 调用父类的初始化方法
        super().__init__(name, age)
        # 添加哺乳动物特有的属性
        self.fur_color = fur_color
        self.body_temperature = "恒温"
        print(f"哺乳动物{name}被创建")
    
    def give_birth(self):
        return f"{self.name}可以生育幼崽"
    
    # 重写父类方法
    def make_sound(self):
        # 首先调用父类方法
        original_sound = super().make_sound()
        # 然后添加特定行为
        return f"{original_sound}，这是哺乳动物的声音"


class Bird(Animal):
    """鸟类，继承自Animal"""
    
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span
        self.has_feathers = True
        print(f"鸟类{name}被创建")
    
    def fly(self):
        return f"{self.name}正在飞翔"
    
    def lay_eggs(self):
        return f"{self.name}可以下蛋"
    
    # 完全重写父类方法
    def make_sound(self):
        return f"{self.name}发出了鸟叫声"


class Dog(Mammal):
    """狗类，继承自哺乳动物类"""
    
    def __init__(self, name, age, fur_color, breed):
        super().__init__(name, age, fur_color)
        self.breed = breed
        self.is_loyal = True
        print(f"狗{name}被创建")
    
    def bark(self):
        return f"{self.name}：汪汪！"
    
    def fetch(self, item):
        return f"{self.name}叼回了{item}"
    
    # 重写父类的方法
    def make_sound(self):
        return f"{self.name}：汪汪汪！"


class Cat(Mammal):
    """猫类，继承自哺乳动物类"""
    
    def __init__(self, name, age, fur_color, is_indoor):
        super().__init__(name, age, fur_color)
        self.is_indoor = is_indoor
        print(f"猫{name}被创建")
    
    def meow(self):
        return f"{self.name}：喵~"
    
    def purr(self):
        return f"{self.name}在打呼噜"
    
    # 重写父类的方法
    def make_sound(self):
        return f"{self.name}：喵喵喵！"


class Parrot(Bird):
    """鹦鹉类，继承自鸟类"""
    
    def __init__(self, name, age, wing_span, can_speak):
        super().__init__(name, age, wing_span)
        self.can_speak = can_speak
        print(f"鹦鹉{name}被创建")
    
    def speak(self, words):
        if self.can_speak:
            return f"{self.name}说：'{words}'"
        else:
            return f"{self.name}不会说话"
    
    # 重写父类的方法
    def make_sound(self):
        if self.can_speak:
            return f"{self.name}：'你好，我是鹦鹉！'"
        else:
            return super().make_sound()


# 演示代码
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("创建动物实例")
    generic_animal = Animal("未知动物", 5)
    print(generic_animal.make_sound())
    print(generic_animal.eat("食物"))
    
    print("\n" + "=" * 50)
    print("创建哺乳动物实例")
    some_mammal = Mammal("某哺乳动物", 3, "棕色")
    print(some_mammal.make_sound())
    print(some_mammal.give_birth())
    print(f"毛色：{some_mammal.fur_color}")
    
    print("\n" + "=" * 50)
    print("创建狗实例")
    dog = Dog("旺财", 2, "金色", "金毛")
    print(dog.make_sound())  # 调用Dog类的make_sound方法
    print(dog.bark())        # 调用Dog类特有的方法
    print(dog.eat("骨头"))   # 调用从Animal继承的方法
    print(dog.give_birth())  # 调用从Mammal继承的方法
    print(f"品种：{dog.breed}，毛色：{dog.fur_color}")
    
    print("\n" + "=" * 50)
    print("创建猫实例")
    cat = Cat("咪咪", 1, "黑色", True)
    print(cat.make_sound())  # 调用Cat类的make_sound方法
    print(cat.purr())        # 调用Cat类特有的方法
    print(cat.sleep())       # 调用从Animal继承的方法
    print(f"是室内猫吗：{cat.is_indoor}")
    
    print("\n" + "=" * 50)
    print("创建鹦鹉实例")
    talking_parrot = Parrot("小绿", 2, 30, True)
    print(talking_parrot.make_sound())  # 调用Parrot类的make_sound方法
    print(talking_parrot.speak("你好"))  # 调用Parrot类特有的方法
    print(talking_parrot.fly())         # 调用从Bird继承的方法
    print(talking_parrot.lay_eggs())    # 调用从Bird继承的方法
    
    silent_parrot = Parrot("小红", 1, 25, False)
    print(silent_parrot.make_sound())   # 不会说话的鹦鹉
    
    print("\n" + "=" * 50)
    print("多态性演示")
    animals = [generic_animal, some_mammal, dog, cat, talking_parrot, silent_parrot]
    
    print("\n所有动物的声音：")
    for animal in animals:
        print(f"{type(animal).__name__}: {animal.make_sound()}")
    
    print("\n所有动物信息：")
    for animal in animals:
        print(f"{type(animal).__name__}: {animal}")
        
    print("\n" + "=" * 50)
    print("isinstance和issubclass演示")
    print(f"dog是Animal的实例吗？{isinstance(dog, Animal)}")
    print(f"dog是Mammal的实例吗？{isinstance(dog, Mammal)}")
    print(f"dog是Bird的实例吗？{isinstance(dog, Bird)}")
    print(f"Dog是Mammal的子类吗？{issubclass(Dog, Mammal)}")
    print(f"Dog是Animal的子类吗？{issubclass(Dog, Animal)}")
    print(f"Mammal是Dog的子类吗？{issubclass(Mammal, Dog)}") 