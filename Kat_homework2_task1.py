# Задание 1
# Определите является ли строка записью числа.
# Подсказка: ищите как это сделать с помощью методов строк)

a = str("OOOO")
print("Строка -- "+a+" -- является записью числа?")
print(a.isdecimal())

a = str("34_78")
print("Строка -- "+a+" -- является записью числа?")
print(a.isdecimal())

a = str("1234")
print("Строка -- "+a+" -- является записью числа?")
print(a.isdecimal())

a = str("3 6")
print("Строка -- "+a+" -- является записью числа?")
print(a.isdecimal())
