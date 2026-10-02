class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        def cal_area(idx1, idx2):
            return abs((idx2 - idx1) * min(heights[idx1], heights[idx2]))

        while left < right:
            if cal_area(left, right) > max_area:
                max_area = cal_area(left, right)
            if cal_area(left + 1, right) > max_area:
                max_area = cal_area(left + 1, right)
            if cal_area(left, right - 1) > max_area:
                max_area = cal_area(left, right - 1)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return max_area


        