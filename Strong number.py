num=145
res=0
dup=num
while num!=0:
    rem=num%10
    fact=1
    for fa in range(1,rem+1):
        fact*=fa
    res+=fact
    num//=10
if dup==res:
    print("Strong Number")
else:
    print("Not Strong Number")
