class VariableTable:
    """
    Class representing the symbol table used by the compiler to manage variables.
    It stores information about variables such as their type, scope, and memory address.

    Attributes:
        variables (dict): A dictionary where each key is a scope name,
                          and each value is another dictionary mapping variable names
                          to their attributes.
    """

    def __init__(self):
        """
        Initializes the VariableTable with an empty variables dictionary.
        """
        self.variables = {}
        self.current_scope = "global"  # Default initial scope

    def set_scope(self, scope_name):
        """
        Sets the current scope. If the scope doesn't exist, it is created.

        Args:
            scope_name (str): The name of the scope to set.
        """
        self.current_scope = scope_name
        if scope_name not in self.variables:
            self.variables[scope_name] = {}

    def add_variable(self, scope, var_name, var_type, address):
        """
        Adds a variable to the symbol table.

        Args:
            scope (str): The scope of the variable ('global' or function name).
            var_name (str): The name of the variable.
            var_type (str): The type of the variable ('entero', 'flotante', 'bool').
            address (int): The virtual memory address of the variable.
        """
        if scope not in self.variables:
            self.variables[scope] = {}
        self.variables[scope][var_name] = {
            'type': var_type,
            'address': address
        }

    def find_scope(self, var_name, current_scope):
        """
        Finds the scope in which a variable is declared.

        Args:
            var_name (str): The name of the variable.
            current_scope (str): The current scope.

        Returns:
            str: The scope where the variable is found, or None if not found.
        """
        # Check current scope first
        if var_name in self.variables.get(current_scope, {}):
            return current_scope

        # Check global scope
        if var_name in self.variables.get("global", {}):
            return "global"

        return None

    def get_variable_type(self, scope, var_name):
        """
        Retrieves the type of a variable.

        Args:
            scope (str): The scope of the variable.
            var_name (str): The name of the variable.

        Returns:
            str: The type of the variable.
        """
        return self.variables[scope][var_name]['type']

    def get_variable_address(self, scope, var_name):
        """
        Retrieves the memory address of a variable.

        Args:
            scope (str): The scope of the variable.
            var_name (str): The name of the variable.

        Returns:
            int: The memory address of the variable.
        """
        return self.variables[scope][var_name]['address']

    def clean_variables(self, scope):
        """
        Cleans up all variables in a given scope.

        Args:
            scope (str): The scope to clean.
        """
        if scope in self.variables:
            del self.variables[scope]
