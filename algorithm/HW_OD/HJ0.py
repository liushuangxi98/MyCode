import time
n = 3000000000
s = time.time()
a = 2 ** n
print(time.time() - s)
s = time.time()
a = 1 << n
print(time.time() - s)
