__author__ = 'Mars'
import  string

f = open('input.txt', 'r')
strpro = f.read()
setA=''
for i in strpro:
    if i not in setA:
        setA+=i

print  setA
# lol orz
w=[][]
for i in range(1,10):
    for j in range(1,10):
        w[i][j]='*'

for i in range(1,10):
    for j in range(1,10):
        print(w[i][j])
