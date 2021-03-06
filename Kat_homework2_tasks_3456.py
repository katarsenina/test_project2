# Задание 3
# Дано целое число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарём, год является високосным, если его номер кратен 4,
# но не кратен 100, а также если он кратен 400.

b = 2018
if b % 4 == 0 or b % 400 == 0 and b % 100 > 0:
    print(str(b) + ' YES')
else:
    print(str(b) + ' NO')


# Задание 4
# Даны три числа a, b, c. Определите, существует ли треугольник с такими сторонами.
# Если треугольник существует, выведите строку YES, иначе выведите строку NO.

a, b, c = 10, 1, 9
if a + b > c and a + c > b and b + c > a:
    print('Yes')
else:
    print('No')

# Задание 5
# Дано три числа. Упорядочите их в порядке возрастания.
# Программа должна считывать три числа a, b, c, затем программа должна менять их значения так,
# чтобы стали выполнены условия a <= b <= c, затем программа выводит тройку a, b, c.
# Дополнительные ограничения: нельзя использовать дополнительные переменные.

# a, b, c = 5, 0, 0
# a, b, c = 5, 5, 0
# a, b, c = 1, 4, 5
# a, b, c = 5, 0, 4
# a, b, c = 1, 3, 2
# a, b, c = 1, 0, 2
a, b, c = 2, 5, 4

if a <= b <= c:
    a, b, c = a, b, c
    print('A', a, b, c)
elif a > b >= c:
    a, b, c = c, b, a
    print('B', a, b, c)
elif a > b <= c:
    a, b, c = b, a, c
    print('C', a, b, c)
elif a >= c < b:
    a, b, c = c, a, b
    print('D', a, b, c)
elif a < c < b:
    a, b, c = a, c, b
    print('F', a, b, c)
else:
    print('Unknown variant')


# Задание 6
# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).