# Ass1
x=lambda b:b-5
print(x(5))

# Ass2
y=lambda a,b,c:a*b+c
print(y(50,10,5))

# Ass3
z=lambda a,b,c,d,e,f:a+b*c-d/e+f
print(z(10,20,30,40,50,10))

# Ass4
def func(n):
    return lambda a:a*n
b=func(2)
print(b(11))

# Ass5
def fun(n):
    return lambda a:a+n
c=fun(10)
d=fun(30)
print(c(5))
print(d(6))

# Ass6
student={
    "name":"daman",
    "class":"M.C.A",
    "rollno":12
    }
print(student)

# Ass 7
def table(n):
    return lambda a:a*n
n=int(input("enetr the number"))
b=table(n)
for i in range(1,11):
    print(n,"X",i,"=",b(i))
