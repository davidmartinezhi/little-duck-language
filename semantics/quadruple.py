class Quadruple:
    """
    A class to manage a collection of quadruples.

    Attributes:
        quadruples (list): A list that stores the quadruples.
        quadruple_count (int): A counter for the number of quadruples stored.
    """

    def __init__(self):
        """Initializes the instance with an empty list and sets the counter to zero."""
        self.quadruples = []
        self.quadruple_count = 0

    def push(self, quadruple):
        """
        Adds a quadruple to the list and increments the counter.

        Args:
            quadruple: The quadruple to be added to the list.
        """
        self.quadruples.append(quadruple)
        self.quadruple_count += 1
