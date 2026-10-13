class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        freq = {}
        formed = 0
        left = 0
        best = float('inf')
        l,r = 0, 0
        for right , c in enumerate(s):
            freq[c] = freq.get(c,0)+1
            if c in need and freq[c] == need[c]:
                formed +=1 
            while formed == len(need):
                if best > right - left +1:
                    best = right - left +1
                    l = left 
                    r = right +1
                freq[s[left]] -= 1
                if s[left] in need and freq[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1
                
        return s[l:r]

