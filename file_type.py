#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/2 0002 上午 9:03
# @Author  : 窜希辣一库
# @Email   : 258786958@qq.com
# @File    : file_type.py
# @Software: PyCharm
# @descrip : file
if __name__ == '__main__':
    pass
import os
myfile = open('myfile.txt ', 'w')
myfile.write('郑广岩会降龙十八掌。\n')
myfile.write('郑广岩很牛逼！\n')
myfile.close()
myfile = open('myfile.txt ', 'r')
# 读一行
print(myfile.readline())
# 读全部
print(myfile.read())
# 迭代器
for line in myfile :
    print(line)
myfile.close()
# getcwd获取当前目录,listdir ,列出本目录下的所有文件
listd = os.listdir(os.getcwd())
print(listd) == ['.git', 'README.md', 'hello.py', 'numeric_data_type.py', 'string_type.py', 'regexp.py', 'list_type.py', 'dict_type.py', 'file_type.py', 'myfile.txt ']
try:


except Exception:
    pass
