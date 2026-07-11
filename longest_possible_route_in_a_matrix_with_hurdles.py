class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        if mat[xs][ys] == 0 or mat[xd][yd] == 0:
            return -1
            
        n = len(mat)
        m = len(mat[0])
        self.max_len = -1
        
        def dfs(r, c, current_len):
            if r == xd and c == yd:
                self.max_len = max(self.max_len, current_len)
                return
                
            mat[r][c] = 0
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1:
                    dfs(nr, nc, current_len + 1)
                    
            mat[r][c] = 1
            
        dfs(xs, ys, 0)
        return self.max_len
