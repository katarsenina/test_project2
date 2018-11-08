# Задание 2
# Задание из класса «Записываем “Number: строка из файла” из одного файла в другой»:
# 1. Кто не успел доделываем / тем, кто успел: воспользуйтесь другим способом для записи в файл
#  (кто сделал с помощью методов – делают с помощью print,
# кто сделал с помощью print – делают с помощью методов)
# 2. Воспользуйтесь менеджером контекста для файла (with … as), в который вы записываете информацию.

"""1"""
first_file = open('song.txt')
output_file = open('count_lines.txt', 'w')
i = 0
for line in first_file:
  i += 1
  print( "Number:", i, line, file=output_file)
first_file.close()
output_file.close()


"""2"""
i = 0
with open('new_file_1.txt', 'w') as n:
    for line in open('song.txt'):
        i += 1
        n.write("Number "+str(i)+": "+line)