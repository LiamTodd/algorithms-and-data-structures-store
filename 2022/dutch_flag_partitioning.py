def partition(L, pivot_index):
    pivot = L[pivot_index]
    j = 0
    lo_mid_boundary = 0
    hi_mid_boundary = len(L) - 1
    while j <= hi_mid_boundary:
        if L[j] < pivot:  # blue case
            swap(L, j, lo_mid_boundary)
            lo_mid_boundary += 1
            j += 1
        elif L[j] > pivot:  # red case
            swap(L, j, hi_mid_boundary)
            hi_mid_boundary -= 1
        else:  # white case
            j += 1
    return L

def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp


print(partition([2,8,6,4,1,7,3,5], 3))