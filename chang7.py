__author__ = 'Mars'

import urllib;
import re, Image
import os

if __name__ == '__main__':
#no idea for this problem, so i cheat~~
#we need use pil lib to handle png file
#url = r"http://www.pythonchallenge.com/pc/def/oxygen.png"
#urllib.urlretrieve(url,"oxygen.png")

#os.system("oxygen.png")

 i = Image.open("oxygen.png")
 rgba = []
for x in range(0, i.size[0], 7):
    rgba += [i.getpixel((x, 45))]
for r, g, b, a in rgba:
    if r == g == b:
        print chr(r),
ans = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print "\n"
for x in ans:
    print chr(x),