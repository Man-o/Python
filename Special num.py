num=6
res=0
for val in range(1,num//2+1):
    if num%val==0:
        res+=val
if num==res:
    print("Special Number")
else:
    print("Not Special Number")
