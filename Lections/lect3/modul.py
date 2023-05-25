def myabs(args):
    list1=list()
    for item in args:
        if item>=0:
            list1.append(item)
        else:
            list1.append(-item)
    return list1

# def mymin(args):
#     min=args[0]
#     for item in args:
#         if item<min:
#             min= item
#     return min