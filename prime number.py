a=19
for p in range(2,a//2+1):
    if a%p==0:
        print("Not prime")
        break
else:
    print("Prime")
print('=====================================================================')
b=18
sq=int(b**(1/2))
for p in range(2,sq+1):
     if b%p==0:
        print("Not prime")
        break
else:
    print("Prime")   
print('=====================================================================')
num=int(input("Enter the number:"))
count=0
for fact in range(1,num+1):
    if num%fact==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("Not prime")
print('=====================================================================')

