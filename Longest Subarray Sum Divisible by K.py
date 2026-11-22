class Solution:
    def longestSubarrayDivK(self, arr, k):
        rem_idx = {0: -1}
        prefix_sum = 0
        max_len = 0

        for i, num in enumerate(arr):
            prefix_sum += num
            rem = prefix_sum % k
            if rem < 0:
                rem += k

            if rem in rem_idx:
                max_len = max(max_len, i - rem_idx[rem])
            else:
                rem_idx[rem] = i

        return max_len
