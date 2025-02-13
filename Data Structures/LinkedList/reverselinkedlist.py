class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    prev = None
    curr = head
    step = 0  # To keep track of the step number for demonstration purposes

    while curr:
        step += 1
        next = curr.next  # Store next node
        print(f"Step {step}: Current node is {curr.val}")
        
        # Reversing the current node's pointer
        curr.next = prev
        print(f" - Reversed {curr.val}'s next pointer from {None if next is None else next.val} to {None if prev is None else prev.val}")
        
        # Move prev and curr one step forward
        prev = curr
        curr = next

        # Display the current state of the reversed part
        print(" - New state of linked list from start to this node:")
        n = prev
        while n:
            print(f" {n.val} ->", end='')
            n = n.next
        print(" None")

    print("Reversal complete. New head is", prev.val)
    return prev

# Helper function to create a linked list from a list of values
def createLinkedList(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for value in lst[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Helper function to print a linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(f"{curr.val} ->", end=" ")
        curr = curr.next
    print("None")

# Create a linked list
lst = [1, 2, 3, 4, 5]
head = createLinkedList(lst)
print("Original Linked List:")
printLinkedList(head)

# Reverse the linked list
reversed_head = reverseLinkedList(head)
print("Reversed Linked List:")
printLinkedList(reversed_head)
