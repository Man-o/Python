#constructor chaining super method
'''class c1:
    def __init__(self):
        print('Im Mano')
class c2(c1):
    def __init__(self):
        super().__init__()
        print('It is c2')
class c3(c2):
    def __init__(self):
        super().__init__()
        print('It is c3')
obj=c3()'''


#constructor chaining class method   
class c1:
    def __init__(self):
        print('Im Mano')
class c2():
    def __init__(self):
        c1.__init__(self)
        print('It is c2')
class c3():
    def __init__(self):
        c2.__init__(self)
        print('It is c3')
obj=c3()
