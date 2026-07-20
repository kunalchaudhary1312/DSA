class Node:
    def __init__(self):
        self.child = {}
        self.freq = 0

class Solution:
    def findPrefixes(self, arr):
        root = Node()
        
        for word in arr:
            curr = root
            for ch in word:
                if ch not in curr.child:
                    curr.child[ch] = Node()
                curr = curr.child[ch]
                curr.freq += 1
        
        ans = []
        for word in arr:
            curr = root
            pref = ""
            for ch in word:
                pref += ch
                curr = curr.child[ch]
                if curr.freq == 1:
                    break
            ans.append(pref)
            
        return ans
