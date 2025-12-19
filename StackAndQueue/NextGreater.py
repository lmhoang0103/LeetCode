class Solution:
    
    # Function to find the next greater 
    # element for each element in the array
    def nextGreaterElements(self, arr):
        
        n = len(arr)  # size of array
        
        # To store the next greater elements
        ans = [-1] * n
        
        # Stack to get elements in LIFO fashion
        st = []
        
        # Start traversing from the back
        for i in range(2 * n - 1, -1, -1):
            
            # Get the actual index
            ind = i % n
            
            # Get the current element
            currEle = arr[ind]
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # element is not the greater element
            while st and st[-1] <= currEle:
                st.pop()
            
            # Store the answer for the second half
            if i < n:
                
                # If the greater element is not 
                # found, stack will be empty
                if st:
                    ans[i] = st[-1]
            
            # Push the current element in the stack 
            # maintaining the decreasing order
            st.append(currEle)
        
        # Return the result
        return ans

# Driver Code
if __name__ == "__main__":
    arr = [5, 7, 1, 7, 6, 0]
    
    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to find the next greater 
    # element for each element in the array
    ans = sol.nextGreaterElements(arr)
    
    print("The next greater elements are:", ans)