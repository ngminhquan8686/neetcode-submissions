class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)

        nums.sort()
        for i in range(n):
            right = n - 1
            left = i + 1
            while left < right:
                if nums[left] + nums[right] > - nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    triplet = tuple(sorted([nums[i], nums[left], nums[right]]))
                    res.add(triplet)
                    right -= 1
                    left += 1
        
        return [list(t) for t in res]


        