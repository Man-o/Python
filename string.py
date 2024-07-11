'''val='Mano'
rev=''
for ind in range(-1,-(len(val)+1),-1):
    rev+=val[ind]
print(rev)'''
'''val='Mano'
rev=''
for ch in val:
    rev=ch+rev
print(rev)'''
'''val='DooD'
sind=0
eind=-1
while sind != len(val)//2:
    if val[sind]!=val[eind]:
        print('Not palindrome')
        break
    sind+=1
    eind+=-1
else:
    print('Palindrome')'''
'''val=[8,9,True,'false','Mano']
for i in val:
    if type(i)==str:
        print(i)'''
'''val=[8,9,True,'false','Mano']
n=[]
for i in range(len(val)):
    if i%2==0:
        n+=[val[i]]
print(n)'''
'''val='abc234@'
n=''
for i in val:
    if  i.isdigit():
        n+=i
print(n)'''
'''val='abc234@'
n=''
for i in val:
    if  i.isalpha():
        n+=i
print(n)'''
'''val='hi how are you'
print(val.replace('hi','Heyy'))'''
'''val='hi how are you'
n=''
for i in val.split():
    if i=='how':
        n+='HOW?'+' '
    else:
        n+=i+' '
print(n)'''
'''val='Mano'
n=' '
for i in val:
    if i in 'AEIOUaeiou':
        n+='*'
    else:
        n+=i
print(n)'''
'''val='hello world'
n=' '
for i in val:
    if val.count(i)>1:
        n+='_'
    else:
        n+=i
print(n)'''
'''val='string.py'
ext=val.split('.')
print(ext[1])'''
'''val='Today is my day'
li_val=list(val)
print(li_val)
print(''.join(li_val))'''
'''val='abc234@'
n=''
for i in val:
    if i.isalnum():
        continue
    n+=i
print(n)'''
'''val='hello welcome to python'
print(','.join(val))'''
'''val='Mano'
t=()
for i in val:
    t=t+(ord(i),)
print(t)'''
'''s='sony12India567pvt21ltd'
add=0
for i in s:
    if i.isdigit():
        add+=int(i)
print(add)'''
'''val='Hello welcome to python'
count=0
for i in val:
    if i==' ':
        count+=1
print(val.count(' '))
print(count)'''
'''val='FreaKy'
cap=0
sm=0
for i in val:
    if i.isupper():
        cap+=1
    elif i.islower():
        sm+=1
print(f'Count of upper:{cap},Count of lower:{sm}')'''

'''var='Get p* in python'
res=''
for i in var.split():
    res+=i[::-1]+' '
print(res.strip())'''

'''var='Get p* in python'
print(' '.join(var.split()[::-1]))'''

'''var='Everyone must attend js'
print(var[:len(var)//2])
print(var[len(var)//2:])'''

'''var='Everyone must attend js'
print(var[::2])
res=''
for i in range(len(var)):
    if i%2==0:
        res+=var[i]
print(res)'''

s='Mano'
for sv in range(len(s)):
    for ev in range(sv+1,len(s)+1):
        print(s[sv:ev])
    print()

'''s='MaN_oF @123'
lower=0
upper=0
con=0
vow=0
digit=0
sp_ch=0
for i in s:
    if('a'<=i<='z'):
          lower+=1
          if i in 'aeiou':
              vow+=1
          else:
              con+=1
    elif ('A'<=i<='Z'):
          upper+=1
          if i in 'AEIOU':
              vow+=1
          else:
              con+=1
    elif i in '1234567890':
        digit+=1
    else:
        sp_ch+=1
        

print(f'upper:{upper},lower:{lower},vow:{vow},con:{con},digit:{digit},sp_ch:{sp_ch}')'''
            


        

