# Варызгин Дмитрий
# Задание 2_2

import time
import numpy as np
import matplotlib.pyplot as plt

a = 15 # начало на графике
s = 16 # количество точек (значений функции)
k = 7

atl1 = [0] * s # массив времен при реализации через факториал (заполнен нулями)
atl2 = [0] * s # массив времен при реализации через факториал с сокращением (заполнен нулями)
atf = [0] * s # массив времен при реализации функциями (заполнен нулями)

def Cf(n, k): # задание функции сочетаний n по k
    if k == 0: return 1
    elif k > n: return 0
    else: return Cf(n - 1, k) + Cf(n - 1, k - 1)
def l(h): # рассчет факториала
    r = 1
    for i in range(1, h + 1): r *= i
    return r
def Cl1(n, k): # просто через определение сочетаний из n по k
    return l(n) / (l(k) * l(n - k))
def Cl2(n, k):  # мой эффективный алгоритм, который не считает три факториала,
                # а считает произведения сверху и снизу дроби причем существует 
                # выбор max, чтобы разграничить, что сокращается: n-k! или k! с n!
    r = 1
    for i in range(max(n - k + 1, k + 1), n + 1): r *= i
    r /= l(k)
    return r
    
for j in range(s):
    n = a + j
    
    tf = time.time() # засекаем время
    print('C(', n, ',', k, ') =', Cf(n, k))   
    atf[j] = time.time() - tf # останавливаем
    print('Время функционального рассчета =', atf[j], 'c.')

    tl1 = time.time() # засекаем время
    c = l(n) / (l(k) * l(n - k))
    print('C(', n, ',', k, ') =', c)  
    atl1[j] = time.time() - tl1 # останавливаем
    print('Время рассчета через факториал =', atl1[j], 'c.')
    
    tl2 = time.time() # засекаем время
    print('C(', n, ',', k, ') =', Cl2(n, k))  
    atl2[j] = time.time() - tl2 # останавливаем
    print('Время рассчета через факториал с сокращением =', atl2[j], 'c.')
    
    print('')

nn = np.arange(a, a + s)
plt.plot(nn, atf, color = 'red', label = 'При рассчете с помощью функции')
plt.plot(nn, atl1, color = 'green', label = 'При рассчете через факториал')
plt.plot(nn, atl2, color = 'blue', label = 'При рассчете через факториал с сокращением')
plt.legend()
plt.show()

