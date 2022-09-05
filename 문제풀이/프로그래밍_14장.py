#1
import numpy as np
x = np.array([i for i in range(9)])
print(x)
x = np.reshape(x, (3,3))
print(x)
# or
x = np.arange(9).reshape(3,3)
print(x)

#2
import numpy as np
x = np.random.rand(3,3)
print(x)

#3
import numpy as np
x = np.random.rand(10,10)
print(x.max(), x.min())

#4
import numpy as np
x = np.ones((3,3))
x[1:-1, 1:-1] = 0
print(x)

#5
import numpy as  np
x = np.zeros((5,5))
print(x)
x[1::2, ::2]=1
x[::2, 1::2]=1
print(x)

#6
import numpy as  np
x = np.random.rand(3,3)
print(x)
x = (x - np.mean(x)) /  np.std(x)
print(x)

#7
import numpy as  np
x = np.arange(10)
print(x)
x[5:9]=x[5:9] * -1
print(x)

#8
import numpy as  np
x = np.arange(9).reshape((3,3))
print(x)
print(np.sum(x), np.sum(x, axis=0), np.sum(x, axis=1))

#9
import numpy as np
x = np.array([4,5])
y = np.array([7,10])
print("원본벡터:\n", x, y)
print("벡터의 내적 : ", np.dot(x,y))

#10
import matplotlib.pyplot as plt
x = [2,0,3,6,4,6,8,12,10,9,18,20,22]
plt.plot(x)
plt.show()

#11
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sigmoid(x)")
plt.show()
