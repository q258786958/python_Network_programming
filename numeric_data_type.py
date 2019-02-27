#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 0025 下午 1:20
# @Author  : 窜希辣一库
# @Email   : 258786958@qq.com
# @File    : numeric_data_type.py
# @Software: PyCharm
import math
import random
# decimal 小数模块
from decimal import *
#
if __name__ == '__main__':
    pass
# 随机数
# random.random() 生成n 0<=n<1
random.random() == 0.181818963965693
# 随机端口号
random.randint(1023, 65535)
# 随机IP地址
str(random.randint(1, 255))+'.'+str(random.randint(1, 255))+'.'+str(random.randint(1, 255))+'.'+str(random.randint(1, 255))
# 随机Mac地址
random.choice(['wangxl', 'zhenggy', 'jiangwb', 'xit', 'sangfl'])
# 整数 + - * /  **乘方  etc int()
# pow(乘方)  abs(绝对值)
# // floor 除法 取比得数小的整数-3<-2.5 所以为-3
10/4 == 2.5, -10/4 == -2.5
10//4 == 2, -10//4 == -3
10 % 4 == 2, 10%4.0 == 2.0
pow(2, 5) == 32, 2**5 == 32
abs(-99) == 99
int(math.pi) == 3
min(3, 4, 6, 9) == 3
max(3, 4, 6, 9) == 9
sum((3, 4, 6, 9)) == 22

# 浮点数  round(四舍五入) int(取整数) float()
1.23, 3.14e-10, 4e210, 2.0e+210
round(3.5) == 4, int(3.5) == 3
float(3) == 3.0
# 八进制 oct(求8进制)
0o777
oct(0o777)  == 0o777
# 十六进制  hex(求16进制)
0xEEE
hex(255)
# 二进制  bin(求二进制) 位移 >> <<  位运算 &  |
0b111
bin(0b1110111 >> 1)
bin(0b1001&0b1010)
bin(0b1001|0b1010)
# 复数
3+4j
# 集合
set('ABCD'),
{1, 2, 3, 4}
# 小数
Decimal('1.1')
# 分数 Fracton(1, 3)
# 布尔型 and  or
bool(1), True, False
#True 99 or 100 =99 真就返回了，不用算100
# 99 and 100 = 100 必须算了100才返回
1 or 1, 100 or 1, 0 or 999, 99 or 100, not 0
1<2, 2==2
#False
not 1, 0 or 0, 0 and 0, 2.0!=2.0,2.0!=2
1 == 2 < 3, 1 == 2 and 2 < 3
#三元运算，if后面为真 返回前面的值，if后面为假，返回后面的值
999 if 0 else 666
999 if 1 else 666
True and False
True or False
