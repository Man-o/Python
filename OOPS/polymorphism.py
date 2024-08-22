#overloading
'''class a3():
    def m1(self,val1):
        print(val1)
    def m1(self,val1,val2):
        print(val1+val2)
    def m1(self,val1,val2,val3):
        print(val1+val2+val3)
obj=a3()
obj.m1(1,2,3)'''

#overloading-Non keyword argument
'''class a3:
    def m1(self,*args):
        res=0
        for ele in args:
            res+=ele
        return res
obj=a3()
print(obj.m1(1,2))
print(obj.m1(7,8))'''

#overloading-reduce function
'''class a3:
    def m1(self,*args):
        from functools import reduce
        return (reduce(lambda a,b:a+b,args,0))
obj=a3()
print(obj.m1(1,2))
print(obj.m1(1))
print(obj.m1())'''

#overloading-positional arguments
'''class a3:
    def m1(self,a=0,b=0,c=0,d=0):
        return(a+b+c+d)
obj=a3()
print(obj.m1(1,3))
print(obj.m1(1,3,6))
print(obj.m1(1,3,6,7,8))'''


#overriding
class parent:
    def m1(self):
        print('parent class m1')
class child(parent):
    def m1(self):
        print('child class m1')
obj=child()
obj.m1()

    
