class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):

            while True:
                if len(stack) == 0:
                    stack.append(i)
                    break
                elif t > temperatures[stack[-1]]:
                    tmp_idx = stack.pop()
                    res[tmp_idx] = i - tmp_idx
                elif t <= temperatures[stack[-1]]:
                    stack.append(i)
                    break
        
        return res

