def next_greater_element(lst):
    stack = []
    res = [-1 for _ in range(len(lst))]
    for i in range(1, len(lst)):
        stack.append((lst[i - 1], i - 1))
        top = stack[-1]
        curr = lst[i]
        if curr > top[0]:
            # pop all elements from stack which are less than the current element
            while len(stack) > 0 and stack[-1][0] < curr:
                _, idx = stack.pop()
                res[idx] = curr
    return res


if __name__ == "__main__":
    lst = [6, 4, 3, 8, 7, 12, 15, 16, 2, 1, 5, 11, 13, 9]
    print(lst)
    print(next_greater_element(lst))
