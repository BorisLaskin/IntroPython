# list_1 = [] # Создание пустого списка
# list_2 = list() # Создание пустого списка
# list_1 = [7, 9, 11, 'safaf', 15, 17]

# for item in list_1:
#     print(item)
#     print(list_1[0])

# print(*list_1)
# print(len(list_1))

# list_2 = [1,5]
# print(list_2)
# list_2.append(9)
# print(list_2)


# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# print(list_1.insert(2, 11))
# print(list_1)
# list_1.insert(10, 11)
# print(list_1)

t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = 1, 5, 3 
print(type(t))
print(t[1])
t = (1)
print(type(t))
t = (28, 9, 1990)
print(t) # (28, 9, 1990)
print(type(t)) # <class 'tuple'>
t=list(t) 
print(t) # [28, 9, 1990]
print(type(t)) #<class 'list'>

t1=(12,'ddsg',213)
print(t1)

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up']) # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
print(dictionary)

for (k,v) in dictionary.items():
    print(k,v)
    print(type((k,v)),type(v))

print(dictionary.items()) #список кортежей

print(type(dictionary))