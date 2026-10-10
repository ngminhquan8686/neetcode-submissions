class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        min_idx = 0
        while left < right:
            mid = left + (right - left) // 2
            if right - left > 1:
                if nums[mid] < nums[right]:
                    right = mid
                elif nums[mid] > nums[right]:
                    left = mid
            else:
                if nums[left] > nums[right]:
                    min_idx = right
                    break
                else:
                    min_idx = left
                    break
        if target == nums[min_idx]:
            return min_idx
        left = 0
        right = len(nums) - 1
        if min_idx == 0:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                
            return -1
        elif min_idx == len(nums) - 1:
            right -= 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                
            return -1
        else:
            if target < nums[right]:
                left = min_idx + 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                    
                return -1
            elif target > nums[right]:
                right = min_idx - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                    
                return -1
            else:
                return right




        


