#fibonacci pattern
'''a=0
b=1
c=0
for r in range(1,6):
    for c in range(1,r+1):
        c=a+b
        print(a,end=' ')
        a=b
        b=c
    print()'''

#even number pattern
'''a=2
for r in range(1,6):
    for c in range(1,r+1):
        print(a,end=' ')
        a+=2
    print()'''

#pattern
'''for r in range(1,6):
    for c in range(1,6):
        if c<=r:
            print(r,end='')
        else:
            print('*',end='')
    print()'''

'''n=5
for r in range(n,0,-1):
    for c in range(1,6):
        if r>=c:
            print(r,end='')
        else:
            print('*',end='')
    print()'''

'''n=5
st=0
for r in range(1,n+1):
    for c in range(1,n+1):
       print(c,end='')
    for s in range(st):
        print('*',end='')
    st+=1
    n-=1
    print()'''

'''n=5
for r in range(1,n+1):
    for c in range(n,0,-1):
        if r<c:
            print('*',end='')
        else:
            print(c,end='')
    print()'''

'''n=5
for r in range(n,0,-1):
    for c in range(n,0,-1):
        if c>r:
            print('*',end='')
        else:
            print(c,end='')
    print()'''

'''n=5
for r in range(n):
    for c in range(n):
        if r>=c:
            print(chr(c+65),end='')
        else:
            print('*',end='')
    print()'''

'''n=5
for r in range(n):
    for c in range(n):
        if r>=c:
            print(chr(r+65),end='')
        else:
            print('*',end='')
    print()'''
    
        

