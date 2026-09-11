import math

class Solution:
    def sameMod(self, arr):
        g = 0
        for x in arr:
            g = math.gcd(g, abs(x - arr[0]))

        if g == 0:
            return -1

        count = 0
        for i in range(1, int(g**0.5) + 1):
            if g % i == 0:
                count += 1
                if i != g // i:
                    count += 1

        return count