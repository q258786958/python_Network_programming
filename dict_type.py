#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 0001 下午 1:39
# @Author  : 窜希辣一库
# @Email   : 258786958@qq.com
# @File    : dict_type.py
# @Software: PyCharm
# @descrip : Dictionary
if __name__ == '__main__':
    pass
# 字典元素
dict1 = {'grand': 'wangxl', 'dad': 'zhenggy', 'son':'jiangwb'}
dict1.keys()
dict1.values()
for x, y in dict1.items():
    print('%-8s is %-10s'%(x,y))
# 字典修改
dict1['grand'] = 'aaa'
dict1['baba'] = 'wangxl'
del dict1['baba']
