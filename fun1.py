# Ass1
for i in range(1,20,2):
    print(("*" *i).center(20))

# Ass 2
a,b,x,y=1,15,3,4
def foo(x,y):
    global a
    a=42
    x,y=y,x
    b=33
    b=17
    c=100
    print(a,b,x,y)
foo(17,4)
print(a,b,x,y)

# Ass3
def f():
    x=42
    def g():
        global x
        x=43
    print("Before calling g :",x)
    g()
    print("After calling g:",x)
f()
print("x in main:",x)

# Ass4
name="ratan"
def outer():
    var_outer="ratan"
    def inner():
        nonlocal var_outer
        var_outer="anu"
        global name
        name="ratanit"
        print(var_outer)
    print(var_outer)
    inner()
    print(var_outer)
outer()

# Ass5
def outer():
    name1="ratan"
    def inner():
        nonlocal name1
        name1="durga"
    inner()
    print(name1)
outer()

# Ass6
def outer():
    s="ratan"
    def inner1():
        s="durga"
    def inner2():
        nonlocal s
        s="sunny"
    def inner3():
         global s
         s="srayva"
    print(s)
    inner1()
    print(s)
    inner2()
    print(s)
    inner3()
    print(s)
outer()
print(s)

# Ass7
a_var=10
b_var=15
e_var=25
d_var=100
def a_func(a_var):
    print("in a_func a_var=",a_var)
    b_var=100+a_var
    d_var=2*a_var
    print("in a_func b_var=",b_var)
    print( "in a_func d_var=",d_var)
    print( "in a_func e_var=",e_var)
    return b_var+10
c_var=a_func(b_var)
print("a_var=",a_var)
print("b_var=",b_var)
print("c_var=",c_var)
print("d_var=",d_var)

# Ass8
def outer():
    name1="ratan"
    def inner():
        nonlocal name1
        name1="durga"
    inner()
    print(name1)
outer()

# Ass9
eid,email,esal=1,'aaa',10000.56
def emp(eid,email,esal):
    globals()['eid']=eid
    globals()['email']=email
    globals()['esal']=esal
    print(eid,email,esal)
def disp():
    print(eid,email,esal)
emp(111,'ratan',10000.45)
disp()
print(eid,email,esal)


