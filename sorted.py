#string sorted
'''stmt='Defently I got the Job'
print(sorted(stmt))
print(sorted(stmt,reverse=True))'''


#List sorted
'''li=['Defently','I','got','the','Job']
print(sorted(li,key=len))
print(sorted(li,key=len,reverse=True))'''

'''def lc(n):
    return n[-1]
print(sorted(li,key=lc))'''

'''lc=lambda li:li[-1]
print(sorted(li,key=lc))'''

'''temp=[('bl',45),('Tn',36),('kash',15),('Ap',47)]
print(sorted(temp,key=lambda temp:temp[0][-1],reverse=True))'''


#Tuple sorted
'''num=([2,7],[7,3],[3,8],[8,7],[9,7],[4,9])
print(sorted(num,key=lambda num:num[0]))
print(sorted(num,key=lambda num:num[1]))'''


#Dictionary sorted
'''temps={'bl':45,'Tn':36,'kash':15,'Ap':47}
print(dict(sorted(temps.items())))
print(dict(sorted(temps.items(),key=lambda temps: temps[-1])))'''
temps={'bl':45,'Tn':36,'kash':15,'Ap':47}
def l(t):
    return len(t[0])
print(sorted(temps.items(),key=l,reverse=True))


