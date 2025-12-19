class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            if right == left:
                return nums[right]
            mid = (left +right)//2
            if mid%2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid
                elif nums[mid] == nums[mid-1]:
                    right = mid
                else:
                    return nums[mid]
            else:
                if nums[mid] == nums[mid + 1]:
                    right = mid-1
                elif nums[mid] == nums[mid-1]:
                    left = mid+1
                else:
                    return nums[mid]
                

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = int((left + right)/2)
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid
        return nums[left]