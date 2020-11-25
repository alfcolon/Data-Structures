"""
Each ListNode holds a reference to its prev node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        # technically a head node of a lengthy linked list could be passed in
        # so I should be iterating through it to get the last node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's prev pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif self.length == 1:
            self.head.prev = new_node
            self.tail = self.head
            self.head = new_node
        elif self.length > 1:
            self.head.prev = new_node
            self.head = new_node
        
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        head_node = self.head
        
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.length == 2:
            self.head = self.tail
            self.head.prev = None
        elif self.length > 2:
            self.head = self.head.next
            self.head.prev = None
        
        self.length -= 1
        return head_node.value
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif self.length == 1:
            self.head.next = new_node
            self.tail = new_node
            self.tail.prev = self.head
            self.tail.next = None
        elif self.length >= 2:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's prev node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        removed_node = None
        
        if self.length == 0:
            return None
        elif self.length == 1:
            removed_node = self.head
            self.head = None
            self.tail = None
        elif self.length == 2:
            removed_node = self.tail
            self.tail = None
            self.head.next = None
        elif self.length > 2:
            removed_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.length -= 1
        return removed_node.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 2 and node != self.head:
            old_tail = self.tail
            self.tail = self.head
            self.head = old_tail
            
            self.head.prev = None
            self.head.next = self.tail
            
            self.tail.prev = self.head
            self.tail.next = None
        elif self.length > 2:
            node.prev.next = node.next
            node.next.prev = node.prev
            
            node.next = self.head
            node.prev = None
            
            self.head.prev = node
            self.head = node
            
            
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length == 2 and node != self.tail:
            old_tail = self.tail
            self.tail = self.head
            self.head = old_tail
            
            self.head.prev = None
            self.head.next = self.tail
            
            self.tail.prev = self.head
            self.tail.next = None
        elif self.length > 2:
            node.prev.next = node.next
            node.next.prev = node.prev
            
            node.next = None
            node.prev = self.tail
            
            self.tail.next = node
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
        elif self.length == 2:
            if node == self.head:
                self.head = self.tail
                self.head.prev = None
                self.tail = self.head
            elif node == self.tail:
                self.tail = self.head
        elif self.length > 2:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = 0
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head.value
        else:
            index = 0
            current_node = self.head
            while current_node != None:
                current_node_value = current_node.value
                if current_node_value > max_value:
                    max_value = current_node_value
                current_node = current_node.next
                index += 1
        return max_value

