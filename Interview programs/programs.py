#sort binary ones
'''l=[]
for n in range(1,11):
    dup=n
    pos=1
    res=0
    count=0
    while dup!=0:
        rem=n%2
        res+=rem*pos
        pos=pos*10
        n=n//2
    while res!=0:
        rem1=res%10
        if rem1==1:
            count+=1
        res=res//10
    if count>=0:
        l.append(dup)
print(l)'''
    
    
#15 armstrong numbers
'''count=0
armstrong=[]
num=0
while count<15:
    dup=num
    dig=len(str(num))
    total=0
    while dup!=0:
        rem=dup%10
        total+=rem**dig
        dup//=10
    if num==total:
        armstrong.append(num)
        count+=1
    num+=1
print(armstrong)'''

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
    
#hallow pattern
num=int(input('Enter the number:'))
spaces=num-1
for r in range(1,num+1):
    for sp in range(spaces):
        print(' ',end='')
    for st in range(1,r*2):
        if r==1 or r==num:
            print('*',end='')
        else:
            if st==1 or st==r*2-1:
                print('*',end='')
            else:
                print(' ',end='')
    print()
    spaces-=1

#swap elements
'''a=5
b=6'''
'''if a>b or a<b or a==b:
    a,b=b,a
    print(f'a is {a} b is {b}')'''
'''temp=a
a=b
b=temp
print(a,b)'''

#dictionary
'''d1={'a':20,'b':30}
d2={'c':20,'a':40}
d3={}
for i in d1.items():
    if i[0] not in d3:
        d3[i[0]]=[i[1]]
    else:
        d3[i[0]]+=[i[1]]
for i in d2.items():
    if i[0] not in d3:
        d3[i[0]]=[i[1]]
    else:
        d3[i[0]]+=[i[1]]
print(d3)'''

#score of word
'''name=input('Enter word:').upper()
score=0
for i in name:
    score+=ord(i)-64
print(score)'''
