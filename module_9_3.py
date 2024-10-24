first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y)]

second_result = [len(first[i]) == len(second[i])  for i in range(min(len(first), len(second)))]

"""Эксперимент"""
# second_result = [bool(x) if len(x) == len(y) else len(x) == len(y) for x, y in zip(first, second)]
#Почему прописывая одинаковое условие как после if, так и после else - на выходе получаем разные булевые значения.
#Если мы оставляем одно условие после цикла получаем только одно значение, а не три?

print(list(first_result))
print(list(second_result))
