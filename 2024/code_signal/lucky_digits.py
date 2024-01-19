# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

# For n = 1230, the output should be
# solution(n) = true;
# For n = 239017, the output should be
# solution(n) = false.


def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    return digits


def solution(n):
    # could make it into a string, but want to extract digits instead
    digits = get_digits(n)

    l_sum = 0
    r_sum = 0
    for i in range(len(digits) // 2):
        l_sum += digits[i]
        r_sum += digits[len(digits) - 1 - i]

    return l_sum == r_sum
