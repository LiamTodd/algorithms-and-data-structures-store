def partition(L, pivot):
    left = []
    right = []
    equivalent = []
    for element in L:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            equivalent.append(element)
    return left + equivalent + right


print(partition([1, 3, 6, 3, 1, 3, 8, 1, 9, 8, 6, 2, 1], 4))
