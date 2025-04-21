# # Chapter 3 练习题

# ## 基础练习

# 1. 创建一个字典，包含5个学生的姓名和年龄，然后实现以下操作：
#    - 添加一个新学生
#    - 删除一个学生
#    - 修改一个学生的年龄
#    - 打印所有学生的姓名

import pandas as pd
from pandas import DataFrame as df

dict = {
    'lihua':11,
    'hanmeimei':20,
    'wocao':12,
    'eiya':15,
    'hei':12
}

dict['new']=10
dict['eiya']=16
# 删除键值对
del dict['hanmeimei']
names=dict.keys()
print("所有学生的姓名:",names) #可，简单拼接不用f string
print(f"所有学生的姓名: {names}") #也可

# 2. 给定两个列表 `[1,2,3,4,5]` 和 `[4,5,6,7,8]`，使用集合操作找出：
#    - 两个列表中的共同元素
#    - 只在第一个列表中出现的元素
#    - 两个列表的所有不重复元素
set1=set([1,2,3,4,5])
set2=set([4,5,6,7,8])
for i in set1:
    for j in set2:
        if i==j:
            print(i)
        else:
            continue
# 可以直接取交集： 
print(set1&set2)

for i in set1:
    for j in set2:
        if i==j:
            set1.remove(i) # 集合用remove
        else:
            continue
# 会报错，在遍历时不能改变集合的大小。 修改后
to_remove=[]
for i in set1:
    for j in set2:       
        if i==j:
            to_remove.append(i) # 集合用remove
        else:
            continue
set1-set(to_remove)

# 可以直接取差集： 
print(set1-set1&set2)

# 可以直接取并集：
print(set1|set2)
    
# 3. 编写代码实现列表的以下操作：
#    - 对列表 `[3,1,4,1,5,9,2,6,5,3,5]` 进行排序
#    - 删除重复元素
#    - 找出最大值和最小值
#    - 计算平均值

list1=list([3,1,4,1,5,9,2,6,5,3,5])
set1=set(list1)
list2=list(set1)
list2.sort()

# sorted（）函数可以接受任何可迭代对象，不修改原始对象。 
# .sorted（）可以接受可迭代对象，返回none，原对象被排序。

max_num= max(list1)
min_num= min(list1)
average= sum(list1)/len(list1)

# ## NumPy练习

# 4. 使用NumPy创建以下数组：
#    - 一个3x3的随机数组
#    - 一个从0到20的等差数列
#    - 一个5x5的单位矩阵

import numpy as np
random_array = np.random.rand(3, 3)
arange_array = np.arange(0, 21)  
#0-20的等差数列
arange_array2 = np.arange(20, 0,-1)
# 20-1的等差数列
identity_matrix = np.eye(5)

# arange（）常用于创造制定范围内的等间隔数组。 arange（start,stop,step默认1,dtype默认none), 返回一个一维的ndarray对象。
# eye() 用于创建一个二维数组（矩阵），其中对角线上的元素为 1，其余元素为 0。这种矩阵称为单位矩阵或身份矩阵。返回一个二维的ndarray对象。
# numpy.eye(N 行数, M=None 列数, k=0 对角线位置, dtype=<class 'float'>, order='C' 按行存储， F表示按列存储)

# 5. 对一个NumPy数组执行以下操作：
#    - 计算所有元素的平均值
#    - 找出大于平均值的所有元素
#    - 将数组重塑为新形状
a1 = np.arange(0, 21)  
a1.mean()
b=[]
for i in a1:
    if i>a1.mean():
        b.append(i)
    else:
        continue
#可以更加简洁
b = [i for i in a1 if i > a1.mean()]

# 假设我们将其重塑为一个 4x5 的数组
try:
    reshaped_array = a1.reshape(4, 5)
    print("重塑后的数组:\n", reshaped_array)
except ValueError as e:
    print("无法重塑数组:", e)

# ## Pandas练习

# 6. 创建一个包含学生信息的DataFrame：
#    - 包含姓名、年龄、成绩三列
#    - 计算平均成绩
#    - 找出成绩最高的学生
#    - 按成绩对学生排序
import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [20, 22, 21, 19, 23],
    'score': [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)
print(df)
average_score=df['score'].mean()
# 找出成绩最高的学生的索引
max_score_index = df['score'].idxmax()
max_score = df['score'].max()
print(type(max_score)) # 注意这里max（）方法返回的是np.int数据类型。因为pandas默认用numpy来处理数据，返回的都是numpy类型。
#可以将np.int转化为int类型
max_score=int(max_score)
# 用.loc[]属性获取索引对应的键值。注意.loc[]后面跟的是[],不是（），因为loc是df的一个属性而不是方法，只有方法需要用（）调用。
top_student = df.loc[max_score_index]

#.loc[]是pandas中dataframe的一个属性，返回的是一个indexer对象，这个indexer对象可以进一步通过[]进行索引。
# 语法： df.loc[row_label,column_label]
# row_label,column label可以是各种东西，下面是举例
print(df.loc[0, 'name'])  #选择单行单列
print(df.loc[[0,1], ['name', 'age']]) #选择多行多列，注意行列label要用list[]包围。
print(df.loc[0:3, 'name':'age']) #选择行切片和列切片，注意切片范围不需要用[]包围。
print(df.loc[(df['age'] > 20) & (df['score'] > 80)]) # 选择满足条件的行,注意多个条件时，每个条件要用括号（）包住。
print(df.loc[df['age'] > 20, ['name', 'age']])  # 选择满足条件的行和特定列
df.loc[0, 'age'] = 21 # 设置单个值
df.loc[1:2, ['age', 'score']] = [[23, 90], [22, 80]] # 设置多个值，注意后面赋值内容是传了一个2X2的矩阵进去
df.loc[df['年龄'] > 20, '成绩'] = 100 # 根据条件设置值

# 与loc的标签（label）索引方式不，datafram还有.iloc属性，他是通过位置索引的。
# 语法： df.iloc[row_index,column_index]
print(df.iloc[0, 0]) #选择第1行，第1列。 因为行label通常和行index一摸一样，所以.loc的行部分看起来和.iloc一样。

#df的排序方法.sort_values(by=column_name,ascending=boolean)
df.sort_values(by='score',ascending= False)

# 7. 数据处理实战：使用pandas
#    - 从CSV文件读取数据
#    - 处理缺失值
#    - 按特定条件筛选数据
#    - 创建数据透视表
import pandas as pd
import numpy as np

# 1. 创建示例CSV数据
sample_data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
    '年龄': [25, np.nan, 35, 28, 32],
    '部门': ['技术', '销售', '技术', '市场', '销售'],
    '工资': [10000, 12000, np.nan, 9000, 15000]
}
df = pd.DataFrame(sample_data)
df.to_csv('employee_data.csv', index=False)

# 2. 从CSV文件读取数据
df = pd.read_csv('employee_data.csv')
print("\n原始数据:")
print(df)

# 3. 处理缺失值
# 年龄用平均值填充，工资用中位数填充
df['年龄'] = df['年龄'].fillna(df['年龄'].mean())  #df['年龄']不再是dataframe格式，而是一个series序列。
df['工资'] = df['工资'].fillna(df['工资'].median())
print("\n处理缺失值后:")
print(df)
#.fillna(value,method=[ffill向前填充,bfill向后填充],inplace=booleam是否原地修改数据)

# 4. 按条件筛选数据
# 筛选技术部门的员工
tech_staff = df[df['部门'] == '技术']
tech_staff = df.loc[df['部门'] == '技术'] # 效果一样
print("\n技术部门员工:")
print(tech_staff)

# 筛选工资大于10000的员工
high_salary = df[df['工资'] > 10000] # 得到满足列条件的所有行
# boolean series = df['column_name'] + logical caculation
# df['工资'] > 10000 --> [F,T,T,F,T]
# sum(df['工资'] > 10000) --> 3 直接返回满足条件的行数
# df[boolean_series] -->  返回所有满足逻辑判断条件的行
print("\n高工资员工:")
print(high_salary)

# 5. 创建数据透视表
# 按部门统计平均工资和人数
pivot_table = pd.pivot_table(
    df, #除了第一个df没有用=号传参之外，其他参数传递都用了=号
    values=['工资', '年龄'],  # 指数据透视表中的指标字段
    index=['部门'], # 指数据透视表中的维度字段
    aggfunc={           # 指数据透视表中指标字段的计算方式： 计数、求和 ……
        '工资': 'mean',  # 注意这里面的计算函数，直接用‘’框起来了
        '年龄': 'count'
    }
)
print("\n部门统计:")
print(pivot_table)
# ## 挑战题

# 8. 创建一个学生成绩管理系统，要求：
#    - 使用dataframe存储学生信息（姓名、多门课程成绩）
#    - 支持添加/删除学生
#    - 支持修改成绩
#    - 计算每个学生的平均成绩
#    - 找出每门课程的最高分

import pandas as pd
import numpy as np

sample_data = {
    'name': ['张三', '李四', '王五', '赵六', '钱七'],
    'literature': [90, 80, np.nan, 70, 81],
    'history': [99, 95, 80, 60, 50],
    'math': [50, 60,70, np.nan, 90]
}

df = pd.DataFrame(sample_data)
def add_st(st_name,literature_score,history_score,math_score):
    df.loc[len(df)]={'name':st_name,
    'literature':literature_score,
    'history':history_score,
    'math':math_score}
    return df

def mod_st(st_name,col_list,new_value_list):
    df.loc[df['name']==st_name,col_list] = new_value_list
    return df

def del_st(st_name):
    df.set_index('name',inplace=True) # 将姓名设置为索引
    df=df.drop(st_name)
    return df

def st_avg_score(st_name):
    df['avg']=df['literature':'math'].mean()
    result = df[['name','avg']]
    return result

def max_score():
    result=pd.pivot_table(
        df,
        values=['literature','history','math'],
        aggfunc={
            'literature': 'max', 
            'history': 'max', 
            'math': 'max', 
        }
    )
    return result

# AI answer 
import pandas as pd
import numpy as np

class StudentManager:
    def __init__(self):
        self.df = pd.DataFrame({
            'name': ['张三', '李四', '王五', '赵六', '钱七'],
            'literature': [90, 80, np.nan, 70, 81],
            'history': [99, 95, 80, 60, 50],
            'math': [50, 60, 70, np.nan, 90]
        })
        
    def add_student(self, st_name, literature_score, history_score, math_score):
        """添加学生信息"""
        try:
            if st_name in self.df['name'].values:
                raise ValueError(f"学生 {st_name} 已存在！")
            
            new_student = {
                'name': st_name,
                'literature': literature_score,
                'history': history_score,
                'math': math_score
            }
            self.df = self.df.append(new_student, ignore_index=True)
            return True
        except Exception as e:
            print(f"添加学生失败: {str(e)}")
            return False

    def modify_scores(self, st_name, col_list, new_value_list):
        """修改学生成绩"""
        try:
            if st_name not in self.df['name'].values:
                raise ValueError(f"找不到学生 {st_name}")
            if len(col_list) != len(new_value_list):
                raise ValueError("科目和成绩数量不匹配")
            
            self.df.loc[self.df['name'] == st_name, col_list] = new_value_list
            return True
        except Exception as e:
            print(f"修改成绩失败: {str(e)}")
            return False

    def delete_student(self, st_name):
        """删除学生信息"""
        ## 修改df行数据是一定要重置索引，避免因索引重复而导致问题。
        #  reset_index(drop=True) 和 .append(df2,ignore_index=True) 分别展示了删除和新增时重置索引的操作。
        try:
            if st_name not in self.df['name'].values:
                raise ValueError(f"找不到学生 {st_name}")
            
            self.df = self.df[self.df['name'] != st_name].reset_index(drop=True)
            return True
        except Exception as e:
            print(f"删除学生失败: {str(e)}")
            return False

    def get_average_scores(self):
        """计算所有学生平均成绩"""
        try:
            score_columns = ['literature', 'history', 'math']
            self.df['average'] = self.df[score_columns].mean(axis=1)
            return self.df[['name', 'average']].copy()
        except Exception as e:
            print(f"计算平均分失败: {str(e)}")
            return None

    def get_highest_scores(self):
        """获取各科目最高分"""
        try:
            score_columns = ['literature', 'history', 'math']
            return self.df[score_columns].max()
        except Exception as e:
            print(f"获取最高分失败: {str(e)}")
            return None

    def display_all(self):
        """显示所有学生信息"""
        print("\n当前所有学生信息：")
        print(self.df)
        
# 主要改进：

# 面向对象设计
# 将所有功能封装在 StudentManager 类中
# 更好的数据封装和管理

# 错误处理
# 添加了异常处理机制
# 增加了输入验证
# 提供了错误提示

# 数据一致性
# 保持 DataFrame 结构的一致性
# 使用 reset_index 维护索引

# 功能增强
# 添加了数据验证
# 增加了显示功能
# 改进了平均分计算方法


# 9. 数据分析项目：
#    - 使用Pandas读取一个真实数据集
#    - 进行数据清洗
#    - 进行基本的统计分析
#    - 创建可视化图表展示结果
