# Chapter 3: Python数据类型

## 1. 字典（Dictionary）

字典是Python中的键值对集合，使用花括号 `{}` 定义。

```python
# 创建字典
student = {
    'name': 'Tom',
    'age': 20,
    'scores': [85, 90, 88]
}

# 访问元素
print(student['name'])  # Tom

# 修改值
student['age'] = 21

# 添加新键值对
student['grade'] = 'A'

# 删除键值对
del student['scores']

# 常用方法
keys = student.keys()     # 获取所有键
values = student.values() # 获取所有值
items = student.items()   # 获取所有键值对
```

## 2. 集合（Set）

集合是无序的唯一元素集合，使用花括号 `{}` 或 `set()` 创建。

```python
# 创建集合
numbers = {1, 2, 3, 4, 5}
fruits = set(['apple', 'banana', 'orange'])

# 集合操作
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 并集
print(A | B)  # {1, 2, 3, 4, 5, 6}

# 交集
print(A & B)  # {3, 4}

# 差集
print(A - B)  # {1, 2}

# 添加和删除元素
numbers.add(6)
numbers.remove(1)
```

## 3. 列表（List）

列表是有序的元素集合，使用方括号 `[]` 定义。

```python
# 创建列表
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'hello', 3.14, True]

# 列表切片
print(numbers[1:4])  # [2, 3, 4]

# 列表操作
numbers.append(6)    # 添加元素
numbers.extend([7, 8]) # 扩展列表
numbers.insert(0, 0) # 插入元素
numbers.remove(3)    # 删除元素
numbers.sort()       # 排序
```

## 4. 数据类型转换

```python
# 字符串转换
str(123)      # '123'
int('123')    # 123
float('3.14') # 3.14

# 列表转换
list('hello') # ['h', 'e', 'l', 'l', 'o']
tuple([1,2,3]) # (1, 2, 3)

# 集合转换
set([1,2,2,3]) # {1, 2, 3}
list({1,2,3})  # [1, 2, 3]

# 字典转换
dict([('a',1), ('b',2)]) # {'a': 1, 'b': 2}
```

## 5. NumPy 简介

NumPy是Python中用于科学计算的核心库。

```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))

# 数组运算
arr + 2  # 广播运算
arr * 2
```

## 6. Pandas 简介

Pandas提供了DataFrame数据结构，适用于处理表格数据。

```python
import pandas as pd

# 创建DataFrame
df = pd.DataFrame({
    'Name': ['Tom', 'Jerry', 'Spike'],
    'Age': [20, 18, 22],
    'Grade': ['A', 'B', 'A']
})

# 基本操作
print(df.head())
print(df['Name'])
print(df.describe())
```
