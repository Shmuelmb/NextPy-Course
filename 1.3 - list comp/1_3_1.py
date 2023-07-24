def intersection(list_1, list_2):
    logic = set([x for x in list_1 for y in list_2 if x == y])
    return list(logic)


print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
