def quickselect(L, k):
    return quickselect_aux(L, 0, len(L), k)

def quickselect_aux(L, lo, hi, k):
    if hi > lo:
        pivot = median_of_medians(L, lo, hi)
        boundaries = dutch_flag_partition(L, lo, hi, pivot)
        low_boundary = boundaries[0]
        high_boundary = boundaries[1]
        if k < low_boundary:
            return quickselect_aux(L, lo, low_boundary, k)
        elif k > high_boundary:
            return quickselect_aux(L, high_boundary, hi, k)
        else:
            return L[k]
    else:
        return L[k]

def dutch_flag_partition(L, lo, hi, pivot):
    low_boundary = lo
    j = lo
    high_boundary = hi - 1
    while j <= high_boundary:
        if L[j] < pivot:
            swap(L, low_boundary, j)
            low_boundary += 1
            j += 1
        elif L[j] > pivot:
            swap(L, j, high_boundary)
            high_boundary -= 1
        else:
            j += 1
    return low_boundary, high_boundary

def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp
    
def median_of_medians(L, lo, hi):
    if lo - hi <= 5:
        return median_of_sublist(L, lo, hi)
    else:
        medians = []
        for i in range(lo, hi, 5):
            j = min(i+5, hi)
            median = median_of_sublist(L, i, j)
            medians.append(median)
        n = len(medians)
        return quickselect_aux(medians, 0, n, n//2)

def median_of_sublist(L, lo, hi):
    extracted = [L[i] for i in range(lo, hi)]
    extracted.sort()
    return extracted[len(extracted)//2]

print(quickselect([1,2,3,4,5], 5//2))
