# Task 1
# Определите является ли строка записью числа.
# Подсказка: ищите как это сделать с помощью методов строк)

a = str("OOOO")
print("Строка -- "+a+" -- является записью числа?")
print(a.isdecimal(), end='\n\n')

a = str("34_78")
print("Строка -- "+a+" -- является записью числа?")
print(a.isdecimal(), end='\n\n')

a = str("1234")
print("Строка -- "+a+" -- является записью числа?")
print(a.isdecimal(), end='\n\n')

a = str("3 6")
print("Строка -- "+a+" -- является записью числа?")
print(a.isdecimal(), end='\n\n')



# Task 2
# Посчитайте сколько у вас пробелов в строке.

b = str('bpython version 0.17 on top of Python 3.6.3')
print("В строке -- '"+b+"' -- пробелов", end=': ')
print(b.count(' '), end='\n')



# Task 3
# Посчитайте сколько у вас символов точки '.' в строке.
b = str('bpython version 0.17 on top of Python 3.6.3')
print("В строке -- '"+b+"' -- точек", end=': ')
print(b.count('.'), end='\n\n')

# Task 4
# Создайте строку "Homework". Преобразуйте ее в строку длиной 100 символов, посередине которой исходное слово,
# а с обоих сторон строка заполнена пробелами. Выведите ее на экран.
c = str('Homework')
print(c.center(100,' '), end='\n\n')

# Task 5
# Сделайте первые буквы слов строки большими (upper case).
print(b.title())
print(b.capitalize())
print(b.upper())
print(b.lower())
