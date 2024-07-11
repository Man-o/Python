num=167
res=str(num*1)+str(num*2)+str(num*3)
for val  in range(1,10):
    if str(val) not in res:
        print("Not fascinating")
        break
else:
    print("Fascinating Number")
