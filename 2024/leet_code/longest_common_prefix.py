from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # vertical scan approach: accepted, faster than average

        # find shortest string
        min_length = min([len(s) for s in strs])

        max_length = 0
        flag = True
        for i in range(min_length):
            # get the character in the i'th position of string 0
            c = strs[0][i]
            # check that all strings have the same character at the i'th position (except str 0)
            for s in strs[1:]:
                # if any string has a different character, break from the loop, signal to outer loop
                if s[i] != c:
                    flag = False
                    break
            # end execution if any character is a mismatch
            if flag is False:
                break
            # all characters match, so increase the max length count
            max_length += 1

        return strs[0][:max_length]

    # 'brute force' (although still accepted)
    # slow
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     res = None
    #     for i in range(len(strs) - 1):
    #         for j in range(i+1, len(strs)):
    #             s1 = strs[i]
    #             s2 = strs[j]
    #             lcp = 0
    #             for k in range(min(len(s1), len(s2))):
    #                 if s1[k] == s2[k]:
    #                     lcp += 1
    #                 else:
    #                     break
    #             if res is None or lcp < res:
    #                 res = lcp
    #     return strs[0][:res]
