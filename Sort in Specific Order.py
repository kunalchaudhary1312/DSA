class Solution:
    def sortIt(self, arr):
        odds = sorted([x for x in arr if x % 2 != 0], reverse=True)
        evens = sorted([x for x in arr if x % 2 == 0])
        arr[:] = odds + evens
