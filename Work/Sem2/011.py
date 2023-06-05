# Александр LyraX: 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи
# является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
number = int(input("Введите число: "))
last_number = 1
pre_last_number = 1
current_index = 2
current_number = 1
while current_number <= number:
    current_number = last_number + pre_last_number
    # print(current_number)
    pre_last_number = last_number
    last_number = current_number
    current_index += 1

    if current_number == number:
        print(current_index)
        break
else:
    print(-1)
