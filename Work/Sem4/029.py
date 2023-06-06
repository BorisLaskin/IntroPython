# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
# n = int(input())
# if max_number > n:
# max_number = n
# print(max_number)
# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
# n = int(input())
# if max_number < n:
# n = max_number
# print(n)
# Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”.
# Ваня:
n = int(input())
max_number = n  #1
while n != 0:
    n = int(input())
    if max_number < n: #2
        max_number = n
print(max_number)
# Петя:
n = int(input())
max_number = n  #4
while n != 0: #1
    n = int(input())
    if max_number < n:
        max_number = n #2
print(max_number) #3