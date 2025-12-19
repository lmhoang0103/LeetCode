class Solution:
    # Function to remove outer parentheses
    def removeOuterParentheses(self, s):
        # Initialize result string
        result = ""  
        # Initialize nesting level counter
        level = 0     

        # Traverse the string
        for char in s:
            # If we encounter '(', increase the level
            if char == '(':
                # If we're inside a primitive, add '(' to result
                if level > 0:
                    result += char
                # Increase the nesting level for '('
                level += 1  
            elif char == ')':
                # Decrease the nesting level for ')'
                level -= 1  
                # If we're inside a primitive, add ')' to result
                if level > 0:
                    result += char

        # Return the final result after removing the outer parentheses
        return result

# Example usage
s = "(()())(())"  
sol = Solution() 

# Get result
print(sol.removeOuterParentheses(s)) 
Complexity Analysis