#用filter()函数求素数
def _not_divisible(n):
    return lambda x: x % n > 0

def primes(num):
    L = []
    def _odd_iter():
        n = 2
        while n < num:
            yield n
            n = n + 1            
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        L.append(n)
        it = filter(_not_divisible(n), it)
    return L

L = list(primes(100))
print(L)
