class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # formula for number of missing at arr[i] = arr[i] - i -1
        low, high = 0, len(arr) -1
        # Edge case where arr not missing
        if arr[high] - arr[low]== len(arr) -1:
            if k < arr[low]:
                return k
            else:
                return arr[high] + (k-arr[low]) +1
        

        while low <=high:
            if low == high:
                break
            mid = (low+high)//2
            # Check if element at this point miss >= k element:
            missing = arr[mid] - mid -1
            if missing < k:
                low = mid +1
            else:
                #if contain kth missing ele, try to lower

                high = mid
        
        #if after search, still find that k is outside range on the right side
        if arr[high] - high - 1 < k:
            return high + k + 1
        return high + k