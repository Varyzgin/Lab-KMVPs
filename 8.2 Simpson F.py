# Варызгин Дмитрий (2 группа ФИИТ)
# Задание 8_2

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

# изменяемые параметры
N = 5000
a = 0
b = 1

def f1(x): return x # задание плотности распределения
def f2(x): return 2 * b - x # задание плотности распределения

# набор для реализации
X1 = np.linspace(a, b, N) # линейное пространство
X2 = np.linspace(b, 2 * b, N) # линейное пространство
x = np.random.uniform(a, 2 * b, N) # рандомные точки
y = np.random.uniform(0, np.max(f1(X1)), N)
ksi = [] # массив точек по методу Неймана
color = ['b'] * N # массив выделяемых цветом точек
kl = 1 + int(np.log2(N)) # формула Стерджеса для к-ва столбцов гистограммы
k = 0 # считаем попавшие под график точки

for i in range(N):
    if (x[i] < b and y[i] < f1(x[i])) or (x[i] > b and y[i] < f2(x[i])):
        ksi.append(x[i]) # кладем точку в массив Неймана (строим случайную величину)
        color[i] = 'green' # красим эту точку в зеленый
        k += 1
    else: color[i] = 'grey'
F = np.linspace(0, 1, k) # строим функцию распределения по колличеству нужных точек

# характеристики случайной величины
print(f'Выборочное среднее = {np.mean(ksi)}')
print(f'Выборочная дисперсия = {np.var(ksi)}')
print(f'Выборочное ст. отклонение = {np.std(ksi)}')

# рисование
plt.hist(ksi, kl, density = True, color = 'lightblue', edgecolor = 'black') # гистограмма
plt.scatter(x, y, c = color, s = 0.5) # точечки
plt.plot(X1, f1(X1), color = 'orange', linestyle = '--', linewidth = 3, label = 'f распределения')
plt.plot(X2, f2(X2), color = 'orange', linestyle = '--', linewidth = 3)
plt.plot(sorted(ksi), F, color = 'red', linewidth = 2, label = 'F распределения')
plt.xlabel('X')
plt.legend()
plt.show()