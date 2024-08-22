#method chaining using class method
'''class a:
    def m1(self):
        print('its m1')
class b():
    def m2(self):
        print('its m2')
        a.m1(self)
class c():
    def m3(self):
        print('its m3')
        b.m2(self)
obj=c()
obj.m3()'''


#method chaining using super method
class a:
    def m1(self):
        print('its m1')
class b(a):
    def m2(self):
        print('its m2')
        super().m1()
class c(b):
    def m3(self):
        print('its m3')
        super().m2()
obj=c()
obj.m3()
