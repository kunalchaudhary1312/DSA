class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        s1 = set()
        s2 = set()

        def inorder1(node):
            if not node:
                return
            inorder1(node.left)
            s1.add(node.data)
            inorder1(node.right)

        def inorder2(node):
            if not node:
                return
            inorder2(node.left)
            s2.add(node.data)
            inorder2(node.right)

        inorder1(r1)
        inorder2(r2)

        common = sorted(list(s1.intersection(s2)))
        return common
