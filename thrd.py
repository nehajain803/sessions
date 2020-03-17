# Ass1
from threading import Thread
class a(Thread):
  def run(self):
    print("hello")
ob=a()
ob.start()

# Ass2
import threading
class b(threading.Thread):
    def run(self):
        for x in range(7):
           print("Hi from child")
a =b()
a.start()


# Ass3
from threading import Thread
class a():
    def f1(self):
        for x in range (2):
            print("hello")
ob=a()
t1=Thread(target=ob.f1())
t1.start()

# Ass4
def f1():
    f=open("mod.txt","wt")
    for x in range(2):
        f.write("This is a file")
     f.close()
f1()

