# Defining a function
# Ass1
def hello():
    print("DAMANJOT")
hello()

# Ass2
def name(fname):
     print(fname +"Jain")
name("Neha")
name("Daman")
name("Aman")

# Ass3
def hello(fname,lname):
    print("Neha"+" "+"Jain")
hello("Neha","Jain")

# Ass4
def add(value1,value2):
    result=value1+value2
    print(result)
    res=value2*value1
    print(res)
add(20,30)

# Ass5
def color(*colours):
    print("Fav color is "+" "+ colours[2])
color("orange","red","yellow","purple")

# Ass6
def child(child1,child2,child3):
    print("First child is "+" "+child3)
child(child2="Daman",child1="Neha",child3="Tania")

# Ass7
def num(num1,num2,num3):
    x=num1*num2/num3
    return x
result=num(100,20,300)
print(result)

# Local & Global functions
def outer():
    x="local"
def inner():
    global x
    x="nonlocal"
    print("inner",x)
inner()
print("outer",x)
outer()

# 2.
x=5
def foo():
    x=10
    print("local x is:",x)
foo()
print("global x is:",x)

# 3.
age=int(input("Enter your age:"))
def vote(age):
  if age>18:
      print("You are eligible")
  else:
      print("You are not eligible")

vote(age)

# 4.
def red():
    a=1
def blue():
    b=2
    print(a)
    print(b)
    blue()
    print(a)
red()

