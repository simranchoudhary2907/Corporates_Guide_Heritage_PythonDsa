import time
import numpy as np

# Python List
start = time.time()

lst = []
for i in range(100000):
    lst.append(i)

end = time.time()

list_time = end - start

# NumPy Array
start = time.time()

arr = np.arange(100000)

end = time.time()

numpy_time = end - start

print("Python List Time:", list_time)
print("NumPy Array Time:", numpy_time)