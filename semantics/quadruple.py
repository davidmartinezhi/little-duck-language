# semantics/quadruple.py

class Quadruple:
    def __init__(self):
        self.quadruples = []
        self.labels = {}
        self.label_counter = 0  # To ensure unique label names

    def push(self, quadruple):
        """
        Adds a quadruple to the list.
        """
        self.quadruples.append(quadruple)

    def add_label(self, label_name=None):
        """
        Assigns a label to the current position in the quadruples.
        If no label name is provided, generates a unique label.
        """
        if not label_name:
            label_name = f"label_{self.label_counter}"
            self.label_counter += 1
        self.labels[label_name] = len(self.quadruples)
        self.push(('label', label_name, None, None))
        return label_name

    def get_quadruples(self):
        """
        Returns the list of quadruples.
        """
        return self.quadruples

    def get_labels(self):
        """
        Returns the dictionary of labels with their positions.
        """
        return self.labels
