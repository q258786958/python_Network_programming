#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 0027 下午 3:31
# @Author  : 窜希辣一库
# @Email   : 258786958@qq.com
# @File    : regexp.py
# @Software: PyCharm
# @descrip : 正则表达式
if __name__ == '__main__':
    pass
import re
# 转意符
# \r回车
# \n newline
# \t tab
# |\\ '\'|  |\^  '^'|   |\$ '$'|  |\. '.'|
re.match('cmd\.exe', 'cmd.exe') == 'match'
re.match('cmd.exe', 'cmdaexe') == 'match'
re.match('cmd\.exe', 'cmdaexe') == 'no match'
# 多种字符
# |\d 任意一个数字 0~9
# |\w 任意一个字母或数字  A~Z a~z 0~9
# \s 任意一个空格 \r \n \t
# | .  任意一个 除\n
re.match('.*', 'oehod12324') == "match='oehod12324'"
re.match('\d\d\d', '123') == "match='123'"
# 如果后面字符长，照样可以匹配，短了则不行
re.match('\d\d\w', '12a') == "match='12a'"
re.match('\d\d\w', '12aa')== "match='12a'"
re.match('\s', '\r\n') == "match='\r'"
temp = '  \n\t\r'
re.match('\s+', temp) == "'  \n\t\r'"
# 匹配次数
# |{n} 重复n次
# |{m,n}重复m~n
# |{m,}至少m次
# |?{0,1}0或一次
# | +{1,}至少1次
# |*{0,}，任意次
ipadd = '192.168.200.101'
macadd = '00-21-9B-11-EA-E2'
# ip地址的正则 ((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))
# mac地址的正则 /(([a-f0-9]{2}:)|([a-f0-9]{2}-)){5}[a-f0-9]{2}/gi
re.match('((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))', ipadd) == 'match'
re.match('/(([a-f0-9]{2}:)|([a-f0-9]{2}-)){5}[a-f0-9]{2}/gi', macadd)
# [@#c] 表示一位，@,#,c选其一
# [^abc] 除a，b，c的一位
# [^a-f0-5] 除去a~f,0~5的一位
re.match('[^a-f0-5]','z') == "match='z'"
re.match('[^a-f0-5]','6') == "match='6'"
re.match('[^a-f0-5]','a') == "no match"
# 抽象意义的字符
# ^ 字符段的开头
# $ 字符段的结束
# () 中的内容看做一个整体
# | 表示'或'的意思
re.match('ba(na)?$', 'ba')
re.match('ba(na)?$', 'bana')
re.match('root|ROOT', 'root')
re.match('root|ROOT', 'ROOT')
# re替换与分割
re.sub('-', '|', 'a-b-c') == 'a|b|c'
re.split('-|=', 'a-b=c') == ['a', 'b', 'c']
# re分组 groups
str = 'wangxl/zheng/jiangwb'
re.match('(\w+)/(\w+)/(\w+)', str).groups() == ('wangxl', 'zheng', 'jiangwb')
str = 'hello python world!'
str.split() == ['hello', 'python', 'world!']
re.match('(\w+)\s+(\w+)\s+(\w+)!', str).groups()  == ('hello', 'python', 'world')
# re.findall() 针对反复出现的有规律的字符串,search 找到第一个返回
str = '<html><head><head><body><body><html>'
re.findall('<(\w+)>', str) == ['html', 'head', 'head', 'body', 'body', 'html']
re.search('<(\w+)>', str) == "match='<html>'"
