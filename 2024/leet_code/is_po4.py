import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        n_log_4 = math.log(n, 4)
        return math.ceil(n_log_4) - n_log_4 == 0
