# Варызгин Дмитрий
# Задание 11_1

import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

# распределение Пуассона
l = [0.5, 1, 3.5]  # массив лямбд
m = 7
x = np.arange(m + 1)
for i in range(len(l)): # цикл по лямбдам
    y = st.poisson.pmf(x, l[i])
    plt.plot(x, y, label = f'При лямбда = {l[i]}')    
    plt.plot(x, y, 'o r') # точки на графике
plt.legend()
plt.show()


