# 1.list
l=["hello","bye","tata"]
print(l)
print(l[2])
for x in l:print(x)
l.append("neha")
print(l)
l.extend("tata")
print(l)
print(l[0:2])
l1=("howareyou")
print(l1[1:5])
l[2]= "world"
print(l)
if "hello" in l:
    print("yes,hello is in the list")
print(len(l))
l.insert(0,"orange")
print(l)
l.pop()
print(l)
del l[1]
print(l)
l2=l.copy()
print (l2)
l3=l+l2
print (l3)

# 2.Tuple
t=("aman","daman","mandeep","neha","tania")
print(t)
print(t[0:3])
for y in t:
    print(y)
l=list(t)
print(l)
l[2]="aman"
print (l)
print(len(t))
if "daman" in t:
    print("No,daman is not in the list")

# 3.set
s={"a","e","i","o","u","0"}
s2={1,2,3,4,5,6,"o"}
print(s)
for z in s:
    print (z)
print(len(s))
print(id(s))
s.add("neha")
print(s)
s.update(["daman","aman"])
print(s)
s.remove("daman")
print(s)
s.discard("aman")
print(s)
s3=s.union(s2)
print("s3",s3)
print(s)
print(s2)
s4=s.intersection(s2)
print("s4",s4)

# Dictionary
student={
    "name":"daman",
    "class":"M.C.A",
    "rollno":12
    }
print(student)
for x in student:
    print (student[x])
for x in student:
    print(x)
student["rollno"]=45
print(student)
x=student.get("name")
print(x)
student["branch"]="M.C.A"
print(student)
student.pop("class")
print(student)
student["college"]="G.N.E"
print(student)
student.pop("name")
print(student)
for z in student.values():
    print(z)
for s in student.items():
    print(s)
if "branch" in student:
    print("yes,branch is given in the student")
print(len(student))