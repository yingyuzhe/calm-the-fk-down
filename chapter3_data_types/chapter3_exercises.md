# Chapter 3 练习题

## 基础练习

1. 创建一个字典，包含5个学生的姓名和年龄，然后实现以下操作：
   - 添加一个新学生
   - 删除一个学生
   - 修改一个学生的年龄
   - 打印所有学生的姓名

import pandas as pd
import pandas.dataframe as df


2. 给定两个列表 `[1,2,3,4,5]` 和 `[4,5,6,7,8]`，使用集合操作找出：
   - 两个列表中的共同元素
   - 只在第一个列表中出现的元素
   - 两个列表的所有不重复元素

3. 编写代码实现列表的以下操作：
   - 对列表 `[3,1,4,1,5,9,2,6,5,3,5]` 进行排序
   - 删除重复元素
   - 找出最大值和最小值
   - 计算平均值

## NumPy练习

4. 使用NumPy创建以下数组：
   - 一个3x3的随机数组
   - 一个从0到20的等差数列
   - 一个5x5的单位矩阵
   
5. 对一个NumPy数组执行以下操作：
   - 计算所有元素的平均值
   - 找出大于平均值的所有元素
   - 将数组重塑为新形状

## Pandas练习

6. 创建一个包含学生信息的DataFrame：
   - 包含姓名、年龄、成绩三列
   - 计算平均成绩
   - 找出成绩最高的学生
   - 按成绩对学生排序

7. 数据处理实战：
   - 从CSV文件读取数据
   - 处理缺失值
   - 按特定条件筛选数据
   - 创建数据透视表

## 挑战题

8. 创建一个学生成绩管理系统，要求：
   - 使用字典存储学生信息（姓名、多门课程成绩）
   - 支持添加/删除学生
   - 支持修改成绩
   - 计算每个学生的平均成绩
   - 找出每门课程的最高分

9. 数据分析项目：
   - 使用Pandas读取一个真实数据集
   - 进行数据清洗
   - 进行基本的统计分析
   - 创建可视化图表展示结果
