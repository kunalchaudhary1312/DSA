class Solution :
    def findXOR ( self , l : int , r : int ) -> int :
        def compute(n):
            rem = n % 4
            if rem == 0:
                return n
            elif rem == 1:
                return 1
            elif rem == 2:
                return n + 1
            else:
                return 0
        return compute(l - 1) ^ compute(r)
