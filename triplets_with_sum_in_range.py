class Solution:
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        arr.sort()
        n = len(arr)

        def count_at_most(target: int) -> int:
            count = 0

            for i in range(n - 2):
                left, right = i + 1, n - 1

                while left < right:
                    total = arr[i] + arr[left] + arr[right]

                    if total <= target:
                        count += right - left
                        left += 1
                    else:
                        right -= 1

            return count

        return count_at_most(r) - count_at_most(l - 1)
