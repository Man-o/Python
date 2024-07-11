#list_comp

'''s='abcd'
print([ord(asc) for asc in s])'''

'''l='I am Mano'
print([word[0] for word in l.split()])'''

'''l='I am Mano'
print([(word,len(word)) for word in l.split()])'''

'''print([i**2 for i in range(1,11)])'''

'''print([i for i in range(0,11,2)])'''

'''names=['laura','bill','alan','evie']
print([v for v in names if v[0] in 'AEIOUaeiou'])'''

'''lang=['python','C','Java','php','c++']
print([l for l in lang if l[0]=='p'])'''

'''s={'apple','google','yahoo','flipkart','instagram'}
print([i for i in s if len(i)<6])'''

'''print([('even',i) if i%2==0  else ('odd',i) for i in range(0,11)])'''
'''print([(i,'small') if i<5 else (i,'large') for i in range(0,11)])'''
'''num=[-5,-3,1,7,-2,-10,8]
print([0 if i<0 else i for i in num ])'''


'''s=['hello','world','python','js']
print([ s[i].upper() if i%2==0 else s[i].lower() for i in range(len(s))])'''

'''s=['mano','freak','money','food']
print([i  for i in s if len(i)%2==0])'''
'''print([i**2 if i%2==0 else i//i for i in range(1,11)])'''

#set comprehension
'''print({i**3 for i in range(1,6)})'''
'''print({i for i in range(1,6,2)})'''
'''print({i for i in 'dude'})'''
'''print({i.upper() for i in 'mano'})'''
'''sen='this is a test this only a test'.split()
print({sen[i] for i in range(len(sen))})'''
'''print({i for i in range(1,11) if i%3==0 or i%5==0})'''
#dict comprehension
'''d={'abc':44.5,'123':4,'c':56}
print({val:key for key,val in d.items()})'''

'''print({key:key*key for key in range(1,6)})'''

'''det={'Name':'Mano','Age':'21','City':'Banglore'}
print({key:val.upper() for key,val in det.items()})'''

'''d={'a':1,'b':2,'c':3,'d':0}
print({key:val for key,val in d.items() if val<2})'''

'''print({key:key**3 for key in range(1,51) if key%2!=0})'''

'''l=['apple','banana','orange','kiwi','grapes']
print({key:key.capitalize() for key in l if key[0] in 'aeiouAEIOU'})'''

'''p=['rohit','sky','bum','hardik','pant']
print({key:key.upper() if len(key)>3 else key.lower() for key in p})'''

'''print({key:key**2 if key%2==0 else key//2 for key in range(1,51)})'''

'''st_temp={'ka':32,'Tn':38,'Kash':10,'Jammu':15,'Kl':25}
print({key:('cold' if val<15 else 'Warm' if 15<=val<=25 else 'hot') for key,val in st_temp.items()})'''

for i in range





