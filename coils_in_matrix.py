class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        dim = 4 * n
        c1 = [1]
        curr = 1
        dirs = [dim, 1, -dim, -1]
        dir_idx = 0

        for _ in range(dim - 1):
            curr += dirs[dir_idx]
            c1.append(curr)

        dir_idx = (dir_idx + 1) % 4
        length = dim - 2

        while length >= 2:
            for _ in range(2):
                for _ in range(length):
                    curr += dirs[dir_idx]
                    c1.append(curr)
                dir_idx = (dir_idx + 1) % 4
            length -= 2

        c2 = [(16 * n * n + 1) - x for x in c1]

        return [c1, c2]
