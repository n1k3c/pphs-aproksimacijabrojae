#izradili: Marko Glavas, Nikola Curilovic, Karlo Marunic                                            
import time
import pycuda.autoinit
import pycuda.driver as drv
import numpy as np
from pycuda.compiler import SourceModule

mod = SourceModule(open("zrno.cu").read())

e_sum = mod.get_function("e_sum")

n = int(input("Unesi broj iteracija: "))
c = np.zeros(n, dtype=np.float32)
start = time.time()
e_sum(drv.Out(c), block=(250,1,1), grid=(1,1))
# sumiraj sve clanove C matrice da bi dobili sumu reda                                              
result = sum(c)

print(result)
end = time.time()
print(end-start)


