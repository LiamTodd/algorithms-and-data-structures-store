# task: return true if the array can be made strictly increasing by removing at most one element, else false.


def solution(sequence):
    left = 0
    right = 1
    err_left = 0
    rem_idx = None
    while right < len(sequence):
        flag = False
        if sequence[left] >= sequence[right]:
            err_left += 1
            flag = True
            rem_idx = left
        if err_left > 1:
            break

        if flag:
            if left == 0:
                left += 1
                right += 1
            else:
                left -= 1
        else:
            left += 1
            if rem_idx == left:
                left += 1
            right += 1

    left = 0
    right = 1
    err_right = 0
    rem_idx = None
    while right < len(sequence):
        flag = False
        if sequence[left] >= sequence[right]:
            err_right += 1
            flag = True
            rem_idx = right
        if err_right > 1:
            break

        if flag:
            right += 1
        else:
            left += 1
            if rem_idx == left:
                left += 1
            right += 1

    if err_left > 1 and err_right > 1:
        return False

    return True
