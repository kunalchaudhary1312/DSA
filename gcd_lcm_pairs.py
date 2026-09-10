class Solution:
    def pairCount(self, x, y):
        if y % x != 0:
            return 0

        n = y // x
        count = 0
        i = 2

        while i * i <= n:
            if n % i == 0:
                count += 1
                while n % i == 0:
                    n //= i
            i += 1

        if n > 1:
            count += 1

        return 1 << count
