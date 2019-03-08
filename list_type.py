#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 0001 上午 9:58
# @Author  : 窜希辣一库
# @Email   : 258786958@qq.com
# @File    : list_type.py
# @Software: PyCharm
# @descrip : list
if __name__ == '__main__':
    pass
# 异构：任何类型,嵌套：列表里放列表
lt = [10, 'hello', [1, 2], {'key1': 'hello'}]
# 生成方式，可迭代对象生成，
lt = list('hello') == ['h', 'e', 'l', 'l', 'o']
lt = list(range(1, 10)) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 索引与切片 list[n]  list[m,n] 上边缘不包含，从零开始
# 嵌套list[j][i]
# 计算长度
len(list(range(1, 10))) == 9
#支持 list1+list2
list1 = list('hello')
list2 = list(range(1, 3))
list3 = list1 + list2
list4 = list1 * 2
# in
1 in [1, 2, 3] == True
for x in list1:
    print(x, end='/')


