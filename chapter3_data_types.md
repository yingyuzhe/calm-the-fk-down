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
fruits = set('apple', 'banana', 'orange') #报错，set函数中只能传入一个参数，需要用list【】起来。

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
#列表元素可以不同

# 列表切片
print(numbers[1:4])  # [2, 3, 4]

# 列表操作
numbers.append(6)    # 添加元素
numbers.extend([7, 8]) # 扩展列表
numbers.insert(0, 1) # 插入元素，表示在第0个位置插入1值
numbers.remove(3)    # 删除元素3， 不是删除第三个元素
numbers.pop(3)       # 删除第三个元素；同时返回被删除的元素。
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
tuple(1,2,3)  #报错，和set()一样只能传入一个参数，需要用list【】起来。



# 集合转换
set([1,2,2,3]) # {1, 2, 3}
list({1,2,3})  # [1, 2, 3]

# 字典转换
dict([('a',1), ('b',2)]) # {'a': 1, 'b': 2}
```
### dict(),list(),set(),tuple() 函数都只能传入一个参数。参数可以是[],{},''。参数不可以是（a,b,c）的形式。

## 5. NumPy 简介

NumPy是Python中用于科学计算的核心库。

```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5]) #形状（Shape）：(5,)，表示一个长度为 5 的一维数组。
zeros = np.zeros((3, 3)) #形状（Shape）：(3,3)，表示一个 3 行 3 列的二维数组。np.zeros()会将所有元素赋值为0.0
ones = np.ones((2, 4)) #形状（Shape）：(2,4)，表示一个 2 行 4 列的二维数组。np.ones()会将所有元素赋值为1.0
print(type(arr))  # 可以查看数据类型
```

### 5.1. **np数据类型和python原生数据类型的区别**

| 特性                | `np.array([1, 2, 3, 4, 5])`       | `list([1, 2, 3, 4, 5])`         |
|---------------------|-----------------------------------|----------------------------------|
| **数据类型**         | `<class 'numpy.ndarray'>`        | `<class 'list'>`                |
| **性能**             | 高效的数值计算                   | 一般用途，不适合大规模数值计算   |
| **维度支持**         | 支持多维数组                     | 只能表示一维或嵌套的一维列表     |
| **广播运算**         | 支持广播运算（如 `arr + 2`）     | 不支持广播运算                  |
| **内存占用**         | 更紧凑的内存布局                 | 内存占用较大                   |


# 数组运算
arr + 2  # 广播运算，即对数组内所有元素+2
arr * 2 # 广播运算，即对数组内所有元素*2


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
print(type(df))
<class 'pandas.core.frame.DataFrame'>

# 基本操作
print(df.head())
print(df['Name'])
print(df.describe())
```
### 6.1 df数据类型的特征和优势
### Pandas DataFrame 数据类型的特点和优势

Pandas 是 Python 中用于数据处理和分析的强大库，其核心数据结构是 **DataFrame**。以下是 Pandas DataFrame 的特点和优势的详细说明：

---

#### 1. **二维表格结构**
- **特点**：DataFrame 是一个二维表格数据结构，类似于电子表格或 SQL 表格。
- **优势**：
  - 易于理解：直观地表示行和列的数据。
  - 灵活操作：支持按列名、行索引等多种方式访问数据。
  - 每一列的数据类型必须相同。

  ```python
  import pandas as pd
  df = pd.DataFrame({
      'Name': ['Tom', 'Jerry', 'Spike'],
      'Age': [20, 18, 22],
      'Grade': ['A', 'B', 'A']
  })
  print(df)
  ```

---

#### 2. **灵活的索引**
- **特点**：支持自定义行索引（Index）和列名（Columns）。
- **优势**：
  - 快速定位：可以通过行索引或列名快速访问数据。
  - 数据对齐：在合并或运算时，自动对齐索引和列。

  ```python
  df = pd.DataFrame({
      'Name': ['Tom', 'Jerry', 'Spike'],
      'Age': [20, 18, 22]
  }, index=['a', 'b', 'c'])
  print(df.loc['a'])  # 按行索引访问
  print(df['Age'])    # 按列名访问
  ```

---

#### 3. **强大的数据处理能力**
- **特点**：提供丰富的数据操作方法。
- **优势**：
  - 数据清洗：支持缺失值处理（如 `fillna`、`dropna`）、重复值检测（如 `duplicated`、`drop_duplicates`）。
  - 数据转换：支持列的重命名（`rename`）、数据类型的转换（`astype`）。
  - 数据聚合：支持分组操作（`groupby`）、统计计算（如 `mean`、`sum`）。

  ```python
  # 缺失值处理
  df.fillna(0, inplace=True)

  # 分组统计
  grouped = df.groupby('Grade').mean()
  print(grouped)
  ```

---

#### 4. **高效的性能**
- **特点**：基于 NumPy 实现，底层使用 C 语言优化。
- **优势**：
  - 高速计算：对于大规模数据集，Pandas 提供了高效的矢量化操作。
  - 内存优化：支持稀疏数据结构和类别型数据（`category`），减少内存占用。

  ```python
  # 矢量化操作 = np的广播运算
  df['Age'] += 1  # 对整列进行加法操作。
  ```

---

#### 5. **丰富的输入输出支持**
- **特点**：支持多种文件格式的读写。
- **优势**：
  - 文件兼容性：可以轻松读取 CSV、Excel、SQL 数据库、JSON 等格式的数据。
  - 数据共享：支持将 DataFrame 导出为多种格式，便于与其他工具集成。

  ```python
  # 读取 CSV 文件
  df = pd.read_csv('data.csv')

  # 导出为 Excel 文件
  df.to_excel('output.xlsx', index=False)
  ```

---

#### 6. **时间序列支持**
- **特点**：内置时间序列功能，支持日期解析、频率转换等。
- **优势**：
  - 时间操作：可以轻松处理时间戳数据（如 `pd.Timestamp`）。
  - 数据采样：支持重采样（`resample`）和滚动窗口计算（`rolling`）。

  ```python
  # 创建时间序列
  dates = pd.date_range('2023-01-01', periods=5)
  df = pd.DataFrame({'Date': dates, 'Value': range(5)})
  print(df)
  ```

---

#### 7. **可视化支持**
- **特点**：内置绘图功能，基于 Matplotlib 实现。
- **优势**：
  - 快速绘图：可以直接绘制折线图、柱状图等。
  - 数据洞察：通过可视化快速了解数据分布和趋势。

  ```python
  # 绘制柱状图
  df['Value'].plot(kind='bar')
  ```

---

### 总结

| 特点                | 描述                                                                 |
|---------------------|----------------------------------------------------------------------|
| **二维表格结构**     | 类似电子表格，支持行和列的操作                                       |
| **灵活的索引**       | 支持自定义索引和列名，方便数据定位                                   |
| **强大的数据处理**   | 提供清洗、转换、聚合等功能，适合复杂数据操作                         |
| **高效的性能**       | 基于 NumPy 实现，支持矢量化操作，适用于大规模数据                     |
| **丰富的输入输出**   | 支持多种文件格式（CSV、Excel、SQL 等），便于数据导入导出             |
| **时间序列支持**     | 内置时间序列功能，适合金融、气象等领域                               |
| **可视化支持**       | 内置绘图功能，方便快速生成图表                                         |

Pandas 的这些特点和优势使其成为数据分析领域的首选工具之一，无论是小规模数据探索还是大规模数据处理，都能高效完成任务。