import re
s='aAb0Cdc6K70+/?{)=-!79'
'''print(re.findall('[a]',s))
print(re.findall('[a7]',s))
print(re.findall('[0-9]',s))
print(re.findall('[a-z]',s))
print(re.findall('[A-Z]',s))
print(re.findall('[a-zA-Z]',s))
print(re.findall('[Aa1234]',s))
print(len(re.findall('[a-zA-Z]',s)))'''

v='Mano Freaky'
'''print(re.findall('[aeiou]',v))
print(re.findall('[aeiou][aeiou]',v))
print(re.findall('[a-z][a-z]',v))
print(re.findall('[A-Z][a-z]',v))
print(re.findall('[a-g]',v))
print(re.findall('[a-z][a-z][a-z]',v))
print(re.findall('[A-Z][a-z][a-z]',v))
print(re.findall('[A-Z][a-z][a-z][a-z]',v))
print(re.findall('[A-Za-z]',v))'''


print(re.findall('[1-9]',s))
print(re.findall('[0-9]',s))
print(re.findall('[1-9][0-9]',s))
print(re.findall('[a-zA-Z0-9]',s))
print(re.findall('[^a-zA-Z0-9]',s))
print(re.findall('[+]',s))
print(re.findall('[^+]',s))
print(re.findall('[?]',s))





