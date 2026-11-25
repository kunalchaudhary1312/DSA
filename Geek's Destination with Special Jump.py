MOD = 10**9 + 7


class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        net = a - b
        cycle = a + b

        def normal_time(pos: int) -> int:
            if pos <= 0:
                return 0
            if pos <= a:
                return pos
            k = (pos - a + net - 1) // net
            rem = pos - k * net
            if rem <= a:
                return k * cycle + rem
            return (k + 1) * cycle

        def sum_normal_1_to_n(n: int) -> int:
            if n <= 0:
                return 0
            if n <= a:
                return n * (n + 1) // 2

            total = a * (a + 1) // 2
            k_max = (n - a + net - 1) // net
            last_full_end = k_max * net + a
            full_k = k_max if n >= last_full_end else k_max - 1

            if full_k >= 1:
                s1 = full_k * (full_k + 1) // 2
                block_const = net * (b + 1) + net * (net - 1) // 2
                total += net * cycle * s1 + full_k * block_const

            rem_start = full_k * net + a + 1
            if rem_start <= n:
                k_part = full_k + 1
                cnt = n - rem_start + 1
                first_val = k_part * cycle + (rem_start - k_part * net)
                last_val = k_part * cycle + (n - k_part * net)
                total += cnt * (first_val + last_val) // 2

            return total

        def sum_normal_range(low: int, high: int) -> int:
            if low > high:
                return 0
            return sum_normal_1_to_n(high) - sum_normal_1_to_n(low - 1)

        no_jump = normal_time(d)
        if l > r:
            return 0

        cap = no_jump - 1
        ans = 0

        j_ge_d_l = max(l, d)
        if j_ge_d_l <= r:
            cnt = r - j_ge_d_l + 1
            val = 1 if cap >= 0 else no_jump
            ans = (ans + cnt * (val % MOD)) % MOD

        j_lt_d_r = min(r, d - 1)
        if l <= j_lt_d_r:
            t_low = d - j_lt_d_r
            t_high = d - l
            if cap < 0:
                cnt = t_high - t_low + 1
                ans = (ans + cnt * (no_jump % MOD)) % MOD
            else:
                lo, hi = t_low, t_high + 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if normal_time(mid) <= cap:
                        lo = mid + 1
                    else:
                        hi = mid
                t_good_end = lo - 1
                if t_low <= t_good_end:
                    cnt_good = t_good_end - t_low + 1
                    ans = (ans + sum_normal_range(t_low, t_good_end) + cnt_good) % MOD
                if lo <= t_high:
                    cnt_bad = t_high - lo + 1
                    ans = (ans + cnt_bad * (no_jump % MOD)) % MOD

        return ans % MOD
