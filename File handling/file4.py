'''with open('file4.txt','r+') as fobj:
    print(fobj.write('AB'))'''

'''with open('file4.txt','w+') as fobj1:
    print(fobj1.write('Manoooooooooooo'))'''

'''with open('file4.txt','a+') as fobj2:
    print(fobj2.write('\nFreaky'))'''

with open('47b0a0edad54fb049e816f13587c9837.jpg','rb') as fobj3:
    content=fobj3.read()
with open('copy.jpg','wb') as fobj4:
    fobj4.write(content)

