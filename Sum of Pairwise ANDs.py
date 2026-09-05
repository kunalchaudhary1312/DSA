class Solution:
        def pairAndSum(self, arr):
            total_sum = 0
            for i in range(32):
                set_bits_count = 0
                for num in arr:
                    if num & (1 << i):
                        set_bits_count += 1

                pairs = (set_bits_count * (set_bits_count - 1)) // 2
                total_sum += pairs * (1 << i)

            return total_sum
