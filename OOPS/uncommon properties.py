#object address
'''class sunday:
    sub='Python'
    time='10.00AM'
    def __init__(self):
        print(self)
std1=sunday()
print(f'Std1:{std1}')
print(std1)
std2=sunday()
print(f'Std2:{std2}')
print(std2)'''

#Accessing uncommon properties
class SBI:
    Branch='Marathahalli'
    IFSC='SBI000025'
    def __init__(self,Name,Mno,Aadhar,Pan,Gender):
        self.Name=Name
        self.Mno=Mno
        self.Aadhar=Aadhar
        self.Pan=Pan
        self.Gender=Gender
Cus1=SBI('Mano',6383706374,659071631369,'ABCD1234','Male')
Cus2=SBI('Freaky',6378416374,659012341369,'DABC1234','Male')
print(Cus1.Name,Cus1.Branch,sep=',')
print(Cus2.Name,Cus2.Mno,sep=',')

#Modifying uncommon properties
Cus2.Mno=1234567890
print(Cus2.Mno)
Cus1.Pan='FPQP1234'
print(Cus1.Pan)

