import matplotlib.pyplot as plt
import numpy as np
# Варызгин Дмитрий
# дано
N = int(input('N=?'))
x = np.linspace(1, 2, N)
f = 2 / x / x
F = 2 - 2 / x
nu = np.random.uniform(0, 1, N)
ksi = 2/(2 - nu)
# график функции распределения
plt.hlines(0, 0.9, 1, 'g')
plt.plot(x, F, label = 'F')
plt.plot(x, f, label = 'f') 
plt.hlines(1, 2, 2.1, 'g')

# гистограмма
kl = 1 + int(np.log2(N))
plt.hist(ksi, kl, density = True)

z1 = sorted(ksi)
NF = np.linspace(0, 1, N)
plt.plot(z1, NF)
pp=10
sm=np.mean(ksi)
svar=np.var(ksi)
print(f'вариационный ряд\n{z1[:pp]}')
print(f'выб среднее={sm:.3f} выб дисперсия={svar:.3f}')
plt.show() 