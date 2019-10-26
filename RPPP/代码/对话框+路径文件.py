# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:58:50 2019

@author: Administrator
"""
from tkinter import *
from tkinter import ttk
# 导入filedialog
from tkinter import filedialog
class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        # 创建7个按钮，并为之绑定事件处理函数
        ttk.Button(self.master, text='选择要输入数据的文件夹',
        command=self.open_dir # 绑定open_dir方法
        ).pack(side=LEFT, ipadx=5, ipady=5, padx= 10)

    def open_dir(self):
        # 调用askdirectory方法打开目录
        path = filedialog.askdirectory(title='打开目录',
            initialdir='g:/')
        print(path) # 初始目录

root = Tk()
root.title("选择要输入数据的文件夹")
App(root)
root.mainloop()

#选择要所有输入数据的文件夹
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

path = filedialog.askdirectory()


  

