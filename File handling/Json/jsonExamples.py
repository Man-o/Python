import json
#dumps
'''c={'RCB':0,'MI':5,'KKR':3}
with open('file.json','w') as fobj:
    content=json.dumps(c,indent=3)
    print(fobj.write(content))'''

#dump
'''c={'RCB':0,'MI':5,'KKR':3}
with open('file1.json','w') as fobj1:
    content=json.dump(c,fobj1)
    print(content)'''

#loads
'''with open('file1.json','r') as fobj2:
    data=fobj2.read()
    print(json.loads(data))'''
#load
'''with open('file1.json','r') as fobj3:
    print(json.load(fobj3))'''

