def radix_sort_string(L):
    string_length = len(L[0])
    for i in range(string_length):
        L = string_radix_pass(L, i)
    return L

# stable counting sort on one index
def string_radix_pass(L, digit):

    # map digit to char index so digit=0 maps to LSC
    string_length = len(L[0])
    char_index = string_length - digit - 1

    # find max val
    max_val = ord("z")

    # construct count array
    count = [0 for _ in range(max_val + 1)]
    for string in L:
        count[ord(string[char_index]) - 1] += 1

    # construct position array
    positions = [0 for _ in range(len(count))]
    for i in range(1, len(positions)):
        positions[i] = positions[i-1] + count[i-1]
    
    # construct solution
    res = [None for _ in range(len(L))]
    for i in range(len(L)):
        res[positions[ord(L[i][char_index]) - 1]] = L[i]
        positions[ord(L[i][char_index]) - 1] += 1
    
    return res


print(radix_sort_string(['a', 'b', 'c', 'd']))
print(radix_sort_string(['d', 'c', 'b', 'a']))

print(radix_sort_string(['za', 'zb', 'zc', 'zd']))
print(radix_sort_string(['zd', 'zc', 'zb', 'za']))


