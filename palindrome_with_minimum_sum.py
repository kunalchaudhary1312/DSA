class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        arr = list(s)

        for i in range(n // 2):
            j = n - 1 - i
            if arr[i] != '?' and arr[j] != '?':
                if arr[i] != arr[j]:
                    return -1
            elif arr[i] != '?':
                arr[j] = arr[i]
            elif arr[j] != '?':
                arr[i] = arr[j]

        last_char = None
        for i in range(n // 2):
            if arr[i] != '?':
                last_char = arr[i]
                break

        if last_char is None:
            return 0

        for i in range(n // 2):
            if arr[i] == '?':
                arr[i] = last_char
                arr[n - 1 - i] = last_char
            else:
                last_char = arr[i]

        if n % 2 == 1 and arr[n // 2] == '?':
            arr[n // 2] = last_char

        ans = 0
        for i in range(n - 1):
            ans += abs(ord(arr[i]) - ord(arr[i + 1]))

        return ans
