class SBI:
    Branch='Marathahalli'
    IFSC='SBI000025'
    def __init__(self,Name,Mno,Aadhar,Pan,Gender):
        self.Name=Name
        self.Mno=Mno
        self.Aadhar=Aadhar
        self.Pan=Pan
        self.Gender=Gender
    def details(self):
        print(f'Name = {self.Name}')
        print(f'Mno = {self.Mno}')
        print(f'Aadhar = {self.Aadhar}')
        print(f'Pan = {self.Pan}')
        print(f'Gender = {self.Gender}')
        print(f'Branch = {self.Branch}')
        print(f'IFSC = {self.IFSC}')
Cus1=SBI('Mano',6383706374,659071631369,'ABCD1234','Male')
Cus2=SBI('Freaky',6378416374,659012341369,'DABC1234','Male')
Cus1.details()
