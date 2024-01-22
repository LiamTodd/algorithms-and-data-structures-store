VOWELS = {"a", "e", "i", "o", "u"}


class Solution:
    def countVowels(self, s):
        return sum([1 if c.lower() in VOWELS else 0 for c in s])

    def halvesAreAlike(self, s: str) -> bool:
        return self.countVowels(s[0 : len(s) // 2]) == self.countVowels(
            s[len(s) // 2 :]
        )
