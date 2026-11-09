class Solution:
    def minDistance(self, word1: str, word2: str) :
        r = len(word1)
        c = len(word2)
        dp = [[0]*(c+1) for _ in range(r+1)]
        for i in range(r+1):
            dp[i][0] = i
        for j in range(c+1):
            dp[0][j] = j
        for i in range(1,r+1):
            for j in range(1,c+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[r][c]



