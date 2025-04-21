# Pandas Cheatsheet

## 创建数据
```python
pd.DataFrame(data)              # 从字典创建
pd.read_csv('file.csv')        # 读取CSV文件
pd.read_excel('file.xlsx')     # 读取Excel文件
```

## 基本操作
```python
df.head()                      # 查看前几行
df.info()                      # 数据信息
df.describe()                  # 统计描述
df.shape                       # 数据形状
```

## 数据选择
```python
df['column']                   # 选择列
df.loc['row']                  # 按标签选择
df.iloc[0]                     # 按位置选择
df.query('age > 25')          # 查询数据
```

## 数据处理
```python
df.dropna()                    # 删除空值
df.fillna(0)                   # 填充空值
df.sort_values('column')       # 排序
df.groupby('column')          # 分组
```

## 数据合并
```python
pd.concat([df1, df2], axis=0, join='outer', ignore_index=True)         
# 连接数据框，axis=0,1按行/列拼接。ignore_index 拼接后是否重新生成索引。 join = outer求并集，inner求交集。
df1.merge(df2, on=None, left_on=None, right_on=None, how='inner')              
# 合并数据框。on: 指定用于连接的列名，要求在两个数据框中都存在。left_on/right_on: 分别指定左表和右表的连接键。how: 指定连接方式，可选值有 'inner'（内连接）、'outer'（外连接）、'left'（左连接）、'right'（右连接）。
df.pivot_table()              # 透视表
```

## SQL 查询
```python
import pandas as pd
import pandasql as psql

# 方法 1: 使用 pandasql (需要先安装: pip install pandasql)
pysqldf = lambda q: psql.sqldf(q, globals())
sql = """
SELECT * 
FROM df 
WHERE age > 25
"""
result = pysqldf(sql)
#这是一个 lambda 函数，创建了一个简写的函数名 pysqldf
# psql.sqldf() 是 pandasql 的核心函数，用于执行 SQL 查询
# globals() 让函数能访问全局变量空间中的所有 DataFrame


# 方法 2: 使用 pandas 内置的 query
df.query('age > 25')  # 等同于上面的 SQL

# 方法 3: 直接连接数据库
from sqlalchemy import create_engine
engine = create_engine('sqlite:///database.db')
df = pd.read_sql('SELECT * FROM table_name', engine)
```

