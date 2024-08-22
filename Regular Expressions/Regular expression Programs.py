import re
#Check the mobile number is valid or not
#Mno='+91-6383706374'
'''Mno=input('Enter Mobile number:')
if(re.match('[+]91(|-| )[6-9][0-9]{9}$',Mno)):
    print('Valid Mobile number')
else:
    print('Invalid Mobile Number')'''


#Check the given emailid is valid or not
#Email='_freaky.2503@gmail.com'
Email=input('Enter Email:')
if(re.match('\w+[.]?\w+@gmail[.]com$',Email)):
    print('Valid Email')
else:
    print('Invalid Email')



