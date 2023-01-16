# 실수와 실수의 비교

# 1
from math import sqrt
n = sqrt(3.0)
print(n * n == 3.0)

# 2
from math import sqrt
n = sqrt(3.0)
print( abs(n*n - 3.0 ) < 0.00001 )

# 3
import math  
print(math.isclose(3.14, 3.15))
print(math.isclose(3.141590003, 3.141590002))
