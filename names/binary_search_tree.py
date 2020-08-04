class Queue:
    def __init__(self):
        self.storage = list()

    def enqueue(self, value):
        self.storage.insert(0, value)

    def dequeue(self):
        if len(self.storage) > 0:
            return self.storage.pop()


class Stack:
    def __init__(self):
        self.storage = list()

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value == value:
            return None
        elif value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        if self:
            if self.left:
                self.left.in_order_print()
            if self.right:
                self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        queue = Queue()
        queue.enqueue(bst)
        while queue is not None:
            # remove the first node from the queue
            cur_node = queue.dequeue()
            # print the removed node
            print(cur_node.value)
            # add all children (of removed node) into the queue
            if cur_node.left:
                queue.enqueue(cur_node.left)
            if cur_node.right:
                queue.enqueue(cur_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        stack = Stack()
        stack.push(bst)
        while len(stack.storage) > 0:
            current = stack.pop()
            print(current.value)
            if current.right:
                stack.push(current.right)
            if current.left:
                stack.push(current.left)
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass
