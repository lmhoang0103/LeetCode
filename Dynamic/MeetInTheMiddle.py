class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//2
        # Let's say the sum is x
        # Diff = | (S-x) - x| = |S-2x| => want x (lower sum) to be as close to S/2 as possible

        # Cut nums into 2 part, equal ele = n
        # How many ele to takes in each part, x and n-x
        A = nums[:n]
        B = nums[n:]

        total = sum(nums)

        sumA = defaultdict(list)
        sumB = defaultdict(list)

        # Build subsets of A in their sum
        # SumA[i] = all sum of subset that have i element
        sumA[0] = 0
        for num in A:
            # For not repeat ele, run back to start
            for k in range(len(A), 0, -1):
                for s in sumA[k-1]:
                    sumA[k].append(s+num)

        sumB[0] = 0
        for num in B:
            # For not repeat ele, run back to start
            for k in range(len(B), 0, -1):
                for s in sumB[k-1]:
                    sumB[k].append(s+num)

        for k in sumB:
            sumB[k].sort()

        res = float('inf')
        for k in range(n+1):
            listA = sumA[k]
            listB = sumB[n-k]

            for a in listA:
                target = total // 2 - a
                arr = listB
                # Binary search for second sum in B
                l, r = 0, len(arr) -1
                while l<=r:
                    mid = (l+r)//2
                    cur = a + arr[mid]
                    res = min(res, abs(total- 2*cur))
                    if arr[mid] < target:
                        l = mid +1
                    else:
                        r = mid -1

        return res

        