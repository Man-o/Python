from abc import ABC,abstractmethod
class animals:
    @abstractmethod
    def color(self):
        pass
    def legs(self):
        print('4 legs')
class dog(animals):
    def color(self):
        print('Black')
class cat(animals):
    def color(self):
        print('Black and White')
obj=dog()
obj.legs()
obj1=cat()
obj1.color()

        
