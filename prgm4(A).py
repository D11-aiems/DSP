import time
import math
import matplotlib.pyplot as p

a = []

def binary_search(a, low, high, key):
    if low <= high:
        mid = (low + high) // 2

        if key == a[mid]:
            print("Key element found at position:", mid)
            return mid

        elif key < a[mid]:
            return binary_search(a, low, mid - 1, key)

        else:
            return binary_search(a, mid + 1, high, key)

    print("Key element not found")
    return -1


n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input("Enter element: "))
    a.append(element)

a.sort()   # Binary search requires sorted array

key = int(input("Enter key value: "))

start = time.time()

print("The array is:", a)
print("The key element is:", key)

result = binary_search(a, 0, n-1, key)

end = time.time()

print("Time taken to search an element using binary search:", end - start)


# Plotting Time Complexity Graph
x = list(range(1, 101))
y = [math.log(i) for i in x]

p.plot(x, y)
p.title("Binary Search Time Complexity")
p.xlabel("Input Size (n)")
p.ylabel("Time Complexity (log n)")
p.show()