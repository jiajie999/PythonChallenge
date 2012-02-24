#!/usr/bin/python
# -*- coding: <utf-8> -*-
__author__ = 'Mars'
import  re
f = open('input.txt', 'r')
strpro = f.read()
ans=""
p=re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
for i in p.findall(strpro):
    ans+=i
#你可以用补集来匹配不在区间范围内的字符。其做法是把"^"作为类别的首个字符；其它地方的"^"只会简单匹配 "^"字符本身。例如，[^5] 将匹配除 "5" 之外的任意字符。

print ans


