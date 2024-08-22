import re
#--*
s='g ga go goa gooa'
'''print(re.findall('^g',s))
print(re.findall('a$',s))
print(re.findall('go*',s))
print(re.findall('go*a',s))
print(re.findall('g*a',s))'''


#--+
h='heep hp hep ph p h'
'''print(re.findall('he+p',h))
print(re.findall('h+p',h))
print(re.findall('h+',h))
print(re.findall('he+',h))
print(re.findall('e+p',h))
print(re.findall('p+',h))
print(re.findall('hee+',h))'''


#--?
'''print(re.findall('e?p',h))
print(re.findall('h?p',h))
print(re.findall('go?',s))
print(re.findall('o?a',s))'''


#--{}
a='a aab acb accb acccb accccb'
'''print(re.findall('ac{2}',a))
print(re.findall('ac{0}b',a))
print(re.findall('ac{3}b',a))
print(re.findall('ac{1,2}b',a))
print(re.findall('a{1}b',a))
print(re.findall('c{4}',a))'''


#--|
'''print(re.findall('a|b',a))
print(re.findall('ac|b',a))
print(re.findall('c|b',a))'''


#--()
b='a ab abc acb'
'''print(re.findall('(ab)',b))
print(re.findall('(a)(b)',b))'''










