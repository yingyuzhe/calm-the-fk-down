#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
简单的待办事项管理器
通过这个程序，您可以添加、查看、完成和删除任务
"""

import json
import os
import sys
from datetime import datetime
from colorama import Fore, Style, init

# 初始化colorama
init(autoreset=True)

# 任务文件路径
TASKS_FILE = "tasks.json"

def clear_screen():
    """清除屏幕"""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks():
    """从文件加载任务"""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"{Fore.RED}任务文件损坏，创建新的任务列表。")
            return []
    return []

def save_tasks(tasks):
    """保存任务到文件"""
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def display_tasks(tasks):
    """显示所有任务"""
    if not tasks:
        print(f"{Fore.YELLOW}没有任务。使用'添加'选项创建新任务。")
        return

    print(f"\n{Fore.CYAN}您的待办事项列表：")
    print(f"{Fore.CYAN}{'ID':^4}|{'状态':^8}|{'创建日期':^20}|{'任务':<50}")
    print(f"{Fore.CYAN}{'-'*4}+{'-'*8}+{'-'*20}+{'-'*50}")
    
    for i, task in enumerate(tasks):
        status = f"{Fore.GREEN}已完成" if task['completed'] else f"{Fore.RED}未完成"
        created_date = task['created_date']
        task_text = task['text']
        print(f"{i+1:^4}|{status:^8}|{created_date:^20}|{task_text:<50}")

def add_task(tasks, task_text):
    """添加新任务"""
    new_task = {
        'text': task_text,
        'completed': False,
        'created_date': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"{Fore.GREEN}任务已添加！")

def complete_task(tasks, task_id):
    """将任务标记为已完成"""
    if 1 <= task_id <= len(tasks):
        tasks[task_id-1]['completed'] = True
        save_tasks(tasks)
        print(f"{Fore.GREEN}任务 {task_id} 已标记为完成！")
    else:
        print(f"{Fore.RED}无效的任务ID！")

def delete_task(tasks, task_id):
    """删除任务"""
    if 1 <= task_id <= len(tasks):
        deleted_task = tasks.pop(task_id-1)
        save_tasks(tasks)
        print(f"{Fore.GREEN}任务 '{deleted_task['text']}' 已删除！")
    else:
        print(f"{Fore.RED}无效的任务ID！")

def show_menu():
    """显示菜单"""
    print(f"\n{Fore.CYAN}===== 待办事项管理器 =====")
    print(f"{Fore.WHITE}1. 查看所有任务")
    print(f"{Fore.WHITE}2. 添加新任务")
    print(f"{Fore.WHITE}3. 完成任务")
    print(f"{Fore.WHITE}4. 删除任务")
    print(f"{Fore.WHITE}0. 退出")
    print(f"{Fore.CYAN}========================")

def main():
    """主函数"""
    tasks = load_tasks()
    
    while True:
        clear_screen()
        show_menu()
        
        choice = input(f"{Fore.YELLOW}请选择操作 (0-4): ")
        
        if choice == '0':
            print(f"{Fore.GREEN}感谢使用！再见！")
            sys.exit(0)
        
        elif choice == '1':
            display_tasks(tasks)
            input("\n按回车键继续...")
        
        elif choice == '2':
            task_text = input(f"{Fore.YELLOW}请输入新任务: ")
            if task_text.strip():
                add_task(tasks, task_text)
            else:
                print(f"{Fore.RED}任务不能为空！")
            input("\n按回车键继续...")
        
        elif choice == '3':
            display_tasks(tasks)
            if tasks:
                try:
                    task_id = int(input(f"{Fore.YELLOW}请输入要完成的任务ID: "))
                    complete_task(tasks, task_id)
                except ValueError:
                    print(f"{Fore.RED}请输入有效的数字！")
            input("\n按回车键继续...")
        
        elif choice == '4':
            display_tasks(tasks)
            if tasks:
                try:
                    task_id = int(input(f"{Fore.YELLOW}请输入要删除的任务ID: "))
                    delete_task(tasks, task_id)
                except ValueError:
                    print(f"{Fore.RED}请输入有效的数字！")
            input("\n按回车键继续...")
        
        else:
            print(f"{Fore.RED}无效的选择！请重试。")
            input("\n按回车键继续...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.GREEN}程序已中断。再见！")
        sys.exit(0) 