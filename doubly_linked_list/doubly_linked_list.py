"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head == None:
            return None
        else:
            value = self.head.value
            self.delete(self.head)
            return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node 
            self.head = new_node
        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None
        if self.tail:
            value = self.tail.value
            self.delete(self.tail)
            return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        value = node.value
        if node is self.head:
            return 
        else:
            self.delete(node)
            self.add_to_head(value)

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        if self.head is None:
            return None
        if self.head == node:
            self.head = node.next
            node.delete()
        if self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # Checks if there is a node in this link list
        if self.head is None:
            # Returns none if no nodes found
            return None
        #Assigns the starting point for the while loop as the first nodes "next" assignment
        current = self.head.next
        #Assigns a variable to the first value in the loop
        max = self.head.value
        #Uses the iteratable "next" param as the iteratable
        while current:
            #Checks if the iteratables current value is greater than the current number being examined
            if current.value > max:
                #Assigns a new value to the comparable value (Stores the highest number found)
                max = current.value
            #Assigns the next node to iterate over
            current = current.next
        #Returns the highest value found
        return max