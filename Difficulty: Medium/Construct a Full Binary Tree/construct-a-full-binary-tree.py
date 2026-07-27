class Solution:
    def constructBinaryTree(self, pre, preMirror):
        self.preIndex = 0
        n = len(pre)
        
        def build(l, h):
            if l > h or self.preIndex >= n:
                return None
            
            root = Node(pre[self.preIndex])
            self.preIndex += 1
            
            if l == h:
                return root
            
            i = l
            while i <= h:
                if preMirror[i] == pre[self.preIndex]:
                    break
                i += 1
            
            root.left = build(i, h)
            root.right = build(l + 1, i - 1)
            
            return root
            
        return build(0, n - 1)