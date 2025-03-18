#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
猜数字游戏
这是一个简单的猜数字游戏，计算机会随机生成一个1-100之间的数字，玩家需要猜出这个数字。
"""

# 第一阶段：导入所需的模块
import random  # 用于生成随机数
import time    # 用于添加时间延迟

# 第二阶段：定义游戏的主要函数
def guess_number_game():
    """
    猜数字游戏的主函数
    """
    # 打印游戏欢迎信息
    print("=" * 30)
    print("欢迎来到猜数字游戏！")
    print("=" * 30)
    print("我已经想好了一个1到100之间的数字。")
    print("你能猜出是什么数字吗？")
    print("=" * 30)
    
    # 让游戏有一点悬念
    print("正在生成随机数...", end="")
    for _ in range(3):  
        #表示循环3次（0，1，2），_ 是一个特殊变量名，表示这个循环变量不会在后续代码中使用到。
        time.sleep(0.5)  # 延迟0.5秒
        print(".", end="", flush=True)
        #end="" 表示不换行，因为print函数默认以"\n"换行.
        #flush=True 表示立即刷新输出缓冲区，确保每次打印的字符都能立即显示在屏幕上。
    print("\n")
    
    # 生成1-100之间的随机数
    secret_number = random.randint(1, 100)
    
    # 初始化猜测次数
    attempts = 0
    
    # 开始游戏循环
    while True:  #while True 表示无限循环，直到遇到break语句才会退出循环。
        # 获取玩家的猜测
        try: #try-except 结构用于捕获和处理可能的异常。防止程序崩困。
            guess = int(input("请猜一个1-100之间的数字: "))
            
            # 验证输入是否在有效范围内
            if guess < 1 or guess > 100:
                print("请输入1-100之间的数字！")
                continue  #continue 语句立即结束当前迭代，跳转到循环的开始处
                
        except ValueError: #except 语句用于捕获和处理特定的异常类型。
            print("请输入一个有效的数字！")
            continue
        
        # 增加猜测次数
        attempts += 1
        
        # 检查猜测结果
        if guess < secret_number:
            print(f"猜小了！再试一次。")
            #f表示这是一个格式化字符串，也称为"f-string"。
            #f前缀允许您在字符串中直接嵌入Python表达式，格式为{表达式}。
        elif guess > secret_number:
            print(f"猜大了！再试一次。")
        else:
            print(f"\n恭喜你！你猜对了！")
            print(f"正确答案是: {secret_number}")
            #f后面的 {secret_number} 表示将 secret_number 变量的值插入到字符串中。
            print(f"你总共猜了 {attempts} 次。")
            break  #break 语句。至此无限循环结束。
    
    # while true 结束后，根据猜测次数给出评价
    if attempts <= 3:
        print("太厉害了！你是猜数字大师！")
    elif attempts <= 6:
        print("不错！你有很好的猜测能力！")
    elif attempts <= 10:
        print("还行，继续练习可以做得更好！")
    else:
        print("加油，下次争取更少的次数猜对！")
    
    # 询问是否再玩一次
    play_again = input("\n要再玩一次吗？(y/n): ").lower()
    #lower() 方法将字符串转换为小写。
    if play_again == 'y' or play_again == 'yes':
        guess_number_game()  # 递归调用，再玩一次
    else:
        print("谢谢参与！下次再见！")

# 第三阶段：程序入口点
if __name__ == "__main__":
    guess_number_game()  # 启动游戏 
#__name__ 是Python的一个特殊变量
#当脚本被直接运行时，__name__ 的值为 "__main__"
#当脚本被导入为模块时，__name__ 的值为模块的名称（例如 "guess_number"）
#上述语句的含义是，只有当脚本被直接运行时，才执行 guess_number_game() 函数

# 在另一个文件中
import guess_number

# 只使用游戏中的某些函数，而不启动整个游戏
guess_number.display_tasks(my_tasks)