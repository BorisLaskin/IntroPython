def is_even1(array):
    out = list()
    for item in array:
        if item%2==0:
            out.append((item,item**2))
    return out

is_even2 = lambda array1: [(i,i*i) for i in array1 if i%2==0]
is_even3 = lambda array: list(map(lambda x: (x,x*x),filter(lambda x: x%2==0,array)))
a=[1, 2, 4, 5,6,7,67,55,56]
print(*is_even1(a))
print(*is_even2(a))
print(*is_even3(a))
print(type(is_even2))
