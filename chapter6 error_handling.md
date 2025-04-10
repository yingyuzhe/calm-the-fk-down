# 第6章：错误处理与调试技巧

## 1. 错误处理基础

### 1.1 异常与错误的区别
```python
# 语法错误 (Error)
if x = 5:  # SyntaxError: 不能使用单个=进行比较
    print(x)

# 运行时异常 (Exception)
x = 10
y = 0
result = x / y  # ZeroDivisionError: 除以零错误
```

### 1.2 常见异常类型
```python
# TypeError: 类型错误
result = "hello" + 123

# ValueError: 值错误
number = int("abc")

# IndexError: 索引错误
list = [1, 2, 3]
value = list[5]

# KeyError: 键错误
dict = {"name": "Tom"}
value = dict["age"]

# FileNotFoundError: 文件未找到错误
with open("不存在的文件.txt") as f:
    content = f.read()
```

## 2. 异常处理最佳实践

### 2.1 基本的try-except结构
```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return None

# 使用示例
print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # None
```

### 2.2 处理多个异常
```python
def process_data(data):
    try:
        value = int(data)
        result = 100 / value
        return result
    except ValueError:
        print("错误：输入必须是数字")
    except ZeroDivisionError:
        print("错误：输入不能为零")
    except Exception as e:
        print(f"发生未知错误：{e}")
    return None

# 使用示例
print(process_data("abc"))  # 错误：输入必须是数字
print(process_data("0"))    # 错误：输入不能为零
print(process_data("5"))    # 20.0
```

### 2.3 finally子句
```python
def read_file(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        return content
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在")
        return None
    finally:
        if file:
            file.close()
            print("文件已关闭")

# 使用示例
content = read_file("test.txt")
```

### 2.4 使用上下文管理器
```python
def read_file_content(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：文件 {filename} 不存在")
        return None

# 使用示例
content = read_file_content("test.txt")
```

## 3. 自定义异常

### 3.1 创建自定义异常类
```python
class InsufficientFundsError(Exception):
    """当账户余额不足时抛出"""
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"余额不足。当前余额: ¥{self.balance}, 取款金额: ¥{amount}"
            )
        self.balance -= amount
        return self.balance

# 使用示例
account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"操作失败：{e}")
```

## 4. 调试技巧

### 4.1 使用print进行简单调试
```python
def complex_calculation(x, y):
    print(f"输入参数：x={x}, y={y}")  # 调试打印
    
    result = x * y
    print(f"计算结果：{result}")  # 调试打印
    
    return result

# 使用示例
complex_calculation(5, 3)
```

### 4.2 使用断言
```python
def process_age(age):
    assert age >= 0, "年龄不能为负数"
    if age < 18:
        return "未成年"
    return "成年"

# 使用示例
try:
    print(process_age(-5))
except AssertionError as e:
    print(f"断言错误：{e}")
```

### 4.3 使用logging模块
```python
import logging

# 配置logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def complex_function(x):
    logging.debug(f"函数输入: {x}")
    
    result = x * 2
    logging.debug(f"计算结果: {result}")
    
    if result > 100:
        logging.warning("结果超过100")
    
    return result

# 使用示例
complex_function(60)
```

## 5. 实践示例：文件处理程序

```python
import logging
import json
from pathlib import Path

class FileProcessError(Exception):
    """文件处理错误的基类"""
    pass

class FileProcessor:
    def __init__(self, directory):
        self.directory = Path(directory)
        self._setup_logging()
    
    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='file_processor.log'
        )
    
    def process_file(self, filename):
        try:
            file_path = self.directory / filename
            
            # 检查文件是否存在
            if not file_path.exists():
                raise FileProcessError(f"文件不存在：{filename}")
            
            # 读取并处理文件
            with file_path.open('r') as f:
                data = json.load(f)
                logging.info(f"成功读取文件：{filename}")
                return data
                
        except json.JSONDecodeError:
            logging.error(f"JSON解析错误：{filename}")
            raise FileProcessError(f"文件格式错误：{filename}")
        except Exception as e:
            logging.error(f"处理文件时发生错误：{e}")
            raise FileProcessError(f"处理文件时发生错误：{e}")

# 使用示例
processor = FileProcessor("data")
try:
    data = processor.process_file("config.json")
    print("文件处理成功！")
except FileProcessError as e:
    print(f"文件处理失败：{e}")
```

此代码示例展示了如何在实际项目中综合运用异常处理、日志记录和文件操作。建议初学者仔细阅读并尝试修改代码，以更好地理解错误处理的应用。