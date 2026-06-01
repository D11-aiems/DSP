import time
a=[]

def divide(a,low,high):
    if(low<high):
        mid=(low+high)//2
        divide(a,low,mid)
        divide(a,mid+1,high)
        merge(a,low,mid,high)
        
def merge(a,low,mid,high):
    temp=[]
    i=low
    k=low
    j=mid+1
    while(i<=mid and j<=high):
        if(a[i]<a[j]):
            temp.insert(k,a[i])
            i=i+1
            k=k+1
        else:
            temp.insert(k,a[j])
            j=j+1
            k=k+1
        while(i<=mid):
           temp.insert(k,a[i])
           k=k+1
           i=i+1
        while(j<=high):
           temp.insert(k,a[j])
           k=k+1
           j=j+1
           p=low
           m=0
        while(p<k):
           a[p]=temp[m]
           p=p+1
           m=m+1
                        
n=int(input("enter size:"))
for i in range(0,n):
    v=int(input("enter values:"))
    a.append(v)
start=time.time()
print("the array before sort:",a)
divide(a,0,n-1)
end=time.time()
print("the array after sort:",a)
print("the time taken to sort an array using merge sort",end-start)
                            
import math
import matplotlib.pyplot as p
p.title("merge sort")
p.xlabel("input")
p.ylabel("time")
x=list(range(1,101))
y=[i*math.log(i) for i in x]
p.plot(x,y)
p.show()
            