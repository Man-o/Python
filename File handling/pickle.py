import pickle
d={'a':1,'b':2,'c':3}
with open('dict.pkl','wb') as fobj:
    content=pickle.dumps(d)
    print(fobj.write(content))
