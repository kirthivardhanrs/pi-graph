import math
import matplotlib.pyplot as plt

iter = 1000

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

def prime(num):
    flag = 0
    if (num == 2):
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            flag = 1
            break
    if (flag == 0):
        return True
    else:
        return False

def the_prime_numbers_i_legit_dont_know_how_this_works_but_apparently_it_works_to_a_certain_extent():
    num = 2
    sum = 1
    x, y = [], []
    for i in range(iter):
        x.append(i)
        while (prime(num) == False):
            num += 1
        frac = 1/num
        if ((num-1) % 4 == 0):
            sum *= (1+frac)
        else:
            sum *= (1-frac)
        y.append(2/sum)
        num += 1
    return [x, y]
    

plt.plot(the_prime_numbers_i_legit_dont_know_how_this_works_but_apparently_it_works_to_a_certain_extent()[0], the_prime_numbers_i_legit_dont_know_how_this_works_but_apparently_it_works_to_a_certain_extent()[1], label = "Prime Numbers")
plt.plot(leibniz()[0], leibniz()[1], label = "Leibniz")
plt.plot(euler()[0], euler()[1], label = "Euler")
plt.plot(pi()[0], pi()[1], label = "Python")
plt.legend()
plt.show()