s=' I will get the job '
m=s.replace('will','')
for ch in m:
    print(ch)
print('----------------------------------------------')
l=['Mano',45,True,[2,6],(44,66)]
i=l.index([2,6])
for n in range(i,7):
    print(n)
print(n)
print('----------------------------------------------')
t=(45,True,[2,6],(44,66))
for ele in t:
    print(ele)
print('----------------------------------------------')
s={'mano',45,True,0,1,False}
for ele in s:
    print(ele)
print(ele)
print('----------------------------------------------')
d={'a':'mano','b':True,'c':45,'a':'freaky'}
for key in d:
    print(key)
print('----------------------------------------------')
d={'a':'mano','b':True,'c':45,'a':'freaky'}
for val in d.values():
    print(val)
print('----------------------------------------------')
d={'a':'mano','b':True,'c':45,'a':'freaky'}
for items in d.items():
    print(items)
print('----------------------------------------------')
me='Developer'
for ind in range(0,9):
    print(me[ind])
print('----------------------------------------------')
me='Developer'
for ind in range(0,9,2):
    print(me[ind])
print('----------------------------------------------')
for ind in range(0,9,2):
    print(ind)
print('----------------------------------------------')
me='Developer'
for ind in range(-1,-10,-1):
    print(me[ind])
print('----------------------------------------------')
me='Freaky'
for i in range(0,6):
    print(me[i])
    for j in range(i+1,6):
        print(me[j])
print('----------------------------------------------')
num=1
while(num<=10):
    print(num)
    num+=1
print('----------------------------------------------')
mName="Developers"
i=0
while i!=10:
    print(mName[i])
    i+=1
print('----------------------------------------------')
count=0
while True:
    count+=1
    print(f"Count is {count}") 
    if count==10:
        break
