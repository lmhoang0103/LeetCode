class Solution:
    # Function to find the largest rectangle area
    def largestRectangleArea(self, heights):
        
        n = len(heights) # Size of array
        
        # Stack 
        st = []
        
        # To store largest area
        largestArea = 0
        
        # To store current area
        area = 0
        
        # To store the indices of next 
        # and previous smaller elements 
        nse, pse = 0, 0
        
        # Traverse on the array
        for i in range(n):
            
            # Pop the elements in the stack until 
            # the stack is not empty and the top 
            # elements is not the smaller element 
            while st and heights[st[-1]] >= heights[i]:
                      
                # Get the index of top of stack
                ind = st.pop()
                
                # Update the index of 
                # previous smaller element 
                pse = st[-1] if st else -1
                
                # Next smaller element index for 
                # the popped element is current index 
                nse = i
                
                # Calculate the area of the popped element
                area = heights[ind] * (nse - pse - 1)
                
                # Update the maximum area
                largestArea = max(largestArea, area)
            
            # Push the current index in stack
            st.append(i)
        
        # For elements that are not popped from stack
        while st:
            
            # NSE for such elements is size of array
            nse = n
            
            # Get the index of top of stack
            ind = st.pop()
            
            # Update the previous smaller element
            pse = st[-1] if st else -1
            
            # Calculate the area of the popped element
            area = heights[ind] * (nse - pse - 1)
            
            # Update the maximum area
            largestArea = max(largestArea, area)
        
        # Return largest area found
        return largestArea
    
    # Function to find the largest 
    # rectangle area containing all 1s 
    def maximalAreaOfSubMatrixOfAll1(self, matrix):
        
        # Determine the size of matrix
        n = len(matrix)
        m = len(matrix[0])
        
        # Prefix sum matric to store heights 
        # for different ground levels 
        prefixSum = [[0] * m for _ in range(n)]
        
        # Fill up the prefix sum matrix column wise
        for j in range(m):
            sum = 0
            
            for i in range(n):
                sum += matrix[i][j]
                
                # If there is no base present
                if matrix[i][j] == 0:
                    prefixSum[i][j] = 0
                    sum = 0
                else:
                    # Store the height
                    prefixSum[i][j] = sum
        
        # To store the maximum area
        maxArea = 0
        
        # Traverse for different levels of ground
        for i in range(n):
            
            # Get the largest area for current level
            area = self.largestRectangleArea(prefixSum[i])
            
            # Update the maximum area
            maxArea = max(area, maxArea)
        
        # Return the maximum area
        return maxArea

# Main code
if __name__ == "__main__":
    matrix = [
        [1, 0, 1, 0, 0], 
        [1, 0, 1, 1, 1], 
        [1, 1, 1, 1, 1], 
        [1, 0, 0, 1, 0]
    ]
    
    # Creating an instance of Solution class
    sol = Solution() 
    
    # Function call to find the largest rectangle area containing all 1s
    ans = sol.maximalAreaOfSubMatrixOfAll1(matrix)
    
    print("The largest rectangle area containing all 1s is:", ans)