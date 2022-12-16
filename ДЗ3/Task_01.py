# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. 
# Посчитать (желательно без использования статистических методов наподобие std, var, mean) 
# среднее арифметическое, 
# среднее квадратичное отклонение, 
# смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy

list1 = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
# среднее арифметическое
a = sum (list1) / len (list1)
print (f'Среднее арифметическое = {a}')
# смещенные дисперсия и ско
s = sum (map(lambda x: (x-a)**2, list1)) #сумма квадратов разницы элемента и среднего значения
disp = s/len(list1) #дисперсия, смещенная
b = numpy.sqrt (disp) #ско
print(f'Дисперсия, смещенная {disp}')
print (f'СКО, смещенное {b}')
# print(numpy.var(list1))
#print(numpy.std(list1))
# несмещенные дисперсия и ско
disp2 = s/(len(list1)-1) #дисперсия, несмещенная
b2 = numpy.sqrt (disp2) #ско
print((f'Дисперсия, несмещенная {disp2}'))
print (f'СКО, несмещенное {b2}')
# print(numpy.var(list1, ddof=1))
# print(numpy.std(list1, ddof=1))