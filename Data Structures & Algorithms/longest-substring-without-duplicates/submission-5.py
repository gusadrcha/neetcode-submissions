class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        curr = set()
        res = 0
        for r in range(len(s)):
            if s[r] not in curr:
                curr.add(s[r])
            else:
                while s[r] in curr:
                    curr.remove(s[l])
                    l += 1
                curr.add(s[r])
            
            res = max(res, len(curr))
        
        return res
        