with open('file5.txt','r') as fobj:
    words=0
    for lines in fobj:
        lines=lines.strip('\n')
        words=lines.split()
        if words.startswith('M'):
            words+=1
    print(words)
   
