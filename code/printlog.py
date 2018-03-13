#用装饰器打印日志

import functools
def printlog(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("begin call")
            res = func(*args, **kw)
            print("end call")
            return res
        return wrapper
    return decorator
    
@printlog("aaa")
def test2():
    print ("函数执行中")

test2()
print ("function name is %s" %test2.__name__)
