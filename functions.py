'''def mano(a,b):
    print(a+b)
    return
    print(a-b)
mano(11,1)
mano(41,7)'''
'''def add(a,b,c):
    return a+b+c
print(add(1,2,3))'''
'''def num(a=0,b=0,c=0):
    print(f'a is {a}')
    print(f'b is {b}')
    print(f'c is {c}')
num(2)'''
'''def sample (*mano):
    print(mano)
sample(1,2,3)
sample(4)'''
'''def number(**mano):
    print(mano)
number(a=3,b=4,c=5)'''
'''def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            print("Not prime")
            break
    return 'prime'
print(prime(7))
print('--------------------------------------------------')'''
'''def prime(num):
    fcount=0
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2
var=7
if prime(var):
    print('prime')
else:
    print('Not')'''
'''num=5
def fact(num,fact=1):
    for val in range(1,num+1):
        fact=fact*val
    return fact
print(fact(num))
print('--------------------------------------------------')'''
    
'''num=153
def armstrong(num,power,res=0):
    while num!=0:
        rem=num%10
        res+=rem**power
        num//=10
    return res
print('Armstrong' if armstrong(num,len(str(num)))==num else 'NOT')'''
'''def disarum(var,power,res=0):
    while var!=0:
        rem=var%10
        res+=rem**power
        power-=1
        var//=10
    return res
var=518
print('Disarum' if disarum(var,len(str(var)))==var else 'Not')'''
def fact(num,fact=1):
    for fa in range(1,num+1):
        fact*=fa
    return fact
def strong(num,res=0):
    while num!=0:
        rem=num%10
        res+=fact(rem)
        num//=10
    return res
num=145
print('strong' if strong(num)==num else 'Not')
