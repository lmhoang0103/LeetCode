


def findMedianSortedArrays(a, b):
    # Ensure the first array is the smaller one
    if len(a) > len(b):
        return findMedianSortedArrays(b, a)

    n1, n2 = len(a), len(b)
    low, high = 0, n1

    # Perform binary search on the smaller array
    while low <= high:
        # Calculate cut points in both arrays
        cut1 = (low + high) // 2
        cut2 = (n1 + n2 + 1) // 2 - cut1

        # Handle edge elements using -inf and inf
        l1 = float('-inf') if cut1 == 0 else a[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else b[cut2 - 1]
        r1 = float('inf') if cut1 == n1 else a[cut1]
        r2 = float('inf') if cut2 == n2 else b[cut2]

        # Check if partition is correct
        if l1 <= r2 and l2 <= r1:
            # Even total length: take average of max left and min right
            if (n1 + n2) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
            else:
                # Odd length: take max of left side
                return max(l1, l2)
        elif l1 > r2:
            # Move left in a[]
            high = cut1 - 1
        else:
            # Move right in a[]
            low = cut1 + 1

    return 0.0  

# Example usage
a = [1, 3]
b = [2]
print("Median is:", findMedianSortedArrays(a, b))
Complexity Analysis
TakeUForward Ad
