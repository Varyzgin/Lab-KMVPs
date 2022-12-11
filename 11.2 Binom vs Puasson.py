# Варызгин Дмитрий
# Задание 11_2

import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
np.set_printoptions(precision=3)

N = 10
# биномиальное распределение
n, p = 100, 1/100
# распределение Пуассона
l = 1  # лямбда

x = np.arange(N)

yB = st.binom.pmf(x, n, p)
yP = st.poisson.pmf(x, l)

plt.vlines(x, 0, yB, color = 'gray')
plt.plot(x, yP, label = 'Распредление Пуассона')
plt.plot(x, yP, 'o', color = 'red')
plt.plot(x, yB, 'x', color = 'green', label = 'Биномиальное распределение')
plt.legend()

print('N Бином   Пуассон')
for i in range(N):
    print(f'{i} {yB[i]:.6f} {yP[i]:.6f}')

plt.show()

