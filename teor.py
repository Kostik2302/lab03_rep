import numpy as np
from scipy.stats import rv_continuous
import time
import random

n = int(input("Введите n "))

class distribution_gen(rv_continuous):
    "distribution"
    def _pdf(self, x):
      return (4 * (np.log(x)) ** 3)/x


print("С помощью наследования (первые 10 значений, все не выводим, но находим)")
start1 = time.perf_counter()
distr = distribution_gen(0,1,np.e)
rand = distr.rvs(size=n)
print(rand[:10])
finish1 = time.perf_counter() - start1

print("С помощью обратной функции (первые 10 значений, все не выводим, но находим)")

reversarr = []
start2 = time.perf_counter()
for i in range(0,n):
    p = random.random()
    reversf = np.e ** (p ** 0.25)
    reversarr.append(reversf)

print(reversarr[:10])
finish2 = time.perf_counter() - start2
print()
print(finish1, " - Время потраченное методом наследования от класса")
print(finish2, " - Время потраченое при использовании обратной функции")

