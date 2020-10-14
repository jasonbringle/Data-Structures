"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the new nodes value is less than the current nodes value
        if value < self.value:
            # if there is no left child already here
            if not self.left:
                # add the new node to the left
                # create a BSTNode and encapsulate the value in it then set it to the left
                self.left = BSTNode(value)
            # otherwise call insert on the left node
            else:
                self.left.insert(value)
        # otherwise (the new nodes value is greaterthan or equal to the current node value)
        else:
            # if there is no right child already here
            if self.right == None:
                # add the new node to the right
                # create a BSTNode and encapsulate the value in it then set it to the right
                self.right == BSTNode(value)
            # otherwise call insert on the right node
            else:
                self.right.insert(value)
       

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value of the current node matches the target
        if self.value == target:
            # return True
            return True

        # check if the target is less than the current nodes value
        if target < self.value:
            # if there is no left child already here
            if not self.left:
                # return False
                return False
            # otherwise
            else:
                # return a call of contains on the left child passing in the target value
                self.left.contains(target)
        # otherwise (the target is greater than the current nodes value)
        if target > self.value:
            # if there is no right child already here
            if self.right == None:
                # return False
                return False
            # otherwise
            else:
                # return a call of contains on the right child passing in the target value
                self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # check for an empty tree
        if self.value == None:
            # return None
            return None

        # ----------------------------------------------
        # recursive approach
        # check if there is no node to the right
        if not self.right:
            # return the nodes value
            return self.value
        # return a call to get max on the right child
        else:
            self.right.get_max()
        # -----------------------------------------------

        # iterative aproach

        # initialise the max value
        max = 0

        # get a ref to the current node
        current = self.value

        # loop while there is still a current node
        while current:
            # if the current value is greater than the max value, update the max value
            if current > max:
                max = self.right
            # move on to the next right node
            current = self.right
        
        # return the max value
        return max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function passing in the current nodes value
        fn(self.value)
        # if there is a node to the left
        if self.left:
            # call the function on the left value
            self.left.for_each(fn)
        
        # if there is a node to the right
        if self.right:
            # call the function on the right node
            self.right.for_each(fn)
            
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        #base case
        # if there are no nodes
        if not self:
            #return
            return
        #if there is a node to the left
        if self.left:
            #call in_order_print on the left
            self.left.in_order_print()
        # print the value of the current node(self.value)
        print(self.value)
        #if the re is a node to the right
        if self.right:
            #call in_order_print on the right
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self): #use a queue
        #Create a queue
        q = Queue()
        # enqueue the first node (self)
        q.enqueue(self)
        # while there is data in the queue
        while len(q) > 0:
            # deque from queue on to current_node
            current = q.dequeue()
            # print the curent_node value
            print(current.value)
            # if the current_node has a left child
            if current.left:
                # enque the left child
                q.enqueue(current.left)
            # if the current node has a right child
            if current.right:
                #enque the right child
                q.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self): #use a stack
        #Create a stack
        s = Stack()
        # push the first node (self)
        s.push(self)
        # while there is data in the stack
        while len(s) > 0:
            # pop from stack on to current_node
            current = s.pop()
            # print the cureent_node value
            print(current.value)
            # if the current_node has a left child
            if current.left:
                # push the left child
                s.push(current.left)
            # if the current node has a right child
            if current.right:
                #push the right child
                s.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
