# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
x=[]
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        x.append(1)
        return 1
    else:
        r = fibonacci(n - 1) + fibonacci(n - 2)
        return r
    x.append(r)

print(fibonacci(int(input('Введите номер последовательности Фибоначчи: '))))
print(x[:-1])