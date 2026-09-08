class Solution:
    def searchWord(self, mat, word):
        if not mat or not mat[0] or not word:
            return []

        R = len(mat)
        C = len(mat[0])
        word_len = len(word)
        ans = []

        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for r in range(R):
            for c in range(C):
                if mat[r][c] == word[0]:
                    found = False
                    for dr, dc in dirs:
                        curr_r, curr_c = r, c
                        k = 1
                        while k < word_len:
                            curr_r += dr
                            curr_c += dc
                            if 0 <= curr_r < R and 0 <= curr_c < C and mat[curr_r][curr_c] == word[k]:
                                k += 1
                            else:
                                break
                        if k == word_len:
                            found = True
                            break
                    if found:
                        ans.append([r, c])
        return ans
