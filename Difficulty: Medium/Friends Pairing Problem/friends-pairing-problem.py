class Solution:
    def countFriendsPairings(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            c = b + (i - 1) * a
            a = b
            b = c
        return b