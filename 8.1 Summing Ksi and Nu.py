# Варызгин Дмитрий (2 группа ФИИТ)
# Задание 8_1

import matplotlib.pyplot as plt
import numpy as np

# параметры
N = 100000
n = 2 # число слагаемых
a = 0 # интервал
b = 2
kl = 1 + int(np.log2(N)) 

# работаем со случайными величинами как с массивами
ksi = np.random.uniform(a, b, N) # заранее задали N значений в массве
eta = np.random.uniform(a, b, N)
nu = ksi + eta
F = np.linspace(0, 1, N)
plt.plot(sorted(nu), F)
plt.hist(nu, kl, density=True, edgecolor='black')
plt.show()

# или работаем со случайной величиной с помощью цикла
n = 2 # число слагаемых
ksi1 = [0] * n
nu1 = [0] * n # результативная случайная величина
for i in range(0, n):
    ksi1[i] = np.random.uniform(a, b, N)
    nu1[i] = ksi1[i] + nu1[i - 1] # -1 индекс при i = 0 норма (возьмется последняя в очереди) 
    plt.hist(nu1[i], kl, density = True, edgecolor = 'black')
    plt.show()
