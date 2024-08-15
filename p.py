'''def even(num):
    if num%2==0:
        return num  
print(list(filter(even,range(100,201))))'''

'''num=140
max=0
while num!=0:
    rem=num%10
    if rem>max:
        max=rem
    num//=10
print(max)'''

'''54321
    5432
     543
      54
       5'''
num=5
space=0
for ev in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for sv in range(num,ev-1,-1):
        print(sv,end=' ')
    print()
    space+=1

print('still Im Worthy')
   


    


