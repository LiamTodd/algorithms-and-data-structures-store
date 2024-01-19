def insertion_sort(L):
    for i in range(1, len(L)):
        current = L[i]
        j = i - 1
        while j >= 0 and current < L[j]:
            # shift j'th element up and update j
            L[j + 1] = L[j]
            j -= 1

        # reinsert
        L[j + 1] = current

    return L


print(insertion_sort([1, 2, 3, 4, 5]))
print(insertion_sort([5, 4, 3, 2, 1]))
