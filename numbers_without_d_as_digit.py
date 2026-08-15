class Solution:
    def countWithout(self, n: int, d: int) -> int:
        if n == 0:
            return 0

        s = str(n)
        length = len(s)
        memo = {}

        def dp(pos, tight, started):
            if pos == length:
                return 1 if started else 0

            state = (pos, tight, started)

            if state in memo:
                return memo[state]

            limit = int(s[pos]) if tight else 9
            count = 0

            for digit in range(limit + 1):

                # Don't allow d as an actual digit.
                # But allow leading zero when d == 0.
                if digit == d and (started or d != 0):
                    continue

                new_tight = tight and (digit == limit)
                new_started = started or (digit != 0)

                count += dp(
                    pos + 1,
                    new_tight,
                    new_started
                )

            memo[state] = count
            return count

        return dp(0, True, False)
