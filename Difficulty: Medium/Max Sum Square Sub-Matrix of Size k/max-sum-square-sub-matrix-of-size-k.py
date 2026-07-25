class Solution:
    def maximumSum(self, mat, k):
        n = len(mat)
        
        # Create a 2D array for prefix sums with an extra row and column of 0s
        # for easier boundary calculations.
        prefix = [[0] * (n + 1) for _ in range(n + 1)]
        
        # 1. Build the prefix sum matrix
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (mat[i-1][j-1] + 
                                prefix[i-1][j] + 
                                prefix[i][j-1] - 
                                prefix[i-1][j-1])
        
        max_sum = float('-inf')
        
        # 2. Iterate through all possible k x k sub-matrices
        for i in range(k, n + 1):
            for j in range(k, n + 1):
                # O(1) calculation of the k x k sub-matrix sum
                current_sum = (prefix[i][j] - 
                               prefix[i-k][j] - 
                               prefix[i][j-k] + 
                               prefix[i-k][j-k])
                
                # Update maximum sum found so far
                if current_sum > max_sum:
                    max_sum = current_sum
                    
        return max_sum