'''l1=[1,2,'mano']
l2=[3,4,'freaky']
print(l1+l2)


l=['abc','123','hello','23']
l1=[]
for i in l:
    if i.isdigit():
        l1.append(i)
print(l1)


s=['apple','google','gmail','instagram','flipkart','facebook']
li=[]
for i in s:
    if len(i)%2==0:
       li.append(i)
print(li)


l1=['hi','hello','python','bye']
l2=[]
for ind in range(-1,-(len(l1)+1),-1):
    l2.append(l1[ind][::-1])
print(l2)'''
    
       
'''odd=[]
for i in range(1,51):
    if i%2!=0:
        odd.append(i)
print(odd)'''

'''li=['apple','google','apple','yahoo','google','amazon']
dup=[]
for i in li:
    if li.count(i)>1:
        dup.append(i)
print(dup)

li=[1,2,3,4]
max_num=0
for num in li:
    if max_num<num:
        max_num=num
print(max_num)


a=[3,4,1,7,3,4,1,7,2,12,8,6,9,11]
a.sort()
b=[]
c=[]
for i in a:
    if i%2!=0:
        b.append(i)
    else:
        c.append(i)
print(b+c)'''
'''sen="hello 123 world 567 welcome to 9724 python"
even_add=0
for i in sen:
    if i.isdigit():
        if int(i)%2==0:
            even_add+=int(i)
print(even_add)'''
#26-06-24 DICTIONARY
'''sen='hello world welcome to python programming hi there'
d={}
for word in sen.split():
    if word[0] not in d:
        d[word[0]]=[word]
    else:
        d[word[0]]+=[word]       
print(d)'''

'''d={'a':'hello','b':100,'c':10.9,'d':'world'}
ne_d={}
for st in d.items():
    if type(st[1])==str:
        ne_d[st[0]]=st[1][::-1]
    else:
         ne_d[st[0]]=st[1]
print(ne_d)'''


'''a=input('enter:')
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)'''


'''a=input('Enter:')
d={}
for i in a:
    if a.count(i)>1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
print(d)'''

    
'''num=(1,2,3,4,5,6,7,8,9,10)
even=0
odd=1
d={}
for i in num:
    if i%2==0:
        if even not in d:
            d[0]=[i]
        else:
            d[0]+=[i]
    else:
        if odd not in d:
            d[1]=[i]
        else:
            d[1]+=[i]
print(d)'''     


'''items=['lotus-flower','lilly-flower','cat-animal','sunflower-flower','dog-animal']
d={}
for i in items:
    list_ele = i.split('-')
    if list_ele[1] == 'animal':
        if list_ele[1] not in d:
            d[list_ele[1]]=[list_ele[0]]
        else:
            d[list_ele[1]]+=[list_ele[0]]
    elif list_ele[1]=='flower':
         if list_ele[1] not in d:
            d[list_ele[1]]=[list_ele[0]]
         else:
            d[list_ele[1]]+=[list_ele[0]]   
print(d) '''  




'''files=('apple.txt','yahoo.pdf','gmail.pdf','amazon.pdf','google.txt','facebook.pdf','flipkart.pdf')
d={}
for i in files:
    sp=i.split('.')
    if sp[1]=='txt':
            if sp[1] not in d:
                d[sp[1]]=[sp[0]]
            else:
                d[sp[1]]+=[sp[0]]
    elif sp[1]=='pdf':
            if sp[1] not in d:
                d[sp[1]]=[sp[0]]
            else:
                d[sp[1]]+=[sp[0]]
                
print(d)'''


'''apps=['apple','google','apple','yahoo']
d={}
for i , app in enumerate(apps):
    if app not in d:
        d[app]=[i]
    else:
        d[app]+=[i]
print(d)'''



d={'a':1,'b':3,'c':4.5,'d':False}
d1={}
for i in d.items():
    d1[i[1]]=i[0]
print(d1)
    
    
    
        









        
        
