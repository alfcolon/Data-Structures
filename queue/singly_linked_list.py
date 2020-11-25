
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # append/add --> add_to_tail
    def add_to_tail(self, value):
        new_node = Node(value, None)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif self.length == 1:
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1

        # remove
    def remove_head(self):
        if self.length == 0:
            return None
        
        current_head = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.length == 2:
            self.head = self.tail
        elif self.length > 2:
            self.head = self.head.next
            
        self.length -= 1
        
        return current_head.value
        
            
    def remove_tail(self):
        if self.length == 0:
            return None
        
        current_tail = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.length == 2:
            self.tail = self.head
        elif self.length > 2:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            self.tail = current_node
            
        self.length -= 1
        
        return current_tail.value
