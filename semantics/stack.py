# semantics/stack.py

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Pushes an item onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Pops the top item from the stack.
        Raises an exception if the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        """
        Peeks at the top item of the stack without removing it.
        Raises an exception if the stack is empty.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception("Stack is empty")

    def is_empty(self):
        """
        Checks if the stack is empty.
        """
        return len(self.items) == 0
