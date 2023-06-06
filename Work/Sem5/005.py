# Дан список интов, повторяющихся
# элементов в списке нет.
# Нужно преобразовать это множество
# в строку, сворачивая соседние по числовому
# ряду числа в диапазоны.
str = input('Введите набор чисел: ')
some_list = [int(item) for item in str.split()]
some_list.sort()

def print_list_sorted(s_list):

    print(s_list)
    flag_list = [1 if s_list[i] == (s_list[i+1]-1) else 0 for i in range(len(s_list)-1)]
    print(flag_list)
    count = 1
    print(s_list[0], end='-')
    while count < len(s_list)-1:
        if flag_list[count] == 0:
            print(s_list[count], end=' ')
            count += 1
        elif flag_list[count] == 1 and flag_list[count-1] == 0:
            print(s_list[count], end='-')
            count += 1
        else:
            count += 1
    else:
        print(s_list[-1])

def print_list(some_list): # решение с  урока выдает не коррекнтый результат
    result_list = []
    temp_list = []
    print(some_list)
    for i in range(0, len(some_list) - 1):
        if some_list[i + 1] - some_list[i] == 1:
            temp_list.append(some_list[i])
    else:
        temp_list.append(some_list[i])
    result_list.append(temp_list)
    temp_list = []
    if temp_list:
        result_list.append(temp_list)

    if some_list[-1] - some_list[-2] == 1:
        result_list[-1].append(some_list[-1])
    else:
        result_list.append([some_list[-1]])

    print_list = []
    for i in result_list:
        if len(i) > 1:
            print_list.append(f'{i[0]}-{i[-1]}')
    else:
        print_list.append(i[0])
    print(*print_list, sep=',')


print_list_sorted(some_list)
print_list(some_list)