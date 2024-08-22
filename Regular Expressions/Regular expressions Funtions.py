import re
a='saturday sunday'

'''print(re.match('sat',a))
print(re.match('at',a))
print(re.search('r',a))
print(re.findall('a',a))
print(re.findall('k',a))
print(re.split('a',a))
print(re.split('a',a,1))
print(re.sub('a','z',a))
print(re.sub('a','z',a,2))
print(re.subn('a','z',a))'''

print(re.findall('.',a))
print(re.findall('^s',a))
print(re.findall('y$',a))


