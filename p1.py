#check whether a character vowel or consonant
'''var='Mano'
for ch in var:
    if ch in 'AEIOUaeiou':
        print(f'{ch} is vowel')
    elif ch not in 'AEIOUaeiou':
        print(f'{ch} is Consonant')'''
        
#reverese a given number
'''num=int(input('Enter number:'))
stri=''
while num!=0:
    rem=num%10
    stri+=str(rem)
    num//=10
print(int(stri))'''

#Duplicate character from given string
'''var='manoFreakk'
for i in var:
    if var.count(i)>1:
        print(i)'''

#creating matrix
'''mat1=[]
mat2=[]
for M1R in range(1,3):
    M1L=[]
    for M1C in range(1,3):
        M1L.append(int(input('Enter M1val:')))
    mat1.append(M1L)
for M2R in range(1,4):
    M2L=[]
    for M2C in range(1,4):
        M2L.append(int(input('Enter M2val:')))
    mat2.append(M2L)
print(mat1)
print(mat2)'''

'''rows=int(input('Enter rows:'))
cols=int(input('Enter cols:'))
print([[int(input('Enter val:')) for col in range (cols)] for rows in range(rows)])'''

#addition of 2 matrix
'''m1=[[1,2],[2,1]]
m2=[[3,4],[5,6]]
newMat=[]
if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
    for r in range(len(m1)):
        lines=[]
        for c in range(len(m1[0])):
            lines.append(m1[r][c]+m2[r][c])
        newMat.append(lines)
print(newMat)'''

#multiplication of 2 matrix
'''m1=[[1,2],[1,2]]
m2=[[1,2],[1,2]]
if len(m1)==len(m1[0]):
    mprod=[]
    for r in range(len(m1)):
        lines=[]
        for c in range(len(m2[0])):
            ans=0
            for v in range(len(m2)):
                ans+=m1[r][v]*m2[v][c]
            lines.append(ans)
        mprod.append(lines)
    print(mprod)'''

#Linear search
'''l=[1,4,5,6,67]
tar=6
for ind in range(len(l)):
    if l[ind]==tar:
        print(f'{tar} available in index {ind}')
        break
else:
    print(-1)'''

#using function
'''def linear(l,tar):
    for ind in range(len(l)):
        if l[ind]==tar:
            return ind
    return -1
print(linear([1,23,4,5],4))'''

#Binary search
'''l=[1,2,3,66,4,7]
hind=len(l)-1
lind=0
tar=3
while lind<=hind:
    mid=(lind+hind)//2
    if l[mid]<tar:
        lind=mid+1
    elif l[mid]>tar:
        hind=mid-1
    elif l[mid]==tar:
        print(mid)
else:
    print(-1)'''

#using function
'''def binary(l,t):
    h=len(l)-1
    low=0
    while low<=h:
        m=(low+h)//2
        if l[m]<t:
            low=m+1
        elif l[m]>t:
            h=m-1
        elif l[m]==t:
            return m
    return -1

print(binary([1,23,6,8,9],0))'''

#bubble sort
'''l=[-1,2,-3,66,5,3]
for ind1 in range(len(l)-1,0,-1):
    for ind2 in range(ind1):
        if l[ind2]>l[ind2+1]:
            l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
print(l)'''

#selection sort
'''l=[1,-4,5,2,3]
for ind1 in range(len(l)):
    li=ind1
    for ind2 in range(ind1+1,len(l)):
        if l[li]>l[ind2]:
            li=ind2
    l[li],l[ind1]=l[ind1],l[li]
print(l)'''

#quick sort
'''def quick(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left=[val for val in l[1:] if pivot>val]
    right=[val for val in l[1:] if pivot<=val]
    return quick(left)+[pivot]+quick(right)
l=[5,2,3,6,-1,9]
print(quick(l))'''

# 1 to 10 number recursion
'''def n(num):
    if num==11:
        return
    print(num)
    n(num+1)
num=1
n(num)'''

#factorial using recursion
'''def fact(num):
    if num==1 or num==0:
        return 1
    return num*fact(num-1)
print(fact(5))'''

#add all digits using recursion
'''def add_dig(num):
    if num==0:
        return 0
    return (num%10)+add_dig(num//10)
print(add_dig(1234))'''

#armstrong using recursion
'''def armstrong(num,nod):
    if num==0:
        return 0
    return (num%10)**nod + armstrong(num//10,nod)
num=153
if armstrong(num,len(str(num)))==num:
    print(f'{num} is a armstrongnumber')
else:
    print('Not Armstrong')'''

#disarum number
'''def disarum(num,nod):
    if num==0:
        return 0
    return (num%10)**nod + disarum(num//10,nod-1)
num=135
if disarum(num,len(str(num)))==num:
    print('disarum')
else:
    print('Not disarum')'''

#armstrong number without using exponential
'''num=153
dup=num
res=0
dig=len(str(num))
while num!=0:
    rem=num%10
    ans=1
    for i in range(dig):
        ans*=rem
    res+=ans
    num//=10
if dup==res:
    print('armstrong')
else:
    print('Not armstrong')'''

#find the digits without typecasting
'''num=356
count=0
while num!=0:
    rem=num%10
    count+=1
    num//=10
print(count)'''

#strong number using recursion
'''def fact(num):
    if num==0 or num==1:
        return 1
    return num*fact(num-1)

def strong(num):
    if num==0:
        return 0
    return fact(num%10)+strong(num//10)
num=147
print('Strong' if strong(num)==num else 'Not strong')'''

#binaray to integer using recursion
'''def B2D(num,pow=0):
    if num==0:
        return 0
    return (num%10)*(2**pow)+B2D(num//10,pow+1)
print(B2D(1101))'''

#decimal to binary using recursion
'''def D2B(num,pos=1):
    if num==0:
        return 0
    return (num%2)*pos+D2B(num//2,pos*10)
print(D2B(14))'''

#Happy number using recursion
'''def sq(num):
    if  num==0:
        return 0
    return (num%10)**2 + sq(num//10)

def check(num):
    if num<10:
        return num==1 or num==7
    return sq(num)
num=23
print('Happy' if check(num) else 'Not happy')'''

#print numbers -10 to 1 using recursion
'''def rec(num):
    if num==2:
        return num
    print(num)
    rec(num+1)
num=-10
rec(num)'''

#strong number
'''num=145
dup=num
res=0
while num!=0:
    rem=num%10
    fact=1
    for fa in range(1,rem+1):
        fact*=fa
    res+=fact
    num//=10
print('Strong' if dup==res else 'Not strong')'''

#Evil or odeous
'''num=3
count=0
while num!=0:
    rem=num%2
    if rem==1:
        count+=1
    num//=2
print('Evil' if count%2==0 else 'Odeous')'''

#pronic number
'''num=42
i=0
while i*(i+1)<=num:
    if i*(i+1)==num:
        print('Pronic')
        break
    i+=1
else:
    print('Not pronic')'''

#reverse a string
'''n='Mano'
rev=''
for i in range(-1,-(len(n)+1),-1):
    rev+=n[i]
print(rev)

#without using range function
val='Banglore'
rev=''
for ch in val:
    rev=ch+rev
print(rev)'''

#palindrome
'''val1='madam'
val2=val1[::-1]
if val2==val1:
    print('Palindrome')
else:
    print('Not Palindrome')'''

#without using range function
'''val='malayalam'
rev=''
for ch in val:
    rev=ch+rev
print('palindrome' if val==rev else 'Not Palindrome')'''

#two pointer method
'''val='dood'
sind=0
eind=-1
while sind!=len(val)//2:
    if val[sind]!=val[eind]:
        print('Not palindrome')
        break
    sind+=1
    eind-=1
else:
    print('Palindrome')'''

#number of vowels
'''val='Manooo'
count=0
for ch in val:
    if ch in 'AEIOUaeiou':
        count+=1
print(count)'''
    
#Remove duplicates
'''val='Manooo'
ans=''
for ch in val:
    if ch not in ans:
        ans+=ch
print(ans)'''

#Convert lowercase to uppercase without using inbuilt method
'''low='abcd'
upp=''
for ch in low:
    upp+=chr(ord(ch)-32)
print(upp)'''

'''string='ManoO'
con=''
for ch in string:
    if ord(ch)>=97:
        con+=chr(ord(ch)-32)
    else:
        con+=chr(ord(ch)+32)
print(con)'''

#Find the strings in given list
'''l=[66,7+9j,'Mano','abc',False]
for s in l:
    if type(s)==str:
        print(s)'''

#Even index elements
'''l=[66,7+9j,'Mano','abc',False]
nl=[]
for e in range(len(l)):
    if e%2==0:
        nl.append(l[e])
print(nl)'''

#Get all the numbers in given string
'''val='M a n o 0'
count=0
for ch in val:
    if ch.isspace():
        count+=1
print(count)'''

#special characters
'''val='ms5115149@%+gmail'
sp_ch=[]
for ch in val:
    if  not  ch.isalnum():
        sp_ch.append(ch)
print(sp_ch)'''

#without using inbuilt method
'''val='ms5115149@%+!~`]gmail'
sp_ch=[]
for ch in val:
    if ord(ch)<=47 or (ord(ch)>=58 and ord(ch)<=64) or (ord(ch)>=91 and ord(ch)<=96) or (ord(ch)>=123 and ord(ch)<=126):
        sp_ch.append(ch)
print(sp_ch)'''

#prime given range
'''for n in range(1,51):
    for fa in range(2,n//2+1):
        if n==1:
            break
        elif n%fa==0:
            break
    else:
        print(f'{n} is prime')'''
'''num=1
while num!=51:
    for fa in range(2,num//2+1):
        if num%fa==0:
            break
    else:
        print(f'{num} is prime')
    num+=1'''

#replace vowels
'''val='Manooo'
nVal=''
for ch in val:
    if ch in 'AEIOUaeiou':
        nVal+='*'
    else:
        nVal+=ch
print(nVal)'''

#replace underscore substring present in more than ones
'''val='Hello world'
op=''
for ch in val:
    if val.count(ch)>1:
        op+='_'
    else:
        op+=ch
print(op)'''

#Find the extension
'''f=input('Enter file:')
ex= f.split('.')
print(ex[1])'''

'''for i in range(1,6):
    f=input('Enter file:')
    ex= f.split('.')
    print(ex[1])'''

#prime using function
'''def prime(num):
    fcount=0
    for i in range(1,num+1):
        if num%i==0:
            fcount+=1
    if fcount==2:
        return 'Prime'
    else:
        return 'Not prime'
num=1
print(prime(num))'''

#strong number using function
'''def fact(rem,fact=1):
    for fa in range(1,rem+1):
        fact*=fa
    return fact
def strong(num):
    res=0
    while num!=0:
        rem=num%10
        res+=fact(rem)
        num//=10
    return res
num=145
print('Strong' if strong(num)==res else 'Not strong')'''

#alphabet pattern
'''for i in range(5):
    k=0
    for j in range(5):
        print(chr(i+65+k)+' ',end='')
        k+=5
    print()'''

#max_num in list
'''li=[33,34,56,78,1]
max_num=0
for i in range(len(li)):
    if max_num<li[i]:
        max_num=li[i]
print(max_num)'''
        
    
#fascinating number
'''num=192
tot=str(num*1)+str(num*2)+str(num*3)
for i in (1,10):
    if str(i) not in tot:
        print('Not fascinating')
        break
else:
    print('Fascinating')'''

#tech number
'''n=2024
s=str(n)
if n==(int(s[:len(s)//2])+int(s[len(s)//2:]))**2:
    print('tech')
else:
    print('Not tech')'''

#integer to binary
'''num=15
pos=1
bin=0
while num!=0:
    rem=num%2
    bin+=rem*pos
    pos*=10
    num//=2
print(bin)'''

#Reverse a number
'''num=156
st=''
while num!=0:
    rem=num%10
    st+=str(rem)
    num//=10
print(int(st))'''

#special function
'''def prime(num):
    fa=0
    for i in range(1,num+1):
        if num%i==0:
            fa+=1
    return fa==2
print(list(filter(prime,range(1,10))))'''

#add all digits
'''def add(num):
    res=0
    while num!=0:
        rem=num%10
        res+=rem
        num//=10
    return res
print(list(map(add,[123,456,98])))'''

#even length strings
'''print(list(filter(lambda val:len(val)%2==0,['python','css','Html','freak'])))'''

#patterns using map function
'''print('\n'.join(list(map(lambda sp,st:sp*' '+st*'*',range(0,5),range(5,0,-1)))))'''

'''num=4
print('\n'.join(list(map(lambda sp,st:sp*' '+st*'*',range(num-1,-1,-1),range(1,num*2,2)))))'''

'''print('\n'.join(list(map(lambda n:(chr(n+64))*n,range(1,6)))))'''

#polyprime
'''def prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
        return True
def polindrome(num,rev=0):
    dup=num
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return dup==rev
num=11
for num in range(10,21):
    print(f'{num} is polyprime' if prime(num) and polindrome(num) else 'Not')'''
    
#reverse number
'''def reverse(num,rev=0):
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev
print(reverse(5689))'''


#special number
'''def special(num,res=0):
    for i in range(1,num//2+1):
        if num%i==0:
            res+=i
    return res==num
num=7
print('special' if special(num) else 'Not')'''

#sunny number
'''def sunny(num):
    val=0
    while val*val<=num:
        if val*val==num:
            return True
        val+=1
    return False
val=26
print('Sunny' if sunny(num) else 'False')'''

#first 10 polyprime
'''def prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
        return True
def polindrome(num,rev=0):
    dup=num
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return dup==rev
num=0
count=0
while count<10:
    if(polindrome(num) and prime(num)):
        print(num)
        count+=1
    num+=1'''

#first 10 armstrong numbers
'''def armstrong(num,nod):
    res=0
    while num!=0:
        rem=num%10
        res+=rem**nod
        num//=10
    return res
num=0
count=0
while count<=14:
    if armstrong(num,len(str(num)))==num:
        print(num)
        count+=1
    num+=1'''

#convert string to list vice versa
'''var='Mano'
li=list(var)
print(li)
print(' '.join(li))'''

#comma seprator
'''var='hello welcome to python'
print(','.join(var))'''

#upper character using ascii values
'''var='MaNoO'
count=0
for i in var:
    if  ord(i)>64 and ord(i)<91:
        count+=1
print(count)'''

#dictionary programs
'''var='Hii Hello world welcome to python'
d={}
for word in var.split():
    if word[0] not in d:
        d[word[0]]=[word]
    else:
        d[word[0]]+=[word]
print(d)'''

#reverse a dictionary
'''d={'a':'Hello','b':'World','c':780}
nd={}
for item in d.items():
    if type(item[1])==str:
        nd[item[0]]=item[1][::-1]
    else:
        nd[item[0]]=item[1]
print(nd)'''

#occurence of character in dictionary
'''val='Manooo'
d={}
for i in val:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)'''

#grouping odd and even numbers in dictionary
'''var=(1,2,3,4,56,7,89,5)
e_key=0
o_key=1
d={}
for i in var:
    if i%2==0:
        if  e_key not in d:
            d[0]=[i]
        else:
            d[0]+=[i]
    else:
        if  o_key not in d:
            d[1]=[i]
        else:
            d[1]+=[i] 
print(d)'''

#grouping files
'''files=('apple.txt','yahoo.pdf','gmail.pdf','google.txt')
d={}
for item in files:
    items=item.split('.')
    if items[1]=='txt':
        if items[1] not in d:
            d[items[1]]=[items[0]]
        else:
            d[items[1]]+=[items[0]]
    elif items[1]=='pdf':
        if items[1] not in d:
            d[items[1]]=[items[0]]
        else:
            d[items[1]]+=[items[0]]    
print(d)'''

'''d1={'a':20,'b':30}
d2={'c':20,'a':40}
d={}
for i in d1.items():
    if i[0] not in d:
        d[i[0]]=[i[1]]
    else:
        d[i[0]]+=d[i[1]]
for i in d2.items():
    if i[0] not in d:
        d[i[0]]=[i[1]]
    else:
        d[i[0]]+=d[i[1]]
print(d)'''



#all the substring in given string
'''s='hello'
for sv in range(len(s)):
    for ev in range(sv+1,len(s)+1):
        print(s[sv:ev])'''

#consonants
'''s='Mano freaky'
count=0
for i in s:
    if ('A<=i<=Z' or 'a<=i<=z') and i not in 'AEIOUaeiou' and not i.isspace():
        count+=1
print(count)'''

#pramid
'''num=7
spaces=num//3
stars=1
for lines in range(num):
    for sp in range(spaces):
        print('',end='')
    for st in range(stars):
        print('*',end='')
    print()
    if lines<num//2:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2'''
        
        
        
        


            
        



        
        
        



            








    
        




        
        


        
        
        
    
    


    

    
        
    
    
    
    
    
    
                
                       
                       
    



