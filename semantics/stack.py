class Stack:
    """
    Class implementing a simple stack.
    """

    def __init__(self):
        self.stack = []

    def push(self, element):
        """
        Adds an element to the top of the stack.

        Args:
            element (Any): Element to add.
        """
        self.stack.append(element)

    def pop(self):
        """
        Removes and returns the element at the top of the stack.

        Returns:
            Any: Element at the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if not self.is_empty():
            return self.stack.pop()
        raise Exception("Stack is empty")

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return len(self.stack) == 0

    def peek(self):
        """
        Returns the element at the top of the stack without removing it.

        Returns:
            Any: Element at the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if not self.is_empty():
            return self.stack[-1]
        raise Exception("Stack is empty")