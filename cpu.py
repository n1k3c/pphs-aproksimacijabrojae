import numpy as np
import time

def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

n = int(input("Unesi broj iteracija: "))
c = np.zeros(n, dtype=np.float32)
start=time.time()
for x in range (0,n):
	c[x] = 1/factorial(x)

result = sum(c)
end=time.time()
print(result, end-start)
