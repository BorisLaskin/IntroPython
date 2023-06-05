# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)

import random

some_list = [random.randint(1, 100) for i in range(10)]
other_list = [some_list[i] for i in range(1,len(some_list)) if some_list[i] > some_list[i-1]]
print(some_list)
print(other_list)