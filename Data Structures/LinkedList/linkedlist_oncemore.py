class Node:
    def __init__(self, prev, value, next):
        self.prev = prev
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_head(self, value):
        if not self.head:
            self.head = Node(None, value, None)
        else:
            self.head = Node(None, value, self.head)
    
    def get_length(self):
        itr = self.head
        length = 0
        while itr:
            length += 1
            itr = itr.next
        return length
    
    def add_at(self, value, position):
        length = self.get_length()
        if length < position or position < 0:
            print("Invalid Position")
            return None
        elif position == 0:
            self.add_head(value)
        else:
            itr = self.head
            count = 1
            while itr:
                if count == position:
                    itr.next = Node(itr, value, itr.next)
                    break
                count += 1
                itr = itr.next
        return
    
    def log_list(self):
        itr = self.head
        while itr:
            print(itr.value)
            itr = itr.next

    def reverse_linked_list(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        self.log_list()
    
ll = LinkedList()
ll.add_head(10)
ll.add_head(9)
ll.add_head(8)
ll.add_head(7)
ll.add_head(6)
ll.add_head(5)
ll.add_head(4)
ll.reverse_linked_list()