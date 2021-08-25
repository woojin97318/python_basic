# Library functions for prime 
import sympy 
  
# Output : True 
print(sympy.isprime(5))                         
  
# Output : [2, 3, 5, 7, 11, 13, 17, 19, 23,  
# 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,  
# 73, 79, 83, 89, 97]
print(list(sympy.primerange(100, 1000)))