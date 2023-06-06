# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

n1, n2 = random.randint(10, 20), random.randint(10, 20)
s_list1 = [random.randint(1, 10) for i in range(n1)]
s_list2 = [random.randint(1, 10) for i in range(n2)]
s_set = set(s_list1).intersection(set(s_list2))

print(s_list1)
print(s_list2)
res=list(s_set)
print(res.sort() if res.sort() is not None else res)
