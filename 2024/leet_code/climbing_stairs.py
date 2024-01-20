class Solution:
    def climbStairs_attempt_1(self, n):
        # SOLUTION RAN TOO SLOW

        # base case: stair 0
        if n == 0:
            return 0
        # base case: stair 1
        if n == 1:
            return 1
        # base case: stair 2
        if n == 2:
            return 2
        # recursive case: number of ways to climb to previous two stairs
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution:
    def climbStairs(self, n):
        # ACCEPTED dynamic programming approach using memoization

        # special case: early exit
        if n <= 2:
            return n

        # memoisation
        memo = [None for _ in range(n)]
        # base case: stair 1
        memo[0] = 1
        # base case: stair 2
        memo[1] = 2
        # number of ways to climb stair n = number of ways to climb n-1 + number of ways to climb n-2
        for i in range(2, n):
            memo[i] = memo[i - 1] + memo[i - 2]

        # return number of ways to climb stair n only
        return memo[n - 1]
