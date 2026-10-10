import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters, make lowercase
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return cleaned == cleaned[::-1]
