# 第一章：Python基础语法

## 1. 条件判断

### if语句
```python
# 基本if语句
if 条件:
    执行代码

# if-else语句
if 条件:
    执行代码1
else:
    执行代码2

# if-elif-else语句
if 条件1:
    执行代码1
elif 条件2:
    执行代码2
else:
    执行代码3
```

### 示例：成绩判断
```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

## 2. 循环结构

### while循环
```python
# 基本while循环
while 条件:
    执行代码

# 示例：计算1到100的和
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(f"1到100的和是：{sum}")
```

### for循环
```python
# 基本for循环
for 变量 in 序列:
    执行代码

# 示例：遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 使用range函数
for i in range(5):  # 0到4
    print(i)
```

### 循环控制
```python
# break：跳出循环
for i in range(10):
    if i == 5:
        break
    print(i)

# continue：跳过当前迭代
for i in range(5):
    if i == 2:
        continue
    print(i)
```

## 3. 函数定义

### 基本函数
```python
# 定义函数
def 函数名(参数1, 参数2):
    函数体
    return 返回值

# 示例：计算两个数的和
def add(a, b):
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")
```

### 参数类型
```python
# 默认参数
# 当输入greet()时，默认返回"你好世界"。 输入greet(name="333") 返回"你好，333"
def greet(name="世界"):
    print(f"你好，{name}！")

# 关键字参数
def person_info(name, age, city):
    print(f"姓名：{name}，年龄：{age}，城市：{city}")

person_info(name="张三", age=25, city="北京")
```

### 返回值
```python
# 返回多个值
def get_circle_info(radius):
    area = 3.14 * radius * radius
    perimeter = 2 * 3.14 * radius
    return area, perimeter

area, perimeter = get_circle_info(5)
print(f"面积：{area}，周长：{perimeter}")
```

## 4. 综合练习

### 练习1：判断素数
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 测试
print(is_prime(17))  # True
print(is_prime(20))  # False
```

### 练习2：斐波那契数列
```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# 测试
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 5. 总结

本章学习了：
1. 条件判断：if、elif、else的使用
2. 循环结构：while和for循环
3. 函数定义：参数、返回值、作用域
4. 综合应用：通过练习巩固所学知识

建议：
- 多写代码练习
- 尝试修改示例代码
- 自己设计小练习
- 阅读他人代码学习 