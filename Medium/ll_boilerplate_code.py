class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_linkedlist(self, head):
        """ Print elements of linked list """
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
    
    def partition(self, head: 'Optional[ListNode]', x: int) -> 'Optional[ListNode]':
        # Placeholders for the start of "less than" and "greater than or equal to" lists
        left_list = ListNode(0)
        left_list_iterator = left_list
        right_list = ListNode(0)
        right_list_iterator = right_list
        while head:
            if head.val < x:
                left_list_iterator.next = head
                left_list_iterator = left_list_iterator.next
            else:
                right_list_iterator.next = head
                right_list_iterator = right_list_iterator.next
            head = head.next
        left_list_iterator.next = right_list.next
        right_list_iterator.next = None
        return left_list.next
        
        
def list_to_linkedlist(elements):
    """ Convert list to linked list """
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linkedlist(head):
    """ Print elements of linked list """
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
if __name__ == "__main__":
    input_list = [1, 4, 3, 2, 5, 2]
    x = 6
    head = list_to_linkedlist(input_list)

    sol = Solution()
    new_head = sol.partition(head, x)

    print_linkedlist(new_head)
