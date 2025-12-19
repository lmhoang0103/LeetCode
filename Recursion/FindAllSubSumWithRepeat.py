class Solution:

    # Function to find all combinations recursively
    def findCombination(self, ind, target, arr, ans, ds):
        # Base case: if we have considered all elements in the array
        if ind == len(arr):
            # If the target is zero, we have found a valid combination
            if target == 0:
                ans.append(list(ds))  # Add the current combination to the result
            return

        # Recursive case: pick the element if it's less than or equal to the target
        if arr[ind] <= target:
            ds.append(arr[ind])  # Add the current element to the combination
            self.findCombination(ind, target - arr[ind], arr, ans, ds)  # Continue with the same index to allow repeated elements
            ds.pop()  # Backtrack by removing the last added element

        # Skip the current element and move to the next index
        self.findCombination(ind + 1, target, arr, ans, ds)

    # Main function to get all combinations
    def combinationSum(self, candidates, target):
        ans = []  # To store the result
        ds = []  # To store a current combination
        self.findCombination(0, target, candidates, ans, ds)  # Start the recursive search
        return ans  # Return all valid combinations

# Driver code
if __name__ == "__main__":
    obj = Solution()
    v = [2, 3, 6, 7]  # Candidate numbers
    target = 7  # Target sum

    # Get all combinations
    ans = obj.combinationSum(v, target)

    # Output the combinations
    print("Combinations are: ")
    for combination in ans:
        print(" ".join(map(str, combination)))  # Print each element of the combination