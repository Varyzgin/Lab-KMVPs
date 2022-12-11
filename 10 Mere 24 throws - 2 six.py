# Варызгин Дмитрий
# Задание 10_2 24 * 2
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np
np.set_printoptions(precision=3)

# Биномиальный закон распределения
N = 1000  # серии
k = 2  # число кубиков
n = 24  # число бросков

p = 1 / (6 ** k)  # шанс выпадения шестерок на 2 кубиках

x = np.arange(0, n + 1)
y = st.binom.pmf(x, n, p)
print(f'{1 - y[0]} - Вероятность выпадения хотя бы 1 раз пары шесток на 2 кубиках при 24х бросках')
plt.plot(x, y, color='blue')
plt.vlines(x, 0, y, color='blue')
plt.plot(x, y, 'o r', label='С помощью scipy')
plt.legend()
plt.show()


