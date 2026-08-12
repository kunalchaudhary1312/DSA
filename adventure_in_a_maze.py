class Solution:
    def findWays(self, grid):
        n = len(grid)
        MOD = 10**9 + 7
        
        paths = [[0] * n for _ in range(n)]
        max_adv = [[0] * n for _ in range(n)]
        
        paths[0][0] = 1
        max_adv[0][0] = grid[0][0]
        
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                if i > 0 and grid[i-1][j] in (2, 3) and paths[i-1][j] > 0:
                    paths[i][j] = (paths[i][j] + paths[i-1][j]) % MOD
                    max_adv[i][j] = max(max_adv[i][j], max_adv[i-1][j] + grid[i][j])
                    
                if j > 0 and grid[i][j-1] in (1, 3) and paths[i][j-1] > 0:
                    paths[i][j] = (paths[i][j] + paths[i][j-1]) % MOD
                    max_adv[i][j] = max(max_adv[i][j], max_adv[i][j-1] + grid[i][j])
                    
        if paths[n-1][n-1] == 0:
            return [0, 0]
            
        return [paths[n-1][n-1], max_adv[n-1][n-1]]
