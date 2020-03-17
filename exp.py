# Ass1
try:
    a=10/0
    print (x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
else:
    print("no exception")

# Ass2
try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=a/b
    print("a/b = %d"%c)
except Exception:
    print("not divide by zero")
else:
    print("Hey i am else block")

# Ass3
try:
    a=10/0
    print(a)
except (ArithmeticError,ValueError) :
    print("Arithmetic Exception")
else:
    print("Successfully Done")

# Ass4
try:
    age=int(input("Enter the age:"))
    if age<18:
        raise ValueError;
    else:
        print("The age is valid")
except ValueError:
    print("The age is not valid")

# Ass5
class InvalidAge(Exception):
    def __init__ (self,age):
        super().__init__(self,age)
        self.age=age
class A():
    def m1(self,age):
        try:
            if age<18:
                raise Exception('Invalid Age')
            else:
                print("valid")
        except Exception as e:
            print(e)
ob=A()
age=int(input("enter the age:"))
ob.m1(age)

# Ass6
a=[1,2,3,4,5]
try:
    print("Second element = %d" %(a[1]))
    # print("Sixth element=%d"%(a[5]))
except IndexError:
    print("An error occured")

# Ass7
try:
    a=5
    if a<4:
        b=(a/(a-3))
        print("value of b",b)
except(ZeroDivisionError, NameError):
    print("Error Occurred and Handled")
else:
    print("value is correct")
