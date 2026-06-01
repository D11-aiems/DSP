import time

def insertion_sort(a, n):
    for i in range(1, n):
        k = a[i]
        j = i - 1
        
        while j >=0 and a[j] > k:
            a[j + 1] = a[j]
            j = j - 1
            
            a[j + 1] = k
            
a=[]
n = int(input("enter size:"))
            
for i in range(n):
    a.append(int(input(" enter values: ")))
                    
start = time.time()
print("the array before sort:",a)
            
insertion_sort(a, n)
            
end = time.time()
print("the array after sort:", a)
print("the time taken to start array using insertion sort:",end - start)
                    
import matplotlib.pyplot as p
x = list(range(0,101))
y = [i * i for i in x]
p.plot(x, y)
p.title("time complexity of insertion sort")
p.xlabel("input size (n)")
p.ylabel("time / operations")
p.show()
                    