num=153
digits=len(str(num))
dup=num
total=0
while num!=0:
    rem=num%10
    total=total+rem**digits
    num//=10
if total==dup:
    print("ARMSTRONG NUMBER")
else:
    print("NOT AN ARMSTRONG NUMBER")

