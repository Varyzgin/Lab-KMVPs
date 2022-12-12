# Варызгин Дмитрий
# Задание 11_3
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

N = 1000
a = 1.5
s = 1
sigma = 6

x = np.linspace(-8, 8, N)
y = st.norm.pdf(x, a, s)
p = (1 - st.norm.cdf(sigma, a, s))
print(f'При сигма = 6 вероятность попадения за ее пределы = {p:.9f}')

plt.plot(x, st.norm.pdf(x, 0, 1), '--')
plt.plot(x, y)
plt.vlines(sigma, 0, 0.4, 'g', label='6s')
plt.legend()
plt.show()


