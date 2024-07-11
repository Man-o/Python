'''def even(num):
    if num%2==0:
        return True  
print(list(filter(even,range(100,201))))'''
'''val='dood'
sind=0
eind=-1
while sind!=len(val)//2:
    if val[sind]!=val[eind]:
        print('Not')
        break
    sind+=1
    eind-=1
else:
    print('palindrome')'''
'''from functools import reduce
print(reduce(lambda e1,e2:e1+e2,[100,200,300,400,500]))'''
'''num=5
for sv in range(num,0,-1):
    for col in range(sv,num+1):
        print(col,end=' ')
    print()'''
'''def armstrong(num,nod):
    if num==0:
        return 0
    return (num%10)**nod+armstrong(num//10,nod)
num=370
print('Armstrong' if armstrong(num,len(str(num)))==num else 'Not')'''
'''num=6383706374
while num!=0:
    rem=num%10
    for i in range(2,rem//2+1):
        if rem%i==0:
            break
    else:
        print(rem)
    num//=10'''
'''num=1234
count=0
while num!=0:
    count+=1
    num//=10
print(count)'''
def D2B(num,power=1):
    if num==0:
        return 0
    return (num%2)*power + D2B(num//2,power*10)
num=14
print(D2B(num))
