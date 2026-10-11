class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_rate = 0
        while left <= right :
            mid = left + (right - left) // 2
            total_hour= 0
            for pile in piles:
                if pile % mid == 0:
                    total_hour += pile // mid
                else:
                    total_hour += (pile // mid) + 1
            if total_hour > h:
                left = mid + 1
            else:
                right = mid - 1
                
                if min_rate == 0:
                    min_rate = mid
                elif min_rate > mid:
                    min_rate = mid
        return min_rate

