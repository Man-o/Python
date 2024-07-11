'''fun=lambda a,b,c:a*b+b*c
print(fun(2,3,4))
val=lambda val1,val2,val3:val1*1+val2*2+val3*3=='122333'
print(val('1','2','3'))
num=lambda n1,n2,n3:n1+n2
print(num(1,2,3))
def sq(val):
    return val*val
print(list(map(sq,[1,2,3,4,5])))
for i in map(sq,[1,2,3]):
    print(i,end=' ')
print()
print(list(map(lambda val:val*val,[5,6,7])))
def prime(num,fcount=0):
    for fa in range(1,num+1):
        if num%fa==0:
            fcount+=1
    return fcount==2
print(list(map(prime,range(1,20))))
print('\n'.join(list(map(lambda st:'* '*st,range(1,6)))))
print('-------------------------------------------------')
print('\n'.join(list(map(lambda st:'* '*st,range(5,0,-1)))))
num=5
print('\n'.join(list(map(lambda sp,st:' '*sp + '*'*st,range(num-1,-1,-1),range(1,num+1)))))
num=5
print('\n'.join(list(map(lambda sp,st:' '*sp+'*'*st,range(0,num),range(num,0,-1)))))
num=4
print('\n'.join(list(map(lambda sp,st:' '*sp+'* '*st,range(num-1,-1,-1),range(1,num*2,2)))))
num=4
print('\n'.join(list(map(lambda sp,st:' '*sp+'*'*st,range(0,num),range(num*2-1,0,-2)))))
print('\n'.join(list(map(lambda n:(str(n)+' ')*n,range(5,0,-1)))))'''
'''num=5
print('\n'.join(list(map(lambda n:(str(num+1-n)+' ')*n,range(1,num+1)))))'''
'''def even(num):
    if num%2!=0:
        return True
print(list(filter(even,range(1,10))))'''
'''def armstrong(num,res=0):
    dup=num
    power=len(str(num))
    while num!=0:
        rem=num%10
        res+=rem**power
        num//=10
    return dup==res
print(list(filter(armstrong,range(1,21))))'''
'''def disarum(num,res=0):
    dup=num
    power=len(str(num))
    while num!=0:
        rem=num%10
        res+=rem**power
        power-=1
        num//=10
    return dup==res
print(list(filter(disarum,range(1,101))))'''
'''print(list(filter(lambda val:val%2==0,[110,111,7,9,8])))'''
'''print(list(filter(lambda val:len(val)%2==0,['Mano','Freaky','Shark','123'])))'''
'''print(list(filter(lambda val:len(val)==len(set(val)),['Mano','Freakyy','aab','bbc'])))'''
'''def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
    return True
print(list(filter(prime,range(1,101))))'''
'''def special(num,res=0):
    for fa in range(1,num//2+1):
        if num%fa==0:
            res+=fa
    return res==num
print(tuple(filter(special,range(1,1000))))'''
l1=[1,2,3,4]
l2=[5,6,7,8]
print(list(map(lambda a,b:a+b,l1,l2)))
from functools import reduce
print(reduce(lambda a,b:a*b,range(1,9)))
print(reduce(lambda a,b:a^b,range(1,5)))
