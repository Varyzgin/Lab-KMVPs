# Варызгин Дмитрий (2 группа ФИИТ)
# Задание 7_2
import matplotlib.pyplot as plt
import numpy as np
# параметры
N = 2000
S = 6 # серия
a = 1 
b = 2
# служебные массивы
z = []
color = ['b'] * N
I = 1 / 6
# задаем пространство и функ. зависимость
x = np.linspace(a, b, N)
def f(x): return - x ** 2 + 3 * x - 2
y = f(x)
plt.plot(x, y, color = 'red')
# заполнение точками
x = np.random.uniform(a, b, N)
y = np.random.uniform(0, np.max(f(x)), N)
for i in range(N): # покрас
    if (y[i] < f(x[i])):
        z.append(x[i])
        color[i] = 'green'
    else: color[i] = 'grey'  
plt.scatter(x, y, c = color, s = 1)
plt.show()
# таблица
AI1 = [] # для построения графика ошибок
AI2 = []
print('N     |Инт-ал|Error1|Error2')
for s in range(1, S):
    N = 10 ** s # изменяемый массив точек

    x = np.random.uniform(a, b, N) # задаем пространство
    m1 = sum(f(x)) 
    I1 = ((b - a) / N) * m1 # считаем площадь (интеграл): ширина столбика (множество / число точек) *
    E1 = abs(I - I1) # * ставим столбики друг над другом и считаем суммарную высоту
    AI1.append(E1) 

    x = np.random.uniform(a, b, N)
    y = np.random.uniform(0, np.max(f(x)), N)
    m2 = sum(y < f(x)) # сумма точек под кривой ~= площади
    # S прямоугольника к S под параболой = I от площади к I искомому
    # ниже выражение: I искомый = S под параболой * I от площади / S прямоуг
    # а площадь некой области - количество точек в ней
    I2 = ((b - a) * (np.max(f(x)) - 0)) * m2 / N
    E2 = abs(I - I2)
    AI2.append(E2)
    print(f'10 ^ {s}|{I:.4f}|{E1:.4f}|{E2:.4f}') # :.4f - показать 4 знака после запятой
x1 = np.arange(S - 1)
plt.plot(x1, AI1, 'o r', label = 'Error by building rectangles')
plt.plot(x1, AI2, 'o b', label = 'Error by counting points')
plt.legend()
plt.show()
