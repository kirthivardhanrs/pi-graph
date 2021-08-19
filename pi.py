import math
import matplotlib.pyplot as plt

iter = 100

def leibniz():
    x,y = [],[]
    sign = True
    sum = 0
    denom = 1
    for i in range(1, iter+1):
        x.append(i)
        if (sign):
            sum += 1/denom
        else:
            sum -= 1/denom
        sign = not sign
        denom += 2
        y.append(sum*4)
    return [x, y]

def euler():
    x,y = [], []
    sum = 0
    for i in range(1, iter+1):
        frac = 1/(i**2)
        sum += frac
        x.append(i)
        y.append(math.sqrt(sum*6))
    return [x, y]

def pi():
    x, y = [], []
    for i in range(iter):
        x.append(i)
        y.append(math.pi)
    return [x, y]

plt.plot(leibniz()[0], leibniz()[1])
plt.plot(euler()[0], euler()[1])
plt.plot(pi()[0], pi()[1])
plt.show()

