# Node class represents a linked list node
class Node:
    # Constructor with data and next pointer
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node
        self.next = next1

# Solution class contains merge sort logic
class Solution:
    # Function to merge two sorted linked lists
    def mergeTwoSortedLinkedLists(self, list1, list2):
        # Create a dummy node
        dummyNode = Node(-1)
        
        # Temp pointer to build merged list
        temp = dummyNode

        # Traverse both lists
        while list1 and list2:
            # Choose smaller node
            if list1.data <= list2.data:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            # Move temp pointer
            temp = temp.next

        # Attach remaining nodes
        if list1:
            temp.next = list1
        else:
            temp.next = list2

        # Return head of merged list
        return dummyNode.next

    # Function to find middle of linked list
    def findMiddle(self, head):
        # If list empty or single node
        if not head or not head.next:
            return head

        # Slow and fast pointers
        slow = head
        fast = head.next

        # Move fast twice as fast as slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Return middle node
        return slow

    # Function to perform merge sort
    def sortLL(self, head):
        # Base case: empty or single node
        if not head or not head.next:
            return head

        # Find middle node
        middle = self.findMiddle(head)

        # Split into two halves
        right = middle.next
        middle.next = None
        left = head

        # Recursively sort both halves
        left = self.sortLL(left)
        right = self.sortLL(right)

        # Merge sorted halves
        return self.mergeTwoSortedLinkedLists(left, right)

# Function to print linked list
def printLinkedList(head):
    # Temp pointer to traverse
    temp = head

    # Traverse and print nodes
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Driver code
if __name__ == "__main__":
    # Create linked list: 3 -> 2 -> 5 -> 4 -> 1
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(5)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(1)

    # Print original list
    print("Original Linked List:", end=" ")
    printLinkedList(head)

    # Create Solution object
    obj = Solution()

    # Sort the linked list
    head = obj.sortLL(head)

    # Print sorted list
    print("Sorted Linked List:", end=" ")
    printLinkedList(head)