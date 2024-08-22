#public access modifiers
'''class public:
    def __init__(self):
        self.b=5
    def m1(self):
        print(self.b)
obj1=public()
obj1.m1()'''

#protected access modifiers
'''class protected:
    def __init__(self):
        self.pub='It is public access modifier'
        self._prot='It is protected access modifier'
    def main(self):
        print(self.pub)
        print(self._prot)
obj=protected()
obj.main()
print(obj._prot)'''

#private access modifiers
'''class private:
     def __init__(self):
        self.pub='It is public access modifier'
        self._prot='It is protected access modifier'
        self.__priv='It is private access modifier'
     def main(self):
        print(self.pub)
        print(self._prot)
        print(self.__priv)
obj=private()
print(obj.pub)
print(obj._prot)
print(obj.__priv)'''

#access private access modifier outside the class
'''class private:
     def __init__(self):
        self.pub='It is public access modifier'
        self._prot='It is protected access modifier'
        self.__priv='It is private access modifier'
     def getter(self):
         return self.__priv
     def setter(self):
         self.__priv='Private access modifier'
obj=private()
print(obj.getter())
obj.setter()
print(obj.getter())'''







    
        
        

    
