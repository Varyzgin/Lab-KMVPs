# Варызгин Дмитрий
# Задание 5_1

import matplotlib.pyplot as plt
import numpy as np

N = int(input('N = ')) # Данные с клавиатуры
x = np.linspace(0, 3, N) # x из [0, 3] в N реализациях
f = 2 * np.exp(-2 * x) # плотность распределения
F = 1 - np.exp(-2 * x) # функция распределения
nu = np.random.uniform(0, 1, N) # ню нормально распределена
ksi = -np.log(1 - nu) / 2 # обратная функция

# графики законов распределения
plt.hlines(0, -0.5, 0, 'g', color = 'blue')
plt.plot(x, F, color = 'blue', label='Функция распределения F')
plt.plot(x, f, color = 'green', label='Плотность распределения f') 

# гистограмма
kl = 1 + int(np.log2(N)) # рассчет длины столбца гистограммы по ф.Стержесса
plt.hist(ksi, kl, density = True, color = 'gray')

# модель функции распределения
z1 = sorted(ksi)
NF = np.linspace(0, 1, N)
plt.plot(z1, NF, color = 'red', label='Модель функции NewF')

# характеристики случайной величины
pp = 10
sm = np.mean(ksi)
svar = np.var(ksi)
print(f'Вариационный ряд\n{z1[:pp]}')
print(f'Выб. среднее = {sm:.3f}, Выб. дисперсия = {svar:.3f}')
plt.legend()
plt.show() 
