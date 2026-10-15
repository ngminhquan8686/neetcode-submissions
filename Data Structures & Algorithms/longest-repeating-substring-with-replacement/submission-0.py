class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, length = 0, 0 
        res = float('-inf')

        for r in range(len(s)):
            length += 1
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            max_count = max(count.values())
            while length > max_count + k:
                count[s[l]] -= 1
                max_count = max(count.values())
                l += 1
                length -= 1
            res = max(length, res)

        return res
