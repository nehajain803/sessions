# if else
a=20
b=55
if(a>b):
    print("a is less than b")
else:
    print("b is greater")


# User input
n=int(input("Enter  first number"))
m=int(input("Enter  second number"))
if n>m:
    print(n,"is greater")
else:
    print(m,"is greater")

# elif
a=int(input("Enter first value"))
b=int(input("Enter second value"))
c=int(input("Enter third value"))
if a>b:
    print(a," is greater")
elif b>c:
    print(b," is greater")
else:
    print(c," is greater")

# Range
range(10)
for x in range(10):
    print(x)
range(2,15)
for y in range(2,15):
    print(y)

range=("daman","aman","mandeep","neha","tania")
for z in range:
    print(z,end=" ")

# nesting  for loop
range(1,5)
for x in range(4):
    print(x,end=" ")
for y in range(4):
    print(y,end=" ")
for a in range(4):
 for b in range(5):
    print(a,b,end=" ")
    print()

# Square Star
for a in range(2):
 for b in range(2):
     print("*","*","*","*",end="")
     print()

# while loop
i=1
while i<6:
    print(i)
    if (i==3):
        break
    i+=1




