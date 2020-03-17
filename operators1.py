# 1.Arithmetic operators
x=20
y=40
z=x+y
a=x-y
b=x*y
c=x/y
print(z)
print(a)
print(b)
q=5.0
r=2
t=q%r
s=q//r
print(t)
print(s)

# 2.Assignment operators
w=30
print(w)
w+=6
print(w)
w-=6
print(w)
w*=8
print(w)
w/=7
print(w)
w%=4
print(w)
a=25
a//=4
print(a)
b=30
b**=2
print(b)

# 3.comparison operators
x=8
y=8
if(x==y):
    print("hello")
a=9
b=8
if(a!=b):
    print("bye")
s=85
t=96
if(s>t):
    print("The number is:85")
else:
    print("The number is:96")
x=85
y=62
if(x>=y):
    print("The number is:85")

# 4.Logical operators
a=10
b=20
print(a>b and b>a)
if(a>b or b>a):
    print("The number is:10")
else:
    print("Condition is false")
if(not(a>b or b>a)):
    print("The number is:10")
else:
    print("True")

# 5.Identity operators
x=25
y=25
if(x is y):
    print("identity",25)
else:
    print(56)
a=56
b=56
if(x is not y):
    print("The number is",56)
else:
    print("The number is",89)

# 6.Membership operators
x=["Orange","Apple"]
y=["Banana","Mango"]
print("banana"not in x)
print("Orange"in x)
if("Apple" not in y):
    print("Yes")

# 7.Bitwise operator
a=60
b=13
c=a&b
print(c)
d=a|b
print(d)
e=a^b
print(e)
f=~60
print(f)
i=b<<2
print(i)
b=13
j=b>>2
print(j)
z=-60
a=~z
print(a)












