class Solution:
    def isPossible(self, arr, s, x):
        seq = [s]
        curr_sum = s
        
        for a in arr:
            next_val = curr_sum + a
            seq.append(next_val)
            curr_sum += next_val
            if next_val > x:
                break
                
        for v in reversed(seq):
            if x >= v:
                x -= v
                
        return x == 0