class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for str in strs:
            encoded_string += f"{len(str)}${str}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            
            length = int(s[i:j])
            i = j + length + 1
            res.append(s[j + 1:i])
        
        return res

            

            



