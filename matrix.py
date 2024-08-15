#creat matrix
'''rows=int(input('Enter rows:'))
cols=int(input('Enter cols:'))
mat=[]
for row in range(rows):
    line=[]
    for col in range(cols):
        line.append(int(input('enter value:')))
    mat.append(line)
print(mat)'''

#using list comprehension
'''print([[int(input('Enter values:'))for c in range(cols)]for r in range(rows)])'''

#add 2 matrixes
'''m1=[[1, 2], [3, 4]]
m2=[[5, 6], [7, 8]]
newMat=[]
if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
    for r in range(len(m1)):
        line=[]
        for c in range(len(m1[0])):
            line.append(m1[r][c]+m2[r][c])
        newMat.append(line)
print(newMat)'''

#multiply 2 matrixes
'''m1=[[1, 2], [3, 4]]
m2=[[5, 6], [7, 8]]
if len(m1[0])==len(m2):
    mprod=[]
    for r in range(len(m1)):
        line=[]
        for c in range(len(m2[0])):
            ans=0
            for v in range (len(m2)):
                ans+=m1[r][v]*m2[v][c]
            line.append(ans)
        mprod.append(line)
    print(mprod)
else:
    ('Multiplication not possible')
print(len(m2))'''

    



