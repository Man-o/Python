var=6
for r in range(1,var):
    for c in range(1,var):
        if r%2!=0 and r!=var//2:
            if c%2!=0 and c!=var//2:
                print(c,end='')
            else:
                print(' ',end='')
        elif r%2==0:
            if c%2==0:
                 print(c,end='')
            else:
                print(' ',end='')
        elif r==var//2:
            if c==r:
                print(c,end='')
            else:
                print(' ',end='')
    print()

                
                
