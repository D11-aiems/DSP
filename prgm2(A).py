class student:
    def __init__(self):
        self.roll_no=input("enter roll_no number:")
        self.name=input("enter name:")
        self.python=int(input("enter python marks:"))
        self.java=int(input("enter java marks:"))
        self.os=int(input("enter os marks:"))
        self.se=int(input("enter se marks:"))
    def display(self):
        print("\n students name is:",self.name)
        print("students roll_no is:",self.roll_no)
        print("python marks is:",self.python)
        print("java marks is:",self.java)
        print("os marks is:",self.os)
        print("se marks is:",self.se)
    def total_avg(self):
        total=self.python+self.java+self.os+self.se
        avg=total/4
        print("total marks is:",total)
        print("avg marks is:",avg)
    def result(self):
        if(self.python<35):
            print("failed in pyton")
        else:
            print("pass in python")
        if(self.java<35):
            print("failed in java")
        else:
            print("pass in java")
        if(self.os<35):
            print("failed in os")
        else:
            print("pass in os")
        if(self.se<35):
            print("failed in se")
        else:
            print("pass in se")
 
n=int(input("enter nunmber of students"))
students=[]

for i in range(n):
    print("\n enter details of students",i+1)
    students.append(student())
                                         
for s in students:
    s.display
    s.total_avg()
    s.result()
                
import matplotlib.pyplot as p

x = list(range(101))
y = [i for i in x]

p.plot ( x, y)
p.title("ADT - Time Complexity")
p.xlabel("Input")
p.ylabel("Time")
p.show()                                 
                                