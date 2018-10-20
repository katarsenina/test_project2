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


def distance_two_dots(x1, y1, x2, y2):
    ddd = (x1 - x2) ** 2
    ddd += (y1 - y2) ** 2
    return math.sqrt(ddd)




if __name__ == "__main__":
    print()
