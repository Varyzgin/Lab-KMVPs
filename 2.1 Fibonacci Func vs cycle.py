# Варызгин Дмитрий
# Задание 2_1

import time
import numpy as np
import matplotlib.pyplot as plt

a = 20 # начало на графике
s = 17 # количество точек (значений функции)
atc = [0] * s # массив времен при реализации циклами (заполнен нулями)
atf = [0] * s # массив времен при реализации функциями (заполнен нулями)

def f(n): # задание функции Фиббоначи
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n - 1) + f(n - 2)
    
for j in range(s):
    n = a + j
    
    tf = time.time() # засекаем время
    print('n =', n, 'f =', f(n - 1))   
    atf[j] = time.time() - tf # останавливаем
    print('Время функционального рассчета =', atf[j], 'c.')

    tc = time.time() # засекаем время
    F = [0] * n # массив нулей
    for i in range (2, n):
        F[i] = F[i - 1] + F[i - 2]
    print('n =', n, 'f =', F[n - 1])  
    atc[j] = time.time() - tc # останавливаем
    print('Время цикличного рассчета =', atc[j], 'c.')
    
    print('')

nn = np.arange(a, a + s)
plt.plot(nn, atf, color = 'red', label = 'При рассчете с помощью функции')
plt.plot(nn, atc, color = 'green', label = 'При рассчете с помощью цикла')
plt.legend()
plt.show()

