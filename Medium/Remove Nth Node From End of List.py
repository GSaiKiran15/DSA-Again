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
elements = [1,2,3,4,5]
head = create_linked_list(elements)

def solution(head, n):
    count = 0
    node = ListNode(0, None)
    cur = head
    while cur.next:
        count += 1    
        if count == n:
            node = head
        elif count >= n:
            node = node.next
        print(count, cur.val, node.val)
        cur = cur.next
    node.next = node.next.next
    while head:
        print(head.val)
        head = head.next
solution(head, 2) 