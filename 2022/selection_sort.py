def selection_sort(L):
    for i in range(len(L)):
        min_index = get_min_index(L, i)
        if i != min_index:
            swap(L, i, min_index)
    return L


def get_min_index(L, start_index):
    min_index = start_index
    for i in range(start_index + 1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


print(selection_sort([1, 2, 3, 4, 5]))
print(selection_sort([5, 4, 3, 2, 1]))
