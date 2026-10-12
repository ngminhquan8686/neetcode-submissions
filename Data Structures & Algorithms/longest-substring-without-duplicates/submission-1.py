class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l, res = 0, 0
        for r in range(len(s)):

            while s[r] in unique:
                unique.remove(s[l])
                l += 1

            res = max(r - l + 1, res)
            unique.add(s[r])

        return res