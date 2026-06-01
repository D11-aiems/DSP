import time

a= []

def linear_search(a, n, key):
    for i in range(0, n):
        if key == a[i]:
            print("key element found at position:", i)
            return
        print("key element not found")
        
        
n=int(input("enter number of elements: "))
for i in range(0, n):
    element = int(input("enter an element: "))
    a.append(element)
    
key = int(input("enter key value: "))

print("An array is:", a)

start = time.time()
print("the key element is:", key)
linear_search(a, n, key)
end = time.time()

print("Time taken to search element using linear search:", end - start)   

import matplotlib.pyplot as p
x=list(range(101))
y=[i for i in x]
p.plot(x,y)
p.title("linear search - Time Complexity ")
p.xlabel("input")
p.ylabel("time")
p.show()