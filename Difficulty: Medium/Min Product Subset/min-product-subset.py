class Solution:
    def minProd(self, arr):
        if len(arr) == 1:
            return arr[0]

        neg_count = 0
        zero_count = 0
        prod = 1
        max_neg = float('-inf')
        min_pos = float('inf')

        for num in arr:
            if num == 0:
                zero_count += 1
            else:
                if num < 0:
                    neg_count += 1
                    max_neg = max(max_neg, num)
                if num > 0:
                    min_pos = min(min_pos, num)
                prod *= num

        if neg_count == 0:
            if zero_count > 0:
                return 0
            return min_pos

        if neg_count % 2 == 0:
            prod //= max_neg

        return prod