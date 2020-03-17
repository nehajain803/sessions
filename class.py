# Ass1
class b:
    a=5
    print("a=",a)

# Ass2
class student():
    id=12
    name="Daman"
    def func(self):
        print("ID=%d\nName=%s"%(self.id,self.name))
std=student()
std.func()

# Ass3
class hello():
    a=20
    b=30
    c=a+b
    def func(self):
        print("A=%d\nB=%d\nC=%d"%(self.a,self.b,self.c))
h1=hello()
h1.func()

# Ass4(constructor)
class  student():
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch
    def display(self):
             print("Name:%s\nAge:%d\nBranch:%s"%(self.name,self.age,self.branch))
obj=student("Daman",22,"M.C.A")
obj1=student("Aman",22,"B.C.A")
obj.display()
obj1.display()


# Ass5
class number():
    x=10
    y=20
    def __init__(self,x,y):
        print("value of x",self.x)
        print("value of y",self.y)
n1=number(10,20)

# Ass6
class num():
    a=10
    def __init__(self,a):
        print("The value of x=%d"%(self.a))
a=num(10)


# Ass7
class hello():
    def _str__(self):
        return("hello")
s=hello()
print(s)

# Ass8
class student():
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Employee deleted")
g=student()
del g