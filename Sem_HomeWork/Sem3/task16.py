""" Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X """

#Задание решил чуть усложнить

import random
number = int(input("Сколько чисел сгенерировать?"))
if number > 0:
    list_1=[]
    for i in range(number):
        list_1.append(int(10*random.random()))
    print(list_1)
    task = int(input("какое число искать?"))
    counter=0
    for item in list_1:
        if item == task:
            counter +=1

    print(f"{task} входит в {list_1} {counter} раз")
else:
    print("мало")
