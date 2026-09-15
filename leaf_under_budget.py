from collections import deque

class Solution:
    def getCount(self, root, k):
        if not root:
            return 0

        leaf_levels = []
        queue = deque([(root, 1)])

        while queue:
            node, level = queue.popleft()

            if not node.left and not node.right:
                leaf_levels.append(level)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        leaf_levels.sort()
        count = 0

        for cost in leaf_levels:
            if k >= cost:
                k -= cost
                count += 1
            else:
                break

        return count
