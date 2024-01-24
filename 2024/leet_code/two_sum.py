from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort array, maintaining original indexes
        nums_idx = [(nums[i], i) for i in range(len(nums))]
        sorted_nums = sorted(nums_idx, key=lambda e: e[0])

        for i in range(len(sorted_nums)):
            diff = target - sorted_nums[i][0]
            # search for diff in sorted_nums
            diff_idx = self.binary_search(sorted_nums, diff)
            if diff_idx is not None and diff_idx != sorted_nums[i][1]:
                return [sorted_nums[i][1], diff_idx]

    def binary_search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while hi >= lo:
            mid = (hi + lo) // 2
            if nums[mid][0] == target:
                return nums[mid][1]
            if nums[mid][0] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return None


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
    print(s.twoSum([3, 2, 4], 6))
