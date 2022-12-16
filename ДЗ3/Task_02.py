#В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
# Какова вероятность того, что 3 мяча белые?

import numpy as np
from math import factorial

def combinations (n, k):
    return np.math.factorial(n) // (np.math.factorial(k)*np.math.factorial(n-k))

# Общее число исходов
n = combinations(8, 2) * combinations(12, 4) # 2 мяча из 1го ящика И 4мяча из 2го ящика
# Благоприятные исходы
m = combinations (5, 2)*combinations(5, 1)+combinations(5, 1)*combinations(5, 2)
# 2бел (1я) И 1бел (2я) ИЛИ 1бел (1я) И 2бел (2я)
P = m/n
print(P)