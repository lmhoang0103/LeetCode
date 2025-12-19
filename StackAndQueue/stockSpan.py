class Solution:
    def findPGE(self, arr):
        
        n = len(arr) # size of array
        ans = [0] * n
        st = []
        
        # Start traversing from the front
        for i in range(n):
            
            # Get the current element
            currEle = arr[i]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # element is not the greater element
            while st and arr[st[-1]] <= currEle:
                st.pop()
            
            # If the greater element is not 
            # found, stack will be empty
            if not st:
                ans[i] = -1
                
            # Else store the answer
            else:
                ans[i] = st[-1]
            
            # Push the current index in the stack 
            st.append(i)
        
        # Return the result
        return ans
    
    # Function to find the span of stock prices for each day
    def stockSpan(self, arr, n):
        
        # Get the indices of previous greater elements
        PGE = self.findPGE(arr)
        
        # To store the answer
        ans = [0] * n
        
        # Compute the result
        for i in range(n):
            ans[i] = i - PGE[i]
        return ans

# Class
# Same idea as monotone stack,  only one side, and apply using a class
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:

        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)