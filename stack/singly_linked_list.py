class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        #Creates a new node with a value and a next_node assignment as None. (A None assignment makes it the last node in the list)
        new_node = Node(value, None)
        # Checks the linklist for a self.head assignment and if its not there assigns the new_node to the LinkLinst
        if not self.head:
            self.head = new_node
            self.tail = new_node
         
        else:
        #Otherwise reassigns the next_node in the last node as the new_node
            self.tail.set_next(new_node)
        #And renames the tail in the LinkedList as the new_node
            self.tail = new_node

    def add_to_head(self, value):
        #Creates a new node
        new_node = Node(value)
        # Checks the list for a node
        if not self.head and not self.tail:
        #If there isn't a node then this assigns a new node by assigning the head and tail to the new_node
            self.head = new_node
            self.tail = new_node
        #If there is a head and tail then this....
        else:
        #Assigns the new_node's next paramater to the existing node (WHich is assigned by the LinkLists "head")
            new_node.set_next(self.head)
        #Assigns the head in the LinkList as the new_node
            self.head = new_node


    def remove_head(self):
        #Checks if there is a self.head and returns None if not found
        if not self.head:
            return None
        #Checks if there is a self.head.next_node in the linkedList and if there isnt it sets the head and tail to None and returns the value of the removed node.
        if not self.head.get_next():
        #Assigns variable head to be self.head for calling at the end of remove operation
            head = self.head
        #Assigns self.head to be None
            self.head = None
        #Assigns self.tail to be None
            self.tail = None
        #Returns the value of the head
            return head.get_value()
        #If there is a node with a head and a next_node it sets a variable "value" and assigns it the value for recalling a the end of the operation
        value = self.head.get_value()
        #Assigns the self.head to the next_node so the second node now becomes the first
        self.head = self.head.get_next()
        #Calls removed head node
        return value


    def contains(self, value):
        #Checks if there is a Head in the linkedList. Returns False if no Head is found
        if not self.head:
            return False
        #Assigns variable current to the self.head so a while loop can be performed to find if the value contains the query.
        current = self.head

        #While loop to check if self.head node's get_value() equals the queried value
        while current:
            if current.get_value() == value:
            #Returns true if query is matched
                return True
            #Assigns the current nodes next_node to the variable "current" so it will continue to loop over and search each notes value for the query
            current = current.get_next()
        #Returns False if the query is not found
        return False