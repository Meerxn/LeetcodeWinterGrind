class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        OPT = [[0 for j in range(len(text2) + 1)] for i in range(len(text1)+1)]
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    OPT[i][j] = 1+ OPT[i+1][j+1]
                else:
                    OPT[i][j] = max(OPT[i+1][j],OPT[i][j+1])
        return OPT[0][0]