class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        def backtrack(i, path):
            ans.append(path[:])
            #Always take nums[i]
            for j in range(i, len(nums)):
                # Skip if this element is different than i and the same as it before
                # Dont need to take this ele if taking the previous ele is the same
                # Because we always take nums[i] -> already have the situation where the number of combination is from 0->max
                if j > i and nums[j] == nums[j-1]: # skip duplicates
                    continue
                path.append(nums[j])
                backtrack(j + 1, path)
                path.pop()
        
        backtrack(0, [])
        return ans