# Варызгин Дмитрий (2 группа ФИИТ)
# Задание 6_1

k = 25
m = 19
a = 5
c = 3
x0 = 7
# попытался через рекурсию
# def x(i):
#     if k == 0: return 0
#     else:
#         k-=1
#         return (a * x(i - 1) + c) % m
x = [0] * (k + 1)
x[0] = x0
for i in range(k):
    x[i + 1] = (a * x[i] + c) % m
print(x)
