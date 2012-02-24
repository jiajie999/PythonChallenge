__author__ = 'Mars'
import urllib,re,pickle


url=r'http://www.pythonchallenge.com/pc/def/banner.p'
data = urllib.urlopen(url).read()
data =pickle.loads(data)
line=''
for n in data:
    for m in n:
        line+= m[0]*m[1]
    print line+'\n'
    line=''

