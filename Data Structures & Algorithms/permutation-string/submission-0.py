class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        l = 0
        freq_1 = [0] * 26
        freq_2 = [0] * 26

        for c in s1:
            freq_1[ord(c) - ord('a')] += 1

        for r in range(len(s2)):
            check = True
            freq_2[ord(s2[r]) - ord('a')] += 1
            if r - l > len(s1) - 1:
                freq_2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            for i in range(26):
                if freq_1[i] != freq_2[i]:
                    check = False
                    break
            if check:
                return True
            
        return False
            
        