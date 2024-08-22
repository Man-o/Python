class a:
    pass
class b(a):
    pass
class c(a):
    pass
class d(b,c):
    pass
class e(b,c):
    pass
class f(d,e):
    pass
print(f.mro())
