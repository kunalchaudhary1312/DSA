class Solution:
    def maxHeight(self, height, width, length):
        boxes = []
        for h, w, l in zip(height, width, length):
            boxes.append((max(w, l), min(w, l), h))
            boxes.append((max(h, l), min(h, l), w))
            boxes.append((max(h, w), min(h, w), l))

        boxes.sort(key=lambda b: (b[0] * b[1], b[0]), reverse=True)

        n = len(boxes)
        dp = [b[2] for b in boxes]

        for i in range(1, n):
            for j in range(i):
                if boxes[j][0] > boxes[i][0] and boxes[j][1] > boxes[i][1]:
                    dp[i] = max(dp[i], dp[j] + boxes[i][2])

        return max(dp)
      
