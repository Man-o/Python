#first ten fibonacci sequence
'''pos=10
fv=0
sv=1
for fib in range(pos):
    tv=fv+sv
    print(fv,end=' ')
    fv=sv
    sv=tv'''

#find given position in fibonacci sequence
pos=5
if pos==1 or pos==2:
    print(pos-1)
else:
    fv=0
    sv=1
    for fib in range(5-2):
        tv=fv+sv
        fv=sv
        sv=tv
    print(tv)
