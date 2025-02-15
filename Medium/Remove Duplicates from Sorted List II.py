class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(elements):
    head = None
    tail = None
    for element in elements:
        new_node = ListNode(element)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

# Example usage:
elements = [1,2,3,3,4,4,5]
head = create_linked_list(elements)

def solution(head):
    if not head:
        return head

    dummy = ListNode(0, head)
    prev = dummy
    
    while head:
        # Check for duplicates by comparing the current node with the next node
        if head.next and head.val == head.next.val:
            print(f"Duplicate found starting at node with value: {head.val}")
            # Skip all nodes that have the same value
            while head.next and head.val == head.next.val:
                head = head.next
                print(f"Skipping node with value: {head.val}")
        
        # Check if the previous pointer should be moved or if it should skip the current node
        if prev.next == head:
            print(f"No duplicates directly after prev. Keeping node with value: {head.val}")
            prev = prev.next
        else:
            print(f"Removing all nodes with value: {head.val}")
            prev.next = head.next
        
        # Move head to the next node
        head = head.next
        print("Current list:", end=" ")
        curr = dummy.next
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
    
    return dummy.next

def log(head):
    while head:
        print(head.val)
        head= head.next

log(solution(head))
         
                
            
        
        
    
    