#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 0027 上午 8:30
# @Author  : 窜希辣一库
# @Email   : 258786958@qq.com
# @File    : string_type.py
# @Software: PyCharm


if __name__ == '__main__':
    pass
myname = 'wang xing lu'

# 引号
'xi"an',  "xi'an", r'C:\Program Files\Tencent', '''一篇文章''', b'wangxl'
print('-'*80), print(('|' + ' '*78 + '|')), print(('|' + ' '*78 + '|')), print('-'*80)
# 索引与切片 myname[i: j] i从0开始，j从-1开始，上边缘j不包含。
'wang' in  myname, myname[0] == 'w', myname[-1] == 'u', myname[1: 6] == 'ang x', myname[:], myname[2:]
# 转义字符\ linux换行\n windows换行\n\r Tab \t 引号 \'    newline
'a\na\ta\ra'
# 字符串方法
newname = myname.replace('lu', 'gou')
newname == 'wang xing gou'
where = myname.find('x')
where == 5
myname_u = myname.upper()
myname_u == 'WANG XING LU'
print(myname_u.lower())
# 字符串不可变
s = '\n\twang xing lu\n\t'
s.strip() == 'wang xing lu', s.lstrip() == 'wang xing lu\n\t', s.rstrip() == '\n\twang xing lu'
mynamelist = list(myname)
mynamelist == ['w', 'a', 'n', 'g', ' ', 'x', 'i', 'n', 'g', ' ', 'l', 'u']
mynamelist[0] = 'W', ''.join(mynamelist) == 'Wang xing lu'
# 字符串格式化 浮点%f 整数%d 字符串%s
age = 34
name = 'wang xing lu'
print("my name is %s I'm %d years old." % (name, age))
x = 'A'
# |正常显示|左对齐|右对齐|用0补全右面|
res = '|%s|%10s|%-10s|%010s|'%(x, x, x, x)
res == '|A|         A|A         |         A|'
x = 1.23456789
# -6表示有六个宽度，08有8个宽度，包括+号六个宽度，.2f   .3f 表示小数点后几位
# 负号是右对齐
res = '|%-6.2f|%08.3f|%+006.1f|' %(x, x, x)
res == '|1.23  |0001.235|+001.2|'
# 右对齐打印
print('%-10s1\n%-10s2\n%-10s3'%('wangxl', 'zhenggy', 'jiangwb'))
# format方法
'{0}, {1} and {2}.'.format('wangxl', 'zhenggy', 'jiangwb') == 'wangxl, zhenggy and jiangwb.'
temp = '{0[key1]},{1[key2]},{2[key3]}'.format({'key1': 'wangxl'}, {'key2':'zhenggy'}, {'key3': 'jiangwb'})
temp == 'wangxl,zhenggy,jiangwb'
# |左对齐|右对齐|中间对齐|
temp = '|{key1:>10}|{key2:<10}|{key3:^10}|'.format(key1='wangxl', key2='zhenggy', key3='jiangwb')
temp == '|    wangxl|zhenggy   | jiangwb  |'
x = 1.23456789
temp = '|{0:<6.2f}|{1:08.3f}|{2:+06.1f}|'.format(x, x, x)
temp == '|1.23  |0001.235|+001.2|'
import sys
temp = '{0.platform:>10} = {1}'.format(sys,'laptop')
temp == 'linux = laptop'
