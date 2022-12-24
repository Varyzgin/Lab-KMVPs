# Варызгин Дмитрий (2 группа ФИИТ)
# Задание 7_1
import matplotlib.pyplot as plt
import numpy as np
# параметры
N = 5000
S = 6 # серия
a = 0
b = 1
# служебные массивы
z = []
color = ['b'] * N
# задаем пространство и функ. зависимость
x = np.linspace(a, b, N)
def f(x): return np.sqrt(1 - x ** 2)
y = f(x)
plt.plot(x, y, color = 'red')
# заполнение точками
x = np.random.uniform(a, b, N)
y = np.random.uniform(a, b, N)
for i in range(N): # покрас
    if (y[i] < f(x[i])):
        z.append(x[i])
        color[i] = 'green'
    else: color[i] = 'grey'  
plt.scatter(x, y, c = color, s = 1)

print(f'pi = {(4 * len(z)) / N}')
plt.show()


