# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

import time
import random

# some_string = str(input()).split()
some_string = [chr(random.randint(30, 400)) for _ in range(10 ** 5)]
some_set = set(some_string)

start_time = time.perf_counter()
result = [str(item) + '_' + str(some_string.count(item)) for item in some_set]
a = (' '.join(result))
end_time = time.perf_counter()
duration1 = end_time - start_time

some_string2 = ''.join(some_string)
start_time = time.perf_counter()
count_dict = {}
for item in some_string2:
    if item not in count_dict:
        count_dict[item] = 1
    else:
        count = count_dict[item]
        count_dict[item] = count + 1
result = [str(item) + '_' + str(count_dict[item]) for item in count_dict]
end_time = time.perf_counter()
duration2 = end_time - start_time

print(duration1/duration2)
print(result)
