# Варызгин Дмитрий
# Задание 16_1

import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

y = np.array([0.492, 0.462, 0.350, 0.317, 0.340, 0.351, 0.368, 0.381], float)
x = np.array([0.213, 0.171, 0.291, 0.309, 0.317, 0.362, 0.351, 0.362], float)

kс = np.corrcoef(x, y)
res = st.linregress(x, y)

plt.title(f'Корреляция k = {kс[0][1]}')
plt.plot(x, y, 'o r', label='Исходные данные')
plt.plot(x, res.intercept + res.slope * x, 'g', label='Линия')
plt.legend()
plt.show()

