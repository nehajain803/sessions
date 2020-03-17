# Ass1
f=open(r"C:\Users\Kuljeet\Documents\demo.txt","r")
print(f.read())
print(f.read(10))
print(f.readline())
for x in f:
    print(x)
f.close()

# Ass2
f=open(r"C:\Users\Kuljeet\Documents\demo.txt","a")
f.write("morning")
f.close()
f=open(r"C:\Users\Kuljeet\Documents\demo.txt","r")
print(f.read())

# Ass3
f=open(r"C:\Users\Kuljeet\Documents\demo.txt","r")
print(f.read())
f.close()
f=open(r"C:\Users\Kuljeet\Documents\demo.txt","w")
f.write("oops1, I actually forgot u")
f.close()
f=open(r"C:\Users\Kuljeet\Documents\demo.txt","r")
print(f.read())
f.close()