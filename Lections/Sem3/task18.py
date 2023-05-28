""" Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X """

# Задание решил чуть усложнить

import random
import math
number = int(input("Сколько чисел сгенерировать?"))
if number > 0:
    list_1 = []
    for i in range(number):
        list_1.append(int(10*random.random()))
    print(list_1)
    task = float(input("какое число искать (тип float)?"))

    list_2 = [0] * number
    for i in range(len(list_1)):
        list_2[i]=abs(list_1[i]-task)


    temp = min(list_2)
    res = [i for i, j in enumerate(list_2) if j == temp] #google в помощь https://translated.turbopages.org/proxy_u/en-ru.ru.55990016-64553520-92785d72-74722d776562/https/www.geeksforgeeks.org/python-find-the-index-of-minimum-element-in-list/
    
    # Printing result
    print(f"Самый близкий это элемент {list_1[res[0]]}")
else:
    print("мало")
