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
pd.concat([df1, df2])         # 连接数据框
df1.merge(df2)                # 合并数据框
df.pivot_table()              # 透视表
```
