class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_head(self, val):
        if self.head is None:
            self.head = Node(val, None, None)
        else:
            temp = self.head
            self.head = Node(val, None, temp)
        return self.head
    
    def get_length(self, position=None):
        if position and self.head:
            iterator = self.head
            length = 0
            node = None
            while iterator:
                if length == position - 1:
                    node = iterator                    
                iterator = iterator.next
                length += 1
            return (length, node)
        elif self.head:
            iterator = self.head
            length = 0
            while iterator:
                length += 1
                iterator = iterator.next
            return (length, None)
        return 0
    
    def insert_at(self, val, position):
        length, node = self.get_length(position)
        if position < 0 or position > length + 1:
            print("Position is Invalid !")
        elif position == 0:
            return self.insert_head(val)
        else:
            node.next = Node(val, node, node.next if node.next else None)
    
    def linked_list_log(self, direction=None):
        
        iterator = self.head
        output = []
        while iterator:
            output.append(f"{iterator.val}")
            iterator = iterator.next
        if direction:
            print('->'.join(reversed(output)))
        else:
            print('->'.join(output))

    def delete_at(self,position):
        length, node = self.get_length(position)
        if position < 0 or position > length + 1:
            print("Position is Invalid!")
        elif position == 0:
            self.head = self.head.next
        else:
            node.next = node.next.next
    
    
linked_list = LinkedList()
linked_list.insert_head(10)
linked_list.insert_head(8)
linked_list.insert_at(9,0)
linked_list.linked_list_log("r")
linked_list.delete_at(1)
linked_list.linked_list_log("r")