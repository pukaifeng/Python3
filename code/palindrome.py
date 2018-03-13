#用filter()函数求回数
def is_palindrome(n):  
    return str(n) == str(n)[::-1]  
  
output = filter(is_palindrome, range(1, 100))  
print(list(output))
