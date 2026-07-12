import heapq

class Solution:
    def maxAmount(self, arr, k):
        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)
        
        total_amount = 0
        MOD = 10**9 + 7
        
        while k > 0 and max_heap:
            current_max = -heapq.heappop(max_heap)
            total_amount = (total_amount + current_max) % MOD
            
            if current_max - 1 > 0:
                heapq.heappush(max_heap, -(current_max - 1))
            
            k -= 1
            
            
        return total_amount
