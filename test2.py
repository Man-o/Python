
'''l=[3,4,23,22,54,55,89]
a=0
for i in l:
    if i%2==0:
        #print(i)
        a+=i
print(i)'''

'''n=6
for i in range(2,n//2+1):
    if n%i==0:
        print('Not prime')
        break
else:
    print('Prime')'''

'''s='hello'
d={}
for i in s:
    if i not in d:
        d[i]=ord(i)
print(d)'''

'''l=['hi','hello',10,'12.3',12,90,6.2]
li=[]
for i in l:
    if type(i)==int:
        print(i)'''

'''s='MaNo'
n_s=''
#print(s.lower())
for i in s:
    if i.isupper():
        n_s+=chr(ord(i)+32)
    else:
        n_s+=i
print(n_s)''' 

'''t=('malayalam','hello','hai','dood')
sind=0
eind=-1
for i in t:
    if i[::-1]==i:
        print(f'{i} is  palindrome')
    else:
        print(f'{i} is not palindrome')'''
    
'''while sind<=len(i)//2:
        if sind[i]!=eind[i]:
            print(f'{i} is not palindrome')
            break
        sind+=1
        eind-=1
    else:
        print(f'{i} is palindrome')'''

'''l=[1,2,3,4]
add=0
for i in l:
    add+=i
avg=add/len(l)
print(avg)'''

'''s='helloworld'
d={}
for i in s:
    if i not in d:
        d[i]=i.count(i)
    else:
        d[i]+=1
print(d)'''

'''dc=[(86,'china'),(91,'india'),(1,'US')]
d={}
for i in dc:
    if i not in d:
        d[i[1]]=i[0]
print(d)'''

'''l=[45,23,78,100,56]
max_sco=0
for i in l:
    if i>max_sco:
        max_sco=i
print(max_sco)'''

'''s='m@no$*'
for i in s:
    if i.isalnum():
        continue
    else:
        print(i)'''


a='mano'
for i in a:
    if i not in 'aeiouAEIOU':
        print(i)
    


    
        
        
