num=123456
add=0
while num!=0:
    add+=num%10
    num//=10
print(add)
print('=========================================================')
num=6383706374
even=0
odd=0
while num!=0:
    rem=num%10
    if rem%2==0:
        even=rem
        print(f'Even number{even}')
    else:
        odd=rem
        print(f'Odd number{odd}')
    num//=10
print('=========================================================')
num =11111231
even=0
odd=0
while num!=0:
    rem=num%10
    if rem%2==0:
        even+=rem
    else:
        odd+=rem
    num//=10
print(even,odd)
print('=========================================================')   

        
    
