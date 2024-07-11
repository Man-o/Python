'''i=1
while i<=10:
    print(i)
    i+=1
    print('Outer loop excuted')
    j=1
    while j<=10:
        print(j)
        j+=1
        print('Inner loop excuted')'''
print("---------------------------------------------------------")
m=10
while m>0:
    if m==5:
        break
    print(m)
    n=1
    while n<=10:
        print(n)
        n+=1
    m-=1
print("---------------------------------------------------------")
for num in range(105,99,-1):
    print(num)
else:
    print("All iterations are Done")
print("---------------------------------------------------------")
for eve in range(120,100,-1):
    if(eve%2==0):
        print(f"{eve} is Even Number")
else:
    print('Iterations Completed')
print("---------------------------------------------------------")
'''for DBTT in range(1,101):
    if DBTT%2==0:
        if DBTT%2!=DBTT%3:
            print(f"{DBTT} is Divisible by 2")
    if DBTT%3==0:
        if DBTT%2!=DBTT%3:
            print(f"{DBTT} is Divisible by 3")
    if DBTT%2==0 and DBTT%3==0:
        print(f"{DBTT} is Divisible by 2 and 3")
else:
    print('Successfully executed')'''
print("---------------------------------------------------------")
no=1
while no<=50:
    if no%5==0:
        if no==40:
            break
        print(no)
    no+=1
else:
    print("Above elements without 45")
print("---------------------------------------------------------")
for i in range(1,10):
    if i%2==0:
        continue
    print(i)
print("---------------------------------------------------------")
        
    
