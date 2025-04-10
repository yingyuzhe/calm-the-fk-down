# NumPy Cheatsheet

## 创建数组
```python
np.array([1, 2, 3])              # 从列表创建
np.zeros((3, 3))                 # 创建全0数组
np.ones((2, 4))                  # 创建全1数组
np.empty((2, 3))                 # 创建空数组
np.arange(10)                    # 创建0-9数组
np.linspace(0, 1, 5)            # 创建均匀分布数组
```

## 数组操作
```python
arr.reshape(3, 4)                # 改变形状
arr.T                            # 转置
arr.flatten()                    # 展平数组
np.concatenate((arr1, arr2))     # 连接数组
```

## 数学运算
```python
np.sum(arr)                      # 求和
np.mean(arr)                     # 平均值
np.std(arr)                      # 标准差
np.min(arr)                      # 最小值
np.max(arr)                      # 最大值
```

## 索引和切片
```python
arr[0]                          # 第一个元素
arr[1:5]                        # 切片
arr[1:5:2]                      # 带步长切片
arr[:, 1]                       # 二维数组列
```

## 条件操作
```python
arr > 5                         # 条件判断
arr[arr > 5]                    # 条件索引
np.where(arr > 5)               # 条件查找
```
