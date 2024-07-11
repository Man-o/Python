num=5
for lines in range(1,num+1):
    for st in range(lines):
        print('*',end=' ')
    print()
print('=========================================================================')
num=7
spaces=num//2
stars=1
for lines in range(num):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    if lines<num//2:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2
print('=========================================================================')
num=7
spaces=num//2
stars=1
for lines in range(num//2+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    spaces-=1
    stars+=2
    print()
spaces=1
stars=num-2
for lines in range(10//2):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
spaces=0
stars=num
for lines in range(num,0,-2):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    spaces+=1
    stars-=2
    print()
print('=========================================================================')
num=7
stars=1
for lines in range(1,num+1):
    for st in range(stars):
        print('*',end=' ')
    print()
    if lines<=num//2:
        stars+=1
    else:
        stars-=1
print('=========================================================================')
num=7
spaces=num//2
stars=1
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(stars):
        print('*',end=' ')
    print()
    if lines<=num//2:
        spaces-=1
        stars+=1
    else:
        spaces+=1
        stars-=1
print('=========================================================================')
num=5
for lines in range(1,num+1):
    for col in range(lines):
        print(lines,end=' ')
    print()
print('=========================================================================')
num=4
for lines in range(num,0,-1):
    for col in range(lines):
        print(lines,end=' ')
    print()
print('=========================================================================')
num=5
spaces=num-1
for lines in range(1,num+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for col in range(lines):
        print(lines,end=' ')
    print()
    lines+=1
    spaces-=1
print('=========================================================================')
num=5
spaces=0
for lines in range(num,0,-1):
    for sp in range(spaces):
        print(' ',end=' ')
    for col in range(lines):
        print(lines,end=' ')
    spaces+=1
    lines-=1
    print()
print('=========================================================================')
num=5
spaces=num-1
for lines in range(1,num*2,2):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(1,lines+1):
        print('*',end=' ')
    print()
    spaces-=1
print('=========================================================================')
for lines in range(1,6):
    val=1
    for st in range(lines):
        if lines==1 or lines==2 or lines==4:
            print('*',end=' ')
        else:
            print(val,end=' ')
            val+=1
    print()
