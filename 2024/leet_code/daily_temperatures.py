from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # identical to next-greatest-element implementation, except store index differential in result array instead of n.g.e.
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            stack.append((temperatures[i - 1], i - 1))  # push to the stack
            curr = temperatures[i]
            while len(stack) > 0 and curr > stack[-1][0]:  # peek the top of the stack
                _, idx = stack.pop()
                res[idx] = i - idx
        return res
