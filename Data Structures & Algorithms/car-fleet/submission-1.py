class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack:
                stack.append(time)
                res += 1
            elif time > stack[-1]:
                stack.pop()
                stack.append(time)
                res += 1


        return res
            

        
    
            


        