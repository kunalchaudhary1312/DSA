class Solution:

  def countAlwaysFound(self, arr: list[int]) -> int:
    n = len(arr)
    left_max = [-1] * n
    right_min = [float('inf')] * n

    cur_max = -1
    for i in range(n):
      left_max[i] = cur_max
      if arr[i] > cur_max:
        cur_max = arr[i]

    cur_min = float('inf')
    for i in range(n - 1, -1, -1):
      right_min[i] = cur_min
      if arr[i] < cur_min:
        cur_min = arr[i]

    count = 0
    for i in range(n):
      if arr[i] > left_max[i] and arr[i] < right_min[i]:
        count += 1

    return count
