#В университет на факультеты A и B поступило равное количество студентов, 
# а на факультет C студентов поступило столько же, сколько на A и B вместе. (С = А+В)
# Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. 
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. 
# Студент сдал первую сессию. Какова вероятность, что он учится: 
# a). на факультете A б). на факультете B в). на факультете C?


# формула Байеса, А - сдал, В - факультет
# Полная вероятность: сдал студент с одного из факультетов
#т.к. число студентов на каждом факультете разная, 
# то вероятность того,что один студент учится на факультете:
# А = 1/4, В = 1/4, С = 1/2 
a = 0.8*(1/4)+0.7*(1/4)+0.9*(1/2)
#a) факультет A
p1 = 0.8*(1/4)/a
print(p1)
#a) факультет B
p2 = 0.7*(1/4)/a
print(p2)
#a) факультет C
p3 = 0.9*(1/2)/a
print(p3)