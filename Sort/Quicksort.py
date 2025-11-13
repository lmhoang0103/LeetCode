class Solution:
    # Function to perform quicksort
    def quickSort(self, arr, low, high):
        # Base case
        if low < high:
            # Partition and get pivot index
            pivotIndex = self.partition(arr, low, high)

            # Sort left part
            self.quickSort(arr, low, pivotIndex - 1)

            # Sort right part
            self.quickSort(arr, pivotIndex + 1, high)

    # Function to partition the array
    def partition(self, arr, low, high):
        # Take pivot as last element
        pivot = arr[high]

        # i will track smaller elements
        i = low - 1

        # Loop through the array
        for j in range(low, high):
            # If element <= pivot
            if arr[j] <= pivot:
                # Move i forward
                i += 1

                # Swap arr[i] and arr[j]
                arr[i], arr[j] = arr[j], arr[i]

        # Put pivot in correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        # Return pivot index
        return i + 1

# Driver code
arr = [10, 7, 8, 9, 1, 5]

# Create object
sol = Solution()

# Call quicksort
sol.quickSort(arr, 0, len(arr) - 1)

# Print sorted array
print(*arr)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(a, low, high):
            pivot = a[(low + high) // 2]
            i, j = low - 1, high + 1
            while True:
                i += 1
                while a[i] < pivot:
                    i += 1
                j -= 1
                while a[j] > pivot:
                    j -= 1
                if i >= j:
                    return j
                a[i], a[j] = a[j], a[i]

        def quicksort(a, low, high):
            if low < high:
                p = partition(a, low, high)
                quicksort(a, low, p)
                quicksort(a, p + 1, high)

        quicksort(nums, 0, len(nums) - 1)
        return nums
