def solution_BAD(a, m, k):
    # works, but too slow
    count = 0
    # iterate over subarrays
    for start_index in range(0, len(a) - m + 1):
        flag = True
        # iterate through pairings in each subarray, with break conditions
        for i in range(start_index, start_index + m - 1):
            for j in range(i + 1, start_index + m):
                if i != j and a[i] + a[j] == k:
                    count += 1
                    flag = False
                if flag is False:
                    break
            if flag is False:
                break
    return count


def solution_OK(a, m, k):
    # works, still too slow

    # find all pairings which are at most 'm' elements apart which sum to give k
    # determine index length between them
    # determine how many subarrays each pairing will belong to

    subarrays = [
        0 for _ in range(len(a) - m + 1)
    ]  # tracks which subarrays starting at a given index contain a pair summing to k
    for i in range(len(a)):
        for j in range(i + 1, min(i + m, len(a))):
            if a[i] + a[j] == k:
                distance = j - i
                if distance < m:
                    count = m - distance  # how many subarrays the pair appears in
                    for n in range(i - count + 1, i + 1):
                        if n in range(len(subarrays)):
                            subarrays[n] = 1
    return sum(subarrays)
