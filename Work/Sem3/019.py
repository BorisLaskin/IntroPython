# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
import random

some_list = [random.randint(1, 100) for _ in range(10)]
print(some_list)
sdvig = int(input("Введите длину циклического сдвига: "))

new_list = some_list[-sdvig:] + some_list[:-sdvig]
print(new_list)




