# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
def same_by(charac, objects):
    return len(list(filter(charac, objects))) == len(objects)


some_list = list(range(0, 10, 2))
print(same_by(lambda x: x % 2 == 0, some_list))

def test(**kwargs):
    print(type(kwargs))
    print(kwargs)

test(a=1,b=2,c=4,e=5)