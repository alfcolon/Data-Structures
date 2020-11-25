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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif self.right == None:
            self.right = BSTNode(value)
        else:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # node value check
        if target == self.value:
            return True
        # left check
        if target < self.value:
            return False if self.left == None else self.left.contains(target)
        # right check
        return False if self.right == None else self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        return self.value if self.right == None else self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left != None:
            self.left.for_each(fn)
        if self.right != None:
            self.right.for_each(fn)
            

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # I should use a linked list to speed this up
    def bft_print(self):
        queue = []
        queue.append(self)
        while len(queue):
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left != None:
                queue.append(current_node.left)
            if current_node.right != None:
                queue.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = []
        stack.append(self)
        while len(stack):
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left != None:
                stack.append(current_node.left)
            if current_node.right != None:
                stack.append(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        # pre for print yourself first
        print(self.value)
        if self.left != None:
            self.left.pre_order_dft()
        if self.right != None:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        # post for print yourself after
        if self.left != None:
            self.left.post_order_dft()
        if self.right != None:
            self.right.post_order_dft()
        print(self.value)

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
bst.in_order_print()
print("post order")
bst.post_order_dft()  
