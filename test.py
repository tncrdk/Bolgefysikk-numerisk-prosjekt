import numpy as np

a = np.array([i for i in range(10)])

filter = a > 5

a_filtered = a[filter]

print(a)
print(filter)
print(a_filtered)
