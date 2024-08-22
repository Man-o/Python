class me():
    name="Mano"
    age=20
    degree='BE COMPUTER SCIENCE'
obj1=me()
obj2=me()
#access with object reference
print(obj1.name)
#access with class reference
print(me.age)
#modify in object reference
obj2.age=21
print(obj2.age)
print(obj1.age)
#modify in class
me.degree='BE CSE'
print(me.degree)

    
