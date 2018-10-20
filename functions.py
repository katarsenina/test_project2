def enter_word():
    ''' Ввод слова без пробелов всередине и других небуквенных символов.
     str -> str'''
    while True:
        s = input("Enter word: ").strip()
        if s.isalpha():
            return s



def join_lists(list1, list2, list3):
    '''Соединяет 3 списка  одинакового типа в один
    (list1, list2, list3) -> list'''
    assert type(list1) is type(list2) is type(list3)
    join_lists = list1 + list2 + list3
    return join_lists



class Person:
# дальше конструктор
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        '''Метод для того, чтобы научить print выводить информацию об объекте'''
        return "<Person objec: name = {} {}>".format(self.name, self.surname)

    def fullname(self):
        '''Возвращает имя с фамилией'''
        print(name + surname, sep=' ')
        return "{} {}".format(self.name, self.surname)

    def get_older(self, years=0):
        '''Увеличивает возраст self.age на years лет'''
        self.age += years
#        return self.age


if __name__ == "__main__":


    a = Person("Jack", "Vorobay", 220)
    print(a)
    print(a.fullname())
    print(a.get_older(7))
    s = str(a)
    print(s)


