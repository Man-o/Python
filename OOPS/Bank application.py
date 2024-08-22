class CUB:
    ROI=7
    Branch='Chennai'
    IFSC='CUB00025'
    def __init__(self,Name,Acc_No,Aadhar,Mobile,Gender,Balance,Pin):
        self.Name=Name
        self.Acc_No=Acc_No
        self.Aadhar=Aadhar
        self.Mobile=Mobile
        self.Gender=Gender
        self.Balance=Balance
        self.Pin=Pin
    @classmethod
    def changeBranch(cls):
        cls.Branch='Banglore'
    @staticmethod
    def checkpin():
        User_pin=int(input('Enter the pin:'))
        return User_pin
    def deposit(self):
        if self.Pin==self.checkpin():
            Deposit_Amount=int(input('Enter the deposit amount:'))
            self.Balance+=Deposit_Amount
            print(f'Your account no {self.Acc_No} is credited for RS.{Deposit_Amount}.00 and Availabale balance is {self.Balance}')
        else:
             print('Incorrect Pin Try again')
             for i in range(2):
                if self.Pin==self.checkpin():
                    Deposit_Amount=int(input('Enter the deposit amount:'))
                    self.Balance+=Deposit_Amount
                    print(f'Your account no {self.Acc_No} is credited for RS.{Deposit_Amount}.00 and Availabale balance is {self.Balance}')
                    break
                elif i<1:
                    print('Incorrect Pin Try again')
             else:
                 print('Limit has been reached try after 24hours')
    def pinchange(self):
        if self.Pin==self.checkpin():
            enter_pin=(int(input('Enter the old pin:')))
            if enter_pin==self.Pin:
                new_pin=int(input('Enter the new pin:'))
                if new_pin==self.Pin:
                    print('Your new pin is same as old pin.Try again.')
                else:
                    print(f'Your pin was successfully change.New pin number is {new_pin}')
            else:
                print('Invalid Pin')
        else:
            print('Incorrect Pin Try again')
            for i in range(2):
                if self.Pin==self.checkpin():
                    enter_pin=(int(input('Enter the old pin:')))
                    if enter_pin==self.Pin:
                        new_pin=int(input('Enter the new pin:'))
                        if new_pin==self.Pin:
                            print('Your new pin is same as old pin.Try again.')
                        else:
                            print(f'Your pin was successfully change.New pin number is {new_pin}')
                            break
                    else:
                        print('Incorrect Pin Try again')
                elif i<1:
                    print('Incorrect Pin Try again')  
            else:
                print('Limit has been reached try after 24hours')
            
    def withdraw(self):
        if self.Pin==self.checkpin():
            withdraw_amount=int(input('Enter the withdraw amount:'))
            if withdraw_amount<=self.Balance:
                self.Balance-=withdraw_amount
                print(f'Your account no {self.Acc_No} is debited for RS.{withdraw_amount}.00 and Availabale balance is {self.Balance}')
            else:
                print('Insufficent balance')       
        else:
            print('Incorrect Pin Try again')
            for i in range(2):
                if self.Pin==self.checkpin():
                    withdraw_amount=int(input('Enter the withdraw amount:'))
                    if withdraw_amount<=self.Balance:
                        self.Balance-=withdraw_amount
                        print(f'Your account no {self.Acc_No} is debited for RS.{withdraw_amount}.00 and Availabale balance is {self.Balance}')
                    else:
                        print('Insufficent balance') 
                    break
                elif i<1:
                    print('Incorrect Pin Try again')     
            else:
                print('Limit has been reached try after 24hours')        
    def checkbalance(self):
        if self.Pin==self.checkpin():
            print(f'Available balance is RS.{self.Balance}.00')
        else:
            print('Incorrect Pin Try again')
            for i in range(2):
                if self.Pin==self.checkpin():
                    print(f'Available balance is RS.{self.Balance}.00')
                    break
                elif i<1:
                    print('Incorrect Pin Try again')
            else:
                print('Limit has been reached try after 24hours')  
Cust1=CUB('Vaishali',54888034,2456788,9087653255,'Female',4000,2503)
Cust2=CUB('Ramesh',65478936,4563789,987654321,'Male',500,7819)
Cust1.pinchange()
#Cust1.withdraw()
#Cust1.checkbalance()
#Cust1.deposit()

            
