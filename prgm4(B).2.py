import time

a=[]

def qs(a,low,high):
    if(low<high):
        pivot=divide(a,low,high)
        qs(a,low,pivot-1)
        qs(a,pivot+1,high)
        
def divide(a,low,high):
    pivot=a[low]
    i=low+1
    j=high
    while 1:
        while(i<high) and (pivot>=a[i]):
            i=i+1
        while(pivot<a[j]):
            j=j-1
        if i<j:
            a[i],a[j]=a[j],a[low]
        else:
            a[low],a[j]=a[j],a[low]
            return j
        
n=int(input("enter size:"))
for i in range(0,n):
    value=int(input("enter values:"))
    a.append(value)
start=time.time()
print("the array before sort:",a)
qs(a,0,n-1)
end=time.time()
print("the array value after sort:",a)
print("time taken to sort an array using quick sort",end-start)

import math
import matplotlib.pyplot as p
p.title("quick sort")
p.xlabel("input")
p.ylabel("time")
x=list(range(1,101))
y=[i*math.log(i) for i in x]
p.plot(x,y)
p.show()
