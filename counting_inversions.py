def sort_and_count(L):
    lo = 0
    hi = len(L)
    inversions = 0
    if hi > lo + 1:
        mid = (lo + hi) // 2
        left, inversions_l = sort_and_count(L[lo:mid])
        right, inversions_h = sort_and_count(L[mid:hi])
        L, inversions_s = merge_and_count(left, right)
        inversions = inversions_s + inversions_l + inversions_h
    return L, inversions

def merge_and_count(left, right):
    res = []
    i = 0
    j = 0
    split_inversions = 0
    while i < len(left) or j < len(right): # while there are elements to be merged
        if j >= len(right) or i < len(left) and left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            split_inversions += len(left) - i
    return res, split_inversions


print(sort_and_count([1,2,3,4,5]))
print(sort_and_count([5,4,3,2,1]))