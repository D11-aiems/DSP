import time
import matplotlib.pyplot as p

a=[]

def bubble_sort(a,n):
    for i in range(n):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
        return a
    
n = int(input("enter size:"))
for i in range(n):
    value = int(input("enter values:"))
    a.append(value)
        
print("array before sort:",a)
start = time.time()
bubble_sort(a, n)
end = time.time()
print("array after sort:", a)
print("time taken to start array using bubble sortr:",end - start)
        
#asymptotic graph O(n^2)
x = list(range(0,101))
y = [i * i for i in x]
        
p.plot(x, y)
p.title("time complexity of bubble sort")
p.xlabel("input size (n)")
p.ylabel("time / operations")
p.show()
        