import math
import matplotlib.pyplot as plt

iter = 100

def leibniz():
    x,y = [],[]
    sign = True
    sum = 0
    for i in range(1, iter+1, 2):
        x.append(i)
        if (i%2 != 0):
            frac = 1/i
            if (sign):
                sum += frac
            else:
                sum -= frac
            sign = not sign
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

plt.plot(leibniz()[0], leibniz()[1])
plt.plot(euler()[0], euler()[1])
plt.show()
