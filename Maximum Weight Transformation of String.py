class Solution :
    def getMaxWeight ( self , s ) :
        n = len ( s )
        if n == 0 :
            return 0
        prev2 = 0
        prev1 = 1
        for i in range ( 2 , n + 1 ) :
            res1 = prev1 + 1
            toggles = 0 if s [ i - 2 ] != s [ i - 1 ] else 1
            res2 = prev2 + ( 4 - toggles )
            curr = max ( res1 , res2 )
            prev2 = prev1
            prev1 = curr
        return prev1
