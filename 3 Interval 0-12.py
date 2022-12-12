# Варызгин Дмитрий (2 группа ФИИТ)
# Задание 3_1

import matplotlib.pyplot as plt
import scipy.stats as st
import random as rd
import numpy as np

N = 1000

# интервал
a = 0
b = 12

z = [0] * N
for i in range(N):
    z[i] = rd.uniform(a, b)
# или 3 строчки превращаются в: z = [rd.uniform(a, b) for i in range(N)]

# scipy плотность распределения
f = st.uniform.pdf(z, a, b - a)
plt.plot(z, f, color = 'blue', label = 'Плотность распределения')

# scipy функция распределения
F = st.uniform.cdf(z, a, b - a)
plt.plot(z, F, color = 'green', label = 'Теоретическая функция распределения')

# функция распределения без использования scipy
NF = np.linspace(0, 1, N)
plt.plot(sorted(z), NF, color = 'red', label = 'Фактическая функция распределения')

# гистограмма
kl = 1 + int(np.log2(N)) # формула для определения кол-ва интервалов
plt.hist(z, kl, density = True, color = 'gray')

# характеристики
print(f'Выб. среднее = {np.mean(z):.3f}, Выб. дисперсия = {np.var(z):.3f}')

# красота пунктирная
plt.vlines(b, 0, np.max(f), color = 'blue', linestyle = 'dotted')
plt.vlines(a, 0, np.max(f), color = 'blue', linestyle = 'dotted')
plt.hlines(0, a - 1, a, color = 'green')
plt.hlines(1, b, b + 1, color = 'green')
plt.hlines(0, b, b + 1, color = 'blue')

# вингардиум-левиосса
plt.legend()
plt.show()