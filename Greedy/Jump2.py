class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # nums[i] = max jump
        # Min number of jump to reach last index?

        jumps = 0
        current_end = 0
        farthest = 0
        # Traverse through the array except the last element
        for i in range(len(nums) - 1):
            # Update the farthest index that can be reach
            farthest = max(farthest, i + nums[i])

            # Finish scan this section, reach the last point that can be reach using one jump from the section before
            # Set the end of the next section as the furthest point that can be reach by this section
            if i == current_end:
                # Increment jump counter
                jumps += 1

                # Move the range to the farthest position we can reach
                current_end = farthest
        return jumps