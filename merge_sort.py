def merge_sort(L):
    lo = 0
    hi = len(L)
    if hi > lo + 1:
        mid = (lo + hi) // 2
        left = merge_sort(L[lo:mid])
        right = merge_sort(L[mid:hi])
        L = merge(left, right)
    return L

def merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) or j < len(right): # while there are elements to be merged
        if j >= len(right) or i < len(left) and left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res

print(merge_sort([1,2,3,4,5]))
print(merge_sort([5,4,3,2,1]))
