for st in range(1,6):
    print('*',end=' ')
print()
print('================================================================================')
for lines in range(1,6):
    for st in range(1,6):
        print('*',end=' ')
    print()
print('================================================================================')
for lines in range(1,6):
    for st in range(lines):
        print('*',end=' ')
    print()
print('================================================================================')
num=5
spaces=num-1
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(lines):
        print('*',end=' ')
    spaces=spaces-1
    print()
print('================================================================================')
for lines in range(5,0,-1):
    for st in range(lines):
        print('*',end=' ')
    print()
print('================================================================================')
for i in range(1,6):
    print('* '*i)
print('================================================================================')
num=5
spaces=0
for lines in range(num,0,-1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(lines):
        print('*',end=' ')
    spaces=spaces+1
    print()
print('================================================================================')
num=5
spaces=num-1
for lines in range(1,num*2,2):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range (lines):
        print('*',end=' ')
    spaces=spaces-1
    print()
print('================================================================================')
num=9
spaces=0
for lines in range(num,0,-2):
    for sp in range(spaces):
        print(' ', end=' ')
    for st in range(lines):
        print('*',end=' ')
    spaces=spaces+1
    print()
print('================================================================================')
for lines in range(1,6):
    for num in range(lines):
        print(num+1,end=' ')
    print()
print('================================================================================')    
num=9
spaces=0
for lines in range(num,0,-2):
    for sp in range(spaces):
        print(' ', end=' ')
    for st in range(lines):
        print(st+1,end=' ')
    spaces=spaces+1
    print()
