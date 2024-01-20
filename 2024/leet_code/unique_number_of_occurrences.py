from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # early exit: 0 or 1 elements in the array
        if len(arr) < 2:
            return True

        # sort items
        arr_sorted = sorted(arr)

        # iterate through, tracking unique occurrences
        occurrences = [
            False for _ in range(len(arr))
        ]  # False means 'this number of occurrences is still unique'
        current = arr_sorted[0]
        occurrences_current = 1
        for element in arr_sorted[1:]:
            if element == current:
                # found another instance of the same element
                occurrences_current += 1
            else:
                # encountered a new element
                # check if the number of occurrences is unique
                if occurrences[occurrences_current - 1]:
                    return False
                # store the number of occurrences and reset the current counter and current
                occurrences[occurrences_current - 1] = True
                occurrences_current = 1
                current = element

        # Check for last element
        if occurrences[occurrences_current - 1]:
            return False

        return True
