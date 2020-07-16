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
        # compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # we need to move left
            # if we see that there is no left child, then we can wrap the
            if self.left is None:
            # value in a BSTNode and park it.
                self.left = BSTNode(value)
            # otherwise there is a child
            else:
            # call the left childs insert method
                self.left.insert(value)
        # otherwise, value >= Nodes value
        else:
            # we need to move right
            if self.right is None:
            # if we see there is no right child, then we can wrap the
            # value in a BSTNode and park it.
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
            # call the rights childs insert method
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    # contains == search, similar to insert method
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

        # my solution
        # if target < self.value:
        #     if self.left is None:
        #         return False
        #     return self.left.contains(target)
        # elif target > self.value:
        #     if self.right is None:
        #         return False
        #     return self.right.contains(target)
        # else:
        #     return True

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    # recursive version
    def for_each(self, fn):
        #call the anonymous function on 'self.value'
        fn(self.value)
        #if this node has a left child
        if self.left:
            # pass the anonymous fn to it
            self.left.for_each(fn)
        # if this node has a right child
        if self.right:
            # pass the anonymous fn to it
            self.right.for_each(fn)

    # # iterative depth first for each
    # #DFT: LIFO
    # def for_each(self, fn):
    #     # we use a stack
    #     stack = []
    #     stack.append(self)
    #
    #     # so long as our stack has nodes in it,
    #     # there's more nodes to traverse
    #     while len(stack) > 0:
    #         # pop the top node from the Stack
    #         current = stack.pop()
    #
    #         # add the current nodes right child first
    #         if current.right:
    #             stack.append(current.stack)
    #
    #         # add the current nodes left child
    #         if current.left:
    #             stack.append(current.left)
    #         # call the anonymous function fn()
    #         fn(current.value)
    #
    #
    # # iterative breadth first for each
    # # BFT: FIFO
    # def for_each(self, fn):
    #     from collections import deque
    #
    #     # use a queue to facilitate the ordering
    #     queue = deque()
    #     queue.append(self)
    #
    #     # continue to traverse so long as there
    #     # are nodes in the queue
    #     while len(queue) > 0:
    #         current = queue.popleft()
    #
    #         if current.left:
    #             queue.append(current.left)
    #
    #         if current.right:
    #             queue.append(current.right)
    #
    #         fn(current.value)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):

        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # iterative breadth first for each
    # BFT: FIFO
    # def for_each(self, fn):
    #     from collections import deque
    #
    #     # use a queue to facilitate the ordering
    #     queue = deque()
    #     queue.append(self)
    #
    #     # continue to traverse so long as there
    #     # are nodes in the queue
    #     while len(queue) > 0:
    #         current = queue.popleft()
    #
    #         if current.left:
    #             queue.append(current.left)
    #
    #         if current.right:
    #             queue.append(current.right)
    #
    #         fn(current.value)



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque
        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(self)

        while len(stack) > 0:
            current = stack.pop()

            if current.left:
                stack.append(current.left)
                
            if current.right:
                stack.append(current.right)

            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# root = BSTNode(26)





#end
