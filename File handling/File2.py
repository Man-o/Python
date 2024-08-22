#write
'''fobj=open('file2.txt','w')
print(fobj.write('Mano\nFreaky'))
fobj.close()'''

#writelines
#list
'''fobj2=open('file2.txt','w')
print(fobj2.writelines(['abc\n','cde\n']))
fobj2.close()'''

#dictionary
'''fobj3=open('file2.txt','w')
print(fobj3.writelines({'Abc\n':8,'Cde\n':7}))
fobj3.close()'''

#Append access mode
'''fobj4=open('file2.txt','a')
print(fobj4.readable(),fobj4.writable())
print(fobj4.write('Freakyyyy'))
fobj4.close()'''

#Exclusive access mode
'''fobj5=open('file3.txt','x')
print(fobj5.write('Mano'))
fobj5.close()'''




