def partition(L, pivot_index):
    pivot = L[pivot_index]
    swap(L, 0, pivot_index)
    L_bad = 1
    R_bad = len(L) - 1
    while L_bad <= R_bad:
        while L_bad <= R_bad and L[L_bad] <= pivot:
            L_bad += 1
        while L_bad <= R_bad and L[R_bad] > pivot:
            R_bad -= 1
        if L_bad <= R_bad:
            swap(L, L_bad, R_bad)
    swap(L, R_bad, 0)
    return L
        
def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


print(partition([2,8,6,4,1,7,3,5], 3))