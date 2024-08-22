class a:
    a=int(input('Enter Number:'))
    def properties(self):
        print('Its p1')
class b:
    b=18
    def properties(self):
        print('Its p2')
class c(b,a):
    c=18
    def properties(self):
        super().properties()
        print('Its p3')
obj=c()
obj.properties()
print(obj.a)
