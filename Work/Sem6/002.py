def issimple(number,divisor):
    if divisor == 1 or number == 1:
        return True
    elif number%divisor != 0:
        return issimple(number,divisor-1)
    else:
        return False



number  = int(input("ВВедите число "))
print(f"число {number} "+ ('простое' if issimple(number,int(number**0.5)) else 'непростое'))