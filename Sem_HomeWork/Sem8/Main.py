# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# Программа должна выводить данные - готово
# Программа должна сохранять данные в текстовом файле - готово
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека) - готово
# Использование функций. Ваша программа не должна быть линейной
from functools import reduce

Phone_dict = {}
Second_name_dict = {}
Name_dict = {}
Patronymic = {}
Search_name_dict = {}
Search_second_name_dict = {}

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-16') as f:
        data = f.read()
    data = data.split('\n')
    data = [x.split('\t') for x in data]
    for item in data:
        if item != ['']:
            add_to_phone_dict(item[0], item[1], item[2], item[3])
    return data

def write_file(file_name):
    data = str()
    for key in Phone_dict:
        data += Second_name_dict[key] + '\t' + Name_dict[key] + '\t' + Patronymic[key] + '\t' + Phone_dict[key] + '\n'
    with open(file_name, 'w', encoding='utf-16') as f:
        f.write(data)

def new_key(phone_dict):
    if not len(phone_dict.items()):
        return 1
    else:
        return max(phone_dict.keys()) + 1

def add_to_phone_dict(second_name, name, name_patr, phone_number):
    nk = new_key(Phone_dict)
    Phone_dict[nk] = phone_number
    Second_name_dict[nk] = second_name
    Name_dict[nk] = name
    Patronymic[nk] = name_patr
    if second_name not in Search_second_name_dict:
        Search_second_name_dict[second_name] = list()
        Search_second_name_dict[second_name].append(nk)
    else:
        Search_second_name_dict[second_name].append(nk)

    if name not in Search_name_dict:
        Search_name_dict[name] = list()
        Search_name_dict[name].append(nk)
    else:
        Search_name_dict[name].append(nk)

def del_from_phone_dict(key):
    Phone_dict.pop(key)
    Second_name_dict.pop(key)
    Name_dict.pop(key)
    Patronymic.pop(key)

def print_all_phone_dict():
    for key in Phone_dict:
        print(key, '\t', Second_name_dict[key], '\t', Name_dict[key], '\t', Patronymic[key], '\t', Phone_dict[key])
    print()

def print_one_phone_dict(key):
    print(key, '\t', Second_name_dict[key], '\t', Name_dict[key], '\t', Patronymic[key], '\t', Phone_dict[key])

def find_phone_by_second_name(second_name, Search_second_name_dict):
    data = Search_second_name_dict.get(second_name)
    if data is not None:
        for key in data:
            print_one_phone_dict(key)
    else:
        print(f'{second_name} not found')

def find_phone_by_name(name, Search_name_dict):
    data = Search_name_dict.get(name)
    if data is not None:
        for key in data:
            print_one_phone_dict(key)
    else:
        print(f'{name} not found')

def add_new_line():
    second_name = input("Введите Фамилию :")
    name = input("Введите Имя :")
    name_patr = input("Введите Отчество :")
    while True:
        phone_number = input("Введите номер телефона")
        data = map(lambda x: ord(x), phone_number)
        if all(x >= 48 and x <= 57 for x in data):
            break
        else:
            print("Некорректный номер телефона")

    add_to_phone_dict(second_name, name, name_patr, phone_number)

read_data = read_file('book1.txt')
# меню выбора действий
while True:
    print("Выберите действие:")
    print("1. Добавить новую запись")
    print("2. Вывести все записи")
    print("3. Вывести записи по фамилии")
    print("4. Вывести записи по имени")
    print("5. Удалить запись")
    print("6. Выйти")
    action = input("Введите действие:")
    if action == '1':
        add_new_line()
    elif action == '2':
        print_all_phone_dict()
    elif action == '3':
        second_name = input("Введите фамилию:")
        find_phone_by_second_name(second_name, Search_second_name_dict)
    elif action == '4':
        name = input("Введите имя:")
        find_phone_by_name(name, Search_name_dict)
    elif action == '5':
        key = int(input("Введите ключ:"))
        del_from_phone_dict(key)
    elif action == '6':
        break
    else:
        print("Некорректное действие")

write_file('book2.txt')
