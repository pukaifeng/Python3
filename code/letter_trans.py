#用map()函数实现将字符串首字母大写，其他全部小写
def letter_trans(name):
    return name[0].upper()+name[1:].lower()
    
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(letter_trans,L1))
print(L2)
