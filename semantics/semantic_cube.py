class SemanticCube:
    """
    Class representing the semantic cube used to verify variable types and operations
    in the compiler. The semantic cube defines the result type of an operation given
    the operand types and the operator. It is essential for type checking during
    semantic analysis.

    Attributes:
        cube (dict): A dictionary mapping a tuple of (left_type, right_type, operator)
                     to the resulting type or 'error' if the operation is invalid.
    """

    def __init__(self):
        """
        Initializes the SemanticCube with predefined type combinations and their
        resulting types for various operations.
        """
        self.cube = {
            # Addition operations
            ('entero', 'entero', '+'): 'entero',        # Example: 5 (entero) + 3 (entero) -> 8 (entero)
            ('entero', 'flotante', '+'): 'flotante',    # Example: 5 (entero) + 3.5 (flotante) -> 8.5 (flotante)
            ('flotante', 'entero', '+'): 'flotante',    # Example: 5.5 (flotante) + 3 (entero) -> 8.5 (flotante)
            ('flotante', 'flotante', '+'): 'flotante',  # Example: 5.5 (flotante) + 3.5 (flotante) -> 9.0 (flotante)

            # Subtraction operations
            ('entero', 'entero', '-'): 'entero',        # Example: 5 (entero) - 3 (entero) -> 2 (entero)
            ('entero', 'flotante', '-'): 'flotante',    # Example: 5 (entero) - 3.5 (flotante) -> 1.5 (flotante)
            ('flotante', 'entero', '-'): 'flotante',    # Example: 5.5 (flotante) - 3 (entero) -> 2.5 (flotante)
            ('flotante', 'flotante', '-'): 'flotante',  # Example: 5.5 (flotante) - 3.5 (flotante) -> 2.0 (flotante)

            # Multiplication operations
            ('entero', 'entero', '*'): 'entero',        # Example: 5 (entero) * 3 (entero) -> 15 (entero)
            ('entero', 'flotante', '*'): 'flotante',    # Example: 5 (entero) * 3.5 (flotante) -> 17.5 (flotante)
            ('flotante', 'entero', '*'): 'flotante',    # Example: 5.5 (flotante) * 3 (entero) -> 16.5 (flotante)
            ('flotante', 'flotante', '*'): 'flotante',  # Example: 5.5 (flotante) * 3.5 (flotante) -> 19.25 (flotante)

            # Division operations
            ('entero', 'entero', '/'): 'entero',        # Example: 6 (entero) / 3 (entero) -> 2 (entero)
            ('entero', 'flotante', '/'): 'flotante',    # Example: 5 (entero) / 2.0 (flotante) -> 2.5 (flotante)
            ('flotante', 'entero', '/'): 'flotante',    # Example: 5.5 (flotante) / 2 (entero) -> 2.75 (flotante)
            ('flotante', 'flotante', '/'): 'flotante',  # Example: 5.5 (flotante) / 2.2 (flotante) -> 2.5 (flotante)

            # Less than comparison
            ('entero', 'entero', '<'): 'bool',       # Example: 5 (entero) < 3 (entero) -> False (bool)
            ('entero', 'flotante', '<'): 'bool',     # Example: 5 (entero) < 5.5 (flotante) -> True (bool)
            ('flotante', 'entero', '<'): 'bool',     # Example: 5.5 (flotante) < 6 (entero) -> True (bool)
            ('flotante', 'flotante', '<'): 'bool',   # Example: 5.5 (flotante) < 5.5 (flotante) -> False (bool)

            # Greater than comparison
            ('entero', 'entero', '>'): 'bool',       # Example: 5 (entero) > 3 (entero) -> True (bool)
            ('entero', 'flotante', '>'): 'bool',     # Example: 5 (entero) > 5.5 (flotante) -> False (bool)
            ('flotante', 'entero', '>'): 'bool',     # Example: 5.5 (flotante) > 6 (entero) -> False (bool)
            ('flotante', 'flotante', '>'): 'bool',   # Example: 5.5 (flotante) > 5.0 (flotante) -> True (bool)

            # Not equal comparison
            ('entero', 'entero', '!='): 'bool',      # Example: 5 (entero) != 3 (entero) -> True (bool)
            ('entero', 'flotante', '!='): 'bool',    # Example: 5 (entero) != 5.0 (flotante) -> False (bool)
            ('flotante', 'entero', '!='): 'bool',    # Example: 5.5 (flotante) != 5 (entero) -> True (bool)
            ('flotante', 'flotante', '!='): 'bool',  # Example: 5.5 (flotante) != 5.5 (flotante) -> False (bool)

            # Equal comparison
            ('entero', 'entero', '=='): 'bool',      # Example: 5 (entero) == 5 (entero) -> True (bool)
            ('entero', 'flotante', '=='): 'bool',    # Example: 5 (entero) == 5.0 (flotante) -> True (bool)
            ('flotante', 'entero', '=='): 'bool',    # Example: 5.5 (flotante) == 5 (entero) -> False (bool)
            ('flotante', 'flotante', '=='): 'bool',  # Example: 5.5 (flotante) == 5.5 (flotante) -> True (bool)

            # Assignment operations
            ('entero', 'entero', '='): 'entero',        # Example: int_var (entero) = 5 (entero) -> Valid, int_var is entero
            ('entero', 'flotante', '='): 'error',    # Example: int_var (entero) = 5.5 (flotante) -> Error, cannot assign flotante to entero
            ('flotante', 'entero', '='): 'flotante',    # Example: float_var (flotante) = 5 (entero) -> Valid, float_var is flotante
            ('flotante', 'flotante', '='): 'flotante',  # Example: float_var (flotante) = 5.5 (flotante) -> Valid, float_var is flotante
        }

    def get_type(self, left_type, right_type, operator):
        """
        Retrieves the resulting type of an operation given the types of the left and
        right operands and the operator. If the operation is invalid, raises a TypeError.

        Args:
            left_type (str): The type of the left operand (e.g., 'entero', 'flotante').
            right_type (str): The type of the right operand.
            operator (str): The operator being applied (e.g., '+', '-', '*', '/', '<', '>', '!=', '=').

        Returns:
            str: The resulting type of the operation (e.g., 'entero', 'flotante', 'bool').

        Raises:
            TypeError: If the operation is invalid according to the semantic cube.

        Complexity:
            runtime: O(1), we look for a value in a dictionary
        """
        # Look up the result type in the semantic cube dictionary
        result = self.cube.get((left_type, right_type, operator), 'error')  # Return result type or 'error'
        if result == 'error':
            # If the operation is invalid, raise a TypeError
            raise TypeError(f"Invalid operation: Cannot perform '{operator}' between types '{left_type}' and '{right_type}'.")
        return result
