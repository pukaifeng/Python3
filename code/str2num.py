#用map()和reduce()实现字符串转数字

from functools import reduce
def add(x,y):
    return x*10+y

print(reduce(add,[1,3,5,7,9]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2num(s):
    def fn(x,y):
        return x*10+y
    def char2nub(s):
        return DIGITS[s]
    return reduce(fn,map(char2nub,s))

print(str2num('123456789'))
