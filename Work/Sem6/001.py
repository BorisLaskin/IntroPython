# определить является ли строка полиндромом с помощью рекурсии
def ispolyndrome(letter):
    if len(letter) == 0:
        return True
    elif letter[0] == letter[-1]:
        return ispolyndrome(letter[1:-1])
    else:
        return False

str = input("введите слово: ")
print("yes" if ispolyndrome(str) else "no")