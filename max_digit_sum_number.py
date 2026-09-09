class Solution:
    def findMax(self, n):
        n_str = str(n)
        ans = n
        max_sum = sum(int(d) for d in n_str)

        for i in range(len(n_str)):
            if n_str[i] == '0':
                continue

            candidate_str = n_str[:i] + str(int(n_str[i]) - 1) + '9' * (len(n_str) - i - 1)
            candidate = int(candidate_str)
            cand_sum = sum(int(d) for d in str(candidate))

            if cand_sum > max_sum:
                max_sum = cand_sum
                ans = candidate
            elif cand_sum == max_sum:
                ans = max(ans, candidate)

        return ans
