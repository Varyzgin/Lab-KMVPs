# Варызгин Дмитрий
# Модель инфекции

import time
import numpy as np
import matplotlib.pyplot as plt

# все для графика (параметры)
T = 100 # дней
n = 100 # число точек
m = T / n # шаг

# константы:
g = 1 / 21 # гамма
b = 5 * g # бета
N = 1440 # число людей (в тыс.)
r = b - g
K = r * N / b

# массивы
t = [0] * n # время
I = [0] * n # инфицированные
I[0] = 1 # начальное условие
dI = [0] * n # производная
    
for i in range(n - 1):
    I[i + 1] = r * I[i] * (1 - I[i] / K) * m + I[i]
    dI[i + 1] = r * I[i] * (1 - I[i] / K) * 5
    t[i + 1] = (t[i] + m)

plt.xlabel('Время')
plt.ylabel('Люди, в тыс. ч.')
plt.plot(t, I, color = 'red', label = 'Число инфицированных')
plt.plot(t, dI, color = 'orange', label = 'Производная')
plt.legend()
plt.show()

