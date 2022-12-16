#1. Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

import numpy as np
from math import factorial

def combinations (n, k):
    return np.math.factorial(n) // (np.math.factorial(k)*np.math.factorial(n-k))

#подпункт а
good_combinations = combinations(13, 4)
all_combinations = combinations(52, 4)
P1 = good_combinations / all_combinations

print('Задание 1')
print(f'a) {P1}')

#подпукт б
aces = combinations(4, 1)
notaces = combinations(48, 3)
gc = aces*notaces
P2 = gc / all_combinations

print(f'б) {P2}')

