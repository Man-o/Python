'''num=5
spaces=1
for lines in range(num):
    for sp in range(spaces):
        print(' ', end=' ')
    for st in range(num):
        print('*',end=' ')
    print()
print("==========================================================================")
for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print()
print("==========================================================================")
num=5
for lines in range(1,num+1):
    for val in range(lines):
        print(val,end=' ')
    print()
print("==========================================================================")
num=5
for ev in range(2,num+2):
    for val in range(1,ev):
        print(val,end=' ')
    print()
print("==========================================================================")
num=5
for ev in range(num+1,0,-1):
    for val in range(1,ev):
         print(val,end=' ')
    print()
print("==========================================================================")
num=5
for sv in range(1,num+1):
    for val in range(sv,0,-1):
        print(val,end=' ')
    print()
print("==========================================================================")   
num=5
for sv in range(num,0,-1):
    for val in range(sv,0,-1):
        print(val,end=' ')
    print()
print("==========================================================================")
num=5
spaces=num-1
for ev in range(2,num+2):
    for sp in range(spaces):
        print(' ',end=' ')
    for val in range(1,ev):
        print(val,end=' ')
    print()
    spaces-=1
print("==========================================================================")'''
num=5
spaces=0
for ev in range(num+1,1,-1):
    for sp in range(spaces):
        print(' ',end=' ')
    for val in range(1,ev):
        print(val,end=' ')
    print()
    spaces+=1
print("==========================================================================")
num=5
spaces=0
for sv in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for val in range(sv,num+1):
        print(val,end=' ')
    print()
    spaces+=1
print("==========================================================================")
num=5
spaces=0
for sv in range(num,0,-1):
    for sp in range(spaces):
        print(' ',end=' ')
    for val in range(sv,0,-1):
        print(val,end=' ')
    print()
    spaces+=1
print("==========================================================================")
num=4
spaces=num-1
for ev in range(1,num*2+1,2):
    for sp in range(spaces):
        print(' ',end=' ')
    for val in range(1,ev+1):
        print(val,end=' ')
    print()
    spaces-=1
print("==========================================================================")
num=5
spaces=0
for ev in range(num*2,1,-2):
    for sp in range(spaces):
        print(' ',end=' ')
    for val in range(1,ev):
        print(val,end=' ')
    print()
    spaces+=1








