class Solution:
    def levelSort(self, arr):
        result = []
        index = 0
        level_size = 1
        n = len(arr)
        
        while index < n:
            current_level = arr[index : index + level_size]
            current_level.sort()
            result.append(current_level)
            
            index += level_size
            level_size *= 2
            
        return result
