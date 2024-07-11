num=89
dup=num
res=0
digits=len(str(num))
while num!=0:
    rem=num%10
    res+=rem**digits
    digits-=1
    num//=10
if dup==res:
    print("Disarum")
else:
    print("Not Disarum")
    
