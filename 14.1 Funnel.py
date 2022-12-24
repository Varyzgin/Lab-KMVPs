# Варызгин Дмитрий
# Задание 14_1
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

n = 50
fi = st.norm.rvs(0, 1, n)
x = np.arange(n)
print(f'Среднее = {np.mean(fi):.2f}, Дисперсия = {np.var(fi):.2f}, Ассиметрия = {st.skew(fi):.2f}')
plt.plot(x, fi, 'o')
plt.show()
plt.hist(fi, density=True)
plt.show()

