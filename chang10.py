__author__ = 'Mars'

num = [1, 11, 21, 1211, 111221,3121211]

s = str(num[3])


def change(s, length):
    if length == 1:
        return  s

    if length > 1:
        s = change(s[len(s) / 2:len(s)], len(s[len(s) / 2:len(s)])) + change(s[0:len(s) / 2], len(s[0:len(s) / 2]))
    #        s=s[len(s)/2:len(s)]+s[0:len(s)/2]
    return s


def meg(s1, s2):
    s1 = change(s1, len(s1))
    print(s1)
    s2 = change(s2, len(s2))
    print(s2)
    return s2[0:len(s2) / 2] + s1[0:len(s1) / 2] + s1[len(s1) / 2:len(s1)] + s2[len(s2) / 2:len(s2)]

#(meg('11','21'))#not right~~~

a={'11':'21','1':'11','2':'12'}
ans=''
for y in "1211":
    if y in a.keys():
        ans+=a[y]

import itertools

def look_and_say (length):
    table = {
        ("1", "1", "1"): "31",
        ("1", "1"): "21",
        ("1", ): "11",
        ("2", "2", "2"): "32",
        ("2", "2"): "22",
        ("2", ): "12",
        ("3", "3", "3"): "33",
        ("3", "3"): "23",
        ("3", ): "13"
    }

    prec, result = "1", [1]

    for i in xrange(length - 1):
        prec = "".join(table[tuple(l)] for e, l in itertools.groupby(prec))
        print(prec)
        result.append(int(prec))

    return result

print len(str(look_and_say(31)[30]))