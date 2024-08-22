'''class parent:
    a=9
    b=10
class child1(parent):
    b=6
    c=1
class child2(parent):
    d=7
    c=1
obj=child2()
print(obj.a)
obj2=child1()
print(obj2.b)'''

class SBI:
    def __init__(self,Name,Balance):
        self.Name=Name
        self.Balance=Balance
    def withdraw(self):
        amount=int(input('Withdraw amount:'))
        if amount>self.Balance:
            print('Insufficient Balance')
        else:
            print(f'{amount} debited successfully.Available balance is {self.Balance-amount}')
class gpay(SBI):
    pass
class phonepay(SBI):
    pass
'''user1=gpay('abc',30000)
user1.withdraw()'''
user2=phonepay('xyz',4000)
user2.withdraw()
