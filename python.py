#izradili: Marko Glavas, Nikola Curilovic, Karlo Marunic
import pycuda.autoinit
import pycuda.driver as drv
import numpy as np
from pycuda.compiler import SourceModule

mod = SourceModule(open("zrno.cu").read())

e_sum = mod.get_function("e_sum")

n = int(input("Unesi broj iteracija: "))
d = int(input("Unesi broj decimala: "))
c = np.zeros(n, dtype=np.float32)

e_sum(drv.Out(c), block=(n,1,1), grid=(1,1))
# sumiraj sve clanove C matrice da bi dobili sumu reda                          
result = sum(c)

print (format(result, '.%df' %(d)))
#provjera                                                                      
print (c)

