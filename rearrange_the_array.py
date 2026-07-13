import math

class Solution:
    def minOperations(self, b):
        MOD = 10**9 + 7
        n = len(b)
        visited = [False] * n
        lcm_val = 1
        
        for i in range(n):
            if not visited[i]:
                length = 0
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    curr = b[curr] - 1
                    length += 1
                
                if length > 0:
                    lcm_val = (lcm_val * length) // math.gcd(lcm_val, length)
                    
        return lcm_val % MOD
