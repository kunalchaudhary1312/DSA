class Solution:
    def maxIndexDifference(self, s):
        n = len(s)
        max_reach = [-1] * 26
        ans = -1
        
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - 97
            reach = i
            
            if c < 25 and max_reach[c + 1] != -1:
                reach = max_reach[c + 1]
                
            max_reach[c] = max(max_reach[c], reach)
            
            if c == 0:
                ans = max(ans, reach - i)
                
        return ans