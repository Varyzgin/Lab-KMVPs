# Варызгин Дмитрий
# Задание 12_2
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

# Параметры
a = 0
b = 1
N = 10000
k = 6

# Служебные формулы
kl = 1 + int(np.log2(N))

# Считаем и выводим суммы от 1 до 6 одинаково распределенных сл. вел.
ksi = [0] * k
nu = [0] * k
for i in range(1, k):
    ksi[i] = np.random.uniform(a, b, N)
    nu[i] = ksi[i] + nu[i - 1]
    plt.hist(nu[i], kl, density=True, edgecolor="black")

plt.show()

# Линейно преобразовываем получившееся распределение к нормальному
eta = np.sqrt(12 / i) * nu[i] - np.sqrt(3 * i)
p = plt.hist(eta, kl, density=True, edgecolor="black", color="gray")
mn = np.min(p[1])
mx = np.max(p[1])
x = np.linspace(mn, mx, kl, endpoint=False) + (mx - mn) / kl / 2
plt.plot(x, p[0], color="red", label="Линейно преобразованное распределение")

# SciPy распределение
y1 = sorted(eta)
psi = st.norm.pdf(y1, 0, 1)
plt.plot(y1, psi, color="orange", label="SciPy распределение")

plt.legend()
plt.show()

print(f'Среднее = {np.mean(p[0]):.3f}, Дисперсия = {np.var(p[0]):.3f}')
print(f'Ассиметрия = {st.skew(p[0]):.3f}, Эксцесс = {st.kurtosis(p[0]):.3f}')

