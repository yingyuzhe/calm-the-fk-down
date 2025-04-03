# 基本语法
lambda 参数1, 参数2, ...: 表达式

# 示例
# 无参数
lambda: "Hello"

# 一个参数
lambda x: x * 2

# 多个参数
lambda x, y: x + y

# 带默认值的参数
lambda x=1, y=2: x + y

# 带*args和**kwargs
lambda *args, **kwargs: sum(args)

# 表达式要求
# 只能包含一个表达式
lambda x: x * 2  # 单个表达式

# 错误示例
lambda x: print(x); return x  # 不能包含多个语句
lambda x: if x > 0: return x  # 不能包含if语句
lambda x: for i in range(x): print(i)  # 不能包含循环

# 复杂表达式示例
lambda x: x * 2 if x > 0 else -x  # 可以使用三元运算符
lambda x: [i * 2 for i in range(x)]  # 可以使用列表推导式

#3、返回结果特点
# 自动返回表达式结果
# 示例1：直接返回
lambda x: x * 2  # 返回x * 2的结果

# 示例2：条件返回
lambda x: "正数" if x > 0 else "负数"  # 根据条件返回不同结果

# 示例3：返回多个值（元组）
lambda x: (x * 2, x * 3)  # 返回一个元组

# 示例4：返回None
lambda x: print(x)  # print()返回None

# 4 应用示例
# 排序
students = [
    {"name": "张三", "score": 92},
    {"name": "李四", "score": 85}
]
sorted_students = sorted(students, key=lambda x: x['score'])

# 过滤
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# 映射
squares = list(map(lambda x: x**2, numbers))

# 作为函数参数
def process_data(data, transform):
    return transform(data)

result = process_data(5, lambda x: x * 2)