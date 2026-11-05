class Solution:
    def countSubstrings(self, s: str):
        ans = 0
        n = len(s)
        for i in range(n):
            l = i
            r = i + 1
            while l >= 0 and  r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            l,r = i,i
            while l >= 0 and  r < n  and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans 
