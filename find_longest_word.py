class Solution:
    def findLongestWord(self, s: str, d: list) -> str:
        ans = ""
        for word in d:
            if len(word) < len(ans) or (len(word) == len(ans) and word >= ans):
                continue

            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1

            if i == len(word):
                ans = word

        return ans
