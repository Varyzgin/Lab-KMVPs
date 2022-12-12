# Варызгин Дмитрий (2 группа ФИИТ)
# Задание 9_2

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

# изменяемые параметры
N = 10000
a = 0
b = 6
l = 1
def f(x): return l * np.exp(-l * x) # задание плотности распределения

# набор для реализации
X = np.linspace(a, b, N) # линейное пространство
x = np.random.uniform(a, b, N) # рандомные точки
y = np.random.uniform(0, np.max(f(X)), N)
ksi = [] # массив точек по методу Неймана
color = ['b'] * N # массив выделяемых цветом точек
kl = 1 + int(np.log2(N)) # формула Стерджеса для к-ва столбцов гистограммы
k = 0 # считаем попавшие под график точки

for i in range(N):
    if x[i] < b and y[i] < f(x[i]):
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
plt.scatter(x, y, c = color, s = 0.25) # точечки
plt.plot(X, f(X), color = 'orange', linestyle = '--', linewidth = 3, label = 'f распределения')
plt.plot(sorted(ksi), F, color = 'red', linewidth = 2, label = 'F распределения')
plt.xlabel('X')
plt.legend()
plt.show()

# сравнение с scipy
plt.hist(ksi, kl, density = True, color = 'lightblue', edgecolor = 'black')
ys = st.expon.pdf(X, scale = 1 / l)
plt.plot(X, ys, color = 'red')
plt.show()