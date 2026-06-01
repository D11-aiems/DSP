import time

a=[]

def selection_sort(a,n):
    for i in range(0, n - 1):
        min = 1
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
                # swap A[i] and A[min] using temp
                temp = a[i]
                a[i] = a[min]
                a[min] = temp
                
        return a
    
n = int(input("enter size:"))
for i in range(n):
    value = int(input("enter values:"))
    a.append(value)
        
print("the array before sort:",a)
start = time.time()
selection_sort(a, n)
end = time.time()
print("the array after sort:", a)
print("the time taken to start array using selection sort:",end - start)
        
x = list(range(0,101))
y = [i * i for i in x]

import matplotlib.pyplot as p        
p.plot(x, y)
p.title("time complexity of selection sort")
p.xlabel("input size (n)")
p.ylabel("time / operations")
p.show()
        