def counting_sort_unstable(L):

    count = [0 for _ in range(max(L) + 1)]
    for element in L:
        count[element] += 1
    
    res = []
    for element in range(len(count)):
        for occurrences in range(count[element]):
            res.append(element)

    return res


def counting_sort_stable(L):
    
    count = [0 for _ in range(max(L) + 1)]
    for element in L:
        count[element] += 1
    
    positions = [0 for _ in range(max(L) + 1)]
    for i in range(1, len(positions)):
        positions[i] = positions[i-1] + count[i-1]
    
    res = [None for _ in range(len(L))]
    for i in range(len(res)):
        res[positions[L[i]]] = L[i]
        positions[L[i]] += 1
    
    return res


print('unstable')
print(counting_sort_unstable([1,2,3,4,5]))
print(counting_sort_unstable([5,4,3,2,1]))
print(counting_sort_unstable([1,5,100,3,5]))
print('stable')
print(counting_sort_stable([1,2,3,4,5]))
print(counting_sort_stable([5,4,3,2,1]))
print(counting_sort_stable([1,5,100,3,5]))
