# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.



def print_operation_table(operation, sym, num_rows=7, num_columns=7):
    array = [[sym,] + list(i for i in range(1, num_rows+1))] + list(i for i in range(1, num_columns+1)) 
    for i in range(1, num_rows+1):
        array[i] = [array[i]]+list(map(operation, array[0][1:num_rows+1], [i]*num_columns))

    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end='\t')
        print()

flag = 1
while flag:
    symbol=str(input("Введите символ операции (+,-,*,^,/) или q для выхода : "))
    if symbol == '+':
        oper = lambda x, y: x + y
    elif symbol == '-':
        oper = lambda x, y: x - y
    elif symbol == '/':
        oper = lambda x, y: round(x / y,2)
    elif symbol == '*':
        oper = lambda x, y: x * y
    elif symbol == '^':
        oper = lambda x, y: x ** y
    elif symbol == 'q':
        flag = 0
        continue
    else:
        print("Введен неправильный символ")
        continue
    print_operation_table(oper,symbol)