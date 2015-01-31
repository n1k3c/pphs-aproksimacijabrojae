                                         
#include <math.h>

__global__ void e_sum(float *c){

  const int idx = threadIdx.x;
  double fact = 1;
  for(int i = 1; i<idx+1; i++){
    fact = fact*i;
  }
  fact = 1/fact;
  c[idx] = fact;

}


