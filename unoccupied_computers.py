class Solution:
    def solve(self, n, s):
        occupied = set()
        rejected = set()
        for char in s:
            if char not in occupied and char not in rejected:
                if len(occupied) < n:
                    occupied.add(char)
                else:
                    rejected.add(char)
            elif char in occupied:
                occupied.remove(char)
        return len(rejected)
