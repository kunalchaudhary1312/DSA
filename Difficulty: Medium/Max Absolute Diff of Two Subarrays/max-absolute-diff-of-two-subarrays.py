class Solution:
    def maxDiffSubArrays(self, arr):
        n = len(arr)
        if n < 2:
            return 0
            
        leftMax = [0] * n
        leftMin = [0] * n
        rightMax = [0] * n
        rightMin = [0] * n
        
        currMax = arr[0]
        currMin = arr[0]
        leftMax[0] = arr[0]
        leftMin[0] = arr[0]
        
        for i in range(1, n):
            currMax = max(arr[i], currMax + arr[i])
            leftMax[i] = max(leftMax[i-1], currMax)
            
            currMin = min(arr[i], currMin + arr[i])
            leftMin[i] = min(leftMin[i-1], currMin)
            
        currMax = arr[-1]
        currMin = arr[-1]
        rightMax[-1] = arr[-1]
        rightMin[-1] = arr[-1]
        
        for i in range(n-2, -1, -1):
            currMax = max(arr[i], currMax + arr[i])
            rightMax[i] = max(rightMax[i+1], currMax)
            
            currMin = min(arr[i], currMin + arr[i])
            rightMin[i] = min(rightMin[i+1], currMin)
            
        res = 0
        for i in range(n-1):
            res = max(res, abs(leftMax[i] - rightMin[i+1]), abs(leftMin[i] - rightMax[i+1]))
            
        return res