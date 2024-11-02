class Stack:
    """
    Class implementing a simple stack.
    """

    def __init__(self):
        self.stack = []

    def push(self, element):
        """
        Add an element to the top of the stack.
        """
        self.stack.append(element)

    def pop(self):
        """
        Remove and return the element at the top of the stack.
        """
        if not self.is_empty():
            return self.stack.pop()
        raise Exception("Cannot pop from empty stack.")

    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.stack) == 0

    def peek(self):
        """
        Return the element at the top of the stack without removing it.
        """
        if not self.is_empty():
            return self.stack[-1]
        raise Exception("Cannot peek into empty stack.")
