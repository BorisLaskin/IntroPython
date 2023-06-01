""" Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке (пара-ра-рам рам-пам-папам па-ра-па-да)"""
import numpy as np
def checkfunc1(string,vowels):# Базовое решение
    fraze_list=[item.split('-') for item in string.lower().split()]

    if len(fraze_list)<=1:
        return False
    else:
        res = [[0 for j in range(len(fraze_list[i]))] for i in range(len(fraze_list))]

        for item in vowels:
            for i in range(len(fraze_list)):
                fraze = fraze_list[i]
                for j in range(len(fraze)):
                    res[i][j]+=fraze[j].count(item)

        print("количество слогов в слове")
        print(res)
        res=list(map(lambda x: sum(x),res))
        print("количество слогов в фразе")
        print(res)
        return True if all(x == res[0] for x in res) else False

def checkfunc2(string,vowels):
    fraze_list=string.lower().split()
    if len(fraze_list)<=1:
        return False
    else:
        res = [0 for i in range(len(fraze_list))]
        res = np.array(res)
        for item in vowels:
            arr=np.array(list(map(lambda x: x.count(item),fraze_list)))
            res+=arr
        print("количество слогов в фразе")
        print(res)
        return True if all(x == res[0] for x in res) else False

def checkfunc3(string,vowels):
    fraze_list=string.lower().split()
    if len(fraze_list)<=1:
        return False
    else:
        res = [0 for i in range(len(fraze_list))]
        for item in vowels[0]:
            arr=(list(map(lambda x: x.count(item),fraze_list)))
            res=[res[i]+arr[i] for i in range(len(arr))]
        print("количество слогов в фразе")
        print(res)
        return True if all(x == res[0] for x in res) else False
    
string = str(input("Введите вашу кричалку: "))
vowels = ['а', 'о', 'у', 'и', 'ы', 'э', 'е', 'ё', 'ю', 'я']
# checkfunc(string, vowels)
print("Парам пам-пам" if checkfunc1(string, vowels) else "Пам парам")
print("Парам пам-пам" if checkfunc2(string, vowels) else "Пам парам")
print("Парам пам-пам" if checkfunc3(string, vowels) else "Пам парам")