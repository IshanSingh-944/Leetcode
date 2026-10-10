class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = {}
        freq_t = {}
        for i in s:
            freq[i] = freq.get(i,0)+1
        for j in t:
            freq_t[j] = freq_t.get(j,0)+1
        return freq == freq_t