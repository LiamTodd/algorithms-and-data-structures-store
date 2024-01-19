# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# solution(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".


def count_chars(s1):
    res = {}
    for char in s1:
        if char in res.keys():
            res[char] += 1
        else:
            res[char] = 1
    return res


def solution(s1, s2):
    counter_s1 = count_chars(s1)
    counter_s2 = count_chars(s2)
    print(counter_s1, counter_s2)
    res = 0
    for char in counter_s1.keys():
        if char in counter_s2.keys():
            res += min(counter_s1[char], counter_s2[char])
    return res
