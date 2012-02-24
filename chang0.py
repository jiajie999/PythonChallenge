# chang2
__author__ = 'Mars'
que ="map"
#"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
ans = ''
for i in que:
    if ord(i) in range(ord('a'), ord('z')+1):
        if i=='y':
            ans+='a'
        else:
          if i == 'z':
#            print i
            ans+='b'

          else:
            ans += chr(ord(i) + 2)

    else:
        ans += i
#for i in range(ord('a'), ord('z')+1):
#    print chr(i)
#print  ans

text="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
import string

table = string.maketrans( string.ascii_lowercase, string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
print  table
string.translate(text,table)
print text.translate(table)
