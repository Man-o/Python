#sort binary ones
'''l=' '
ind=0
for n in range(1,11):
    dup=n
    pos=1
    res=0
    count=0
    while n!=0:
        rem=n%2
        res+=rem*pos
        pos=pos*10
        n=n//2
    while res!=0:
        rem1=res%10
        if rem1==1:
            count+=1
        res=res//10
    if count>=3:
        l+=str(dup)
print(l)'''
    
    


#15 armstrong numbers
'''count=0
res=0
num=1
while count<=15:
    dup=num
    dig=len(str(num))
    total=0
    while num!=0:
        rem=num%10
        total+=rem**dig
        num//=10
    if dup==total:
        res+=num
        count+=1
    num+=1
print(res)'''

#pattern python
'''p=input('enter str:')
space=len(p)-1
for sv in range(-1,-len(p)-1,-1):
    for sp in range(space):
        print(' ',end='')
    for ev in range(-1,sv-1,-1):
        print(p[ev],end='')
    print()
    space-=1'''
    
'''n=5
space=n-1
for ev in range(5,0,-1):
    for sp in range(space):
        print(' ',end=' ')
    for sv in range(n,ev-1,-1):
        print(sv,end=' ')
    space-=1
    print()'''

#pattern
n=int(input('Enter number:'))
spaces=n-1
for r in range(1,n*2,2):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(1,r+1):
      if r==1 and r==n*2-1:
          print('*',end='')
      else:
          if st==1 and st==r:
              print('*',end='')
          else:
              print(' ',end='')
    print()
    spaces-=1

    
    
        
        
        
