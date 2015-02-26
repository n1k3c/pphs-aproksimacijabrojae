#include <math.h>

__device__ float fact_fun(int idx){
  float fact = 1;
  for(int i = 1; i<idx+1; i++){
    fact = fact*i;
  }
  fact = 1/fact;
  return fact;
}

__global__ void e_sum(float *c){
  int duljina = 500;
  const int idx = threadIdx.x;
  c[idx] = fact_fun(idx);
  c[duljina-idx-1] = fact_fun(duljina-idx);

}

