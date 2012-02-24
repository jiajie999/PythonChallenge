__author__ = 'Mars'
import  re,os
import zipfile, re# must use zipfile to get comments~~~~~suck problem
findnothing = re.compile(r"Next nothing is (\d+)").match
comments = []
z = zipfile.ZipFile("channel.zip", "r")
seed = "90052"
while True:
    fname = seed + ".txt"
    comments.append(z.getinfo(fname).comment)
    guts = z.read(fname)
    m = findnothing(guts)
    if m:
        seed = m.group(1)
    else:
        break
print "".join(comments)

#nextn = 90052
#ans=""
#for i in range(10,99907):
# if os.path.exists('channel/' + str(i) + '.txt'):
##     print(i)
#     f=open('channel/' + str(i) + '.txt', 'r')
#     ans+=f.read()+'\n'
#
#print ans
#f=open('ans.txt','w')
#f.write(ans)
    #while True:
#    f = open('channel/' + str(nextn) + '.txt', 'r')
#    nextn = f.read()
#    p = re.compile('(\d+)')
#    ans+=nextn+'\n'
#
##    if p.findall(nextn) ==[]:
##        print f.read()
##    else:
#    nextn = p.findall(nextn)[0]
#
#
#    print nextn
#    print  ans
