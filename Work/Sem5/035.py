# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def prog(some_list):
    max_value = max(some_list)
    min_value = min(some_list)
    new_list = list()
    for item in some_list:
        if item == max_value:
            new_list.append(min_value)
        else:
            new_list.append(item)
    return new_list

str = input('Введите набор оценок: ')
some_list = [int(item) for item in str.split()]
print(prog(some_list))