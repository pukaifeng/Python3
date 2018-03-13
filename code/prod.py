#用reduce()函数实现阶乘
from functools import reduce

def prod(n):
    if n == 0:
        return 1
    return reduce(lambda x,y: x*y,list(range(1,n+1)))

print(prod(5))
