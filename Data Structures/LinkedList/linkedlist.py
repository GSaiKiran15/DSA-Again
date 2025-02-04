class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def get_length(self):
        iterator = self.head
        length = 0
        while iterator:
            length += 1
            iterator = iterator.next
        return length
    
    #Insertions
    
    def insert_head(self, value):
        self.head = Node(value, self.head)
    
    def insert_end(self, value):
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(value, None)
        print(iterator.value)
        return self.head
    
    def insert_at(self, position, value):
        length = self.get_length()
        print(length)
        if position > length:
            self.insert_end(value)
            return
        index = 0
        iterator = self.head
        while index < position - 1:
            index += 1
            iterator = iterator.next
        iterator.next = Node(value, iterator.next)          
    
    def log_linked_list(self):
        output = ""
        iterator = self.head
        while iterator:
            output += str(iterator.value)
            if iterator.next:
                output += " -> "
            iterator = iterator.next
        print(output)

        

linked_list = LinkedList()
linked_list.insert_head(3)
linked_list.insert_head(2)
linked_list.insert_head(1)
linked_list.insert_end(4)
linked_list.log_linked_list()
linked_list.get_length()
