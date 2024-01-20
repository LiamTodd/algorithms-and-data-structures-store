from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # SOLUTION RAN TOO SLOW

        # get mins of all sub arrays
        mins = []
        # for each element in arr
        for i in range(len(arr)):
            # for each subarray starting at index i
            for j in range(i + 1, len(arr) + 1):
                # get the min of each subarray
                min_val = arr[i]
                for k in range(i + 1, j):
                    if arr[k] < min_val:
                        min_val = arr[k]
                mins.append(min_val)

        # sum minimums
        return sum(mins) % (10**9 + 7)
