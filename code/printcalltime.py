#用装饰器求执行时间

import time
import functools
def printcalltime(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kw):
        start = time.time()
        res = fun(*args, **kw)
        end = time.time()
        print ("%s excute time = %d ms !" %(fun.__name__, (end - start) * 1000))
        return res
    return wrapper

@printcalltime
def test1():
    time.sleep(2)
    print ("函数执行中")
    
test1()
print ("function name is %s" %test1.__name__)
