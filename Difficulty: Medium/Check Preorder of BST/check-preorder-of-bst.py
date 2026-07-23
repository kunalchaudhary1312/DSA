class Solution:
    def canRepresentBST(self, arr):
        stack = []
        root = float('-inf')
        
        for val in arr:
            if val < root:
                return False
                
            while stack and stack[-1] < val:
                root = stack.pop()
                
            stack.append(val)
            
        return True