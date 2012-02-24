#!/usr/bin/python
# -*- coding: <utf-8> -*-
__author__ = 'Mars'
import urllib, re
num = 98318# set start point 12345

for i in range(1,400):
    url = r"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+str(num)
    data = urllib.urlopen(url).read()
#    p = re.compile('(\d+)')# matching number ; '+' means positive
#    num=p.findall(data)#return a list
#    num=num[0]
    print data
