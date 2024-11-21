class VariableTable:
    """
    Class representing the variable table (symbol table) used in the compiler.
    This table keeps track of all variables declared in different scopes along with their types and memory addresses.
    """

    def __init__(self):
        """
        Initializes the variable table with a global scope.
        The 'variables' attribute is a dictionary where each key is a scope name, and the value is another dictionary
        containing variable names as keys and their attributes (type and address) as values.
        """
        self.variables = {"global": {}}

    def set_scope(self, scope):
        """
        Adds a new scope to the variable table if it doesn't already exist.

        Args:
            scope (str): The name of the scope to add.
        """
        if scope not in self.variables:
            self.variables[scope] = {}

    def add_variable(self, scope, name, var_type, address):
        """
        Adds a new variable to the variable table under the specified scope.

        Args:
            scope (str): The scope in which the variable is declared.
            name (str): The name of the variable.
            var_type (str): The data type of the variable (e.g., 'entero', 'flotante').
            address (int): The virtual memory address assigned to the variable.

        Raises:
            Exception: If the variable is already declared in the given scope.
        """
        if name in self.variables[scope]:
            raise Exception(f"Variable '{name}' is already declared in scope '{scope}'.")
        self.variables[scope][name] = {
            'type': var_type,
            'address': address
        }

    def get_variable_type(self, scope, name):
        """
        Retrieves the data type of a variable in the specified scope.

        Args:
            scope (str): The scope where the variable is declared.
            name (str): The name of the variable.

        Returns:
            str or None: The data type of the variable if found, otherwise None.
        """
        return self.variables[scope][name].get('type', None)

    def get_variable_address(self, scope, name):
        """
        Retrieves the virtual memory address of a variable in the specified scope.

        Args:
            scope (str): The scope where the variable is declared.
            name (str): The name of the variable.

        Returns:
            int or None: The virtual memory address of the variable if found, otherwise None.
        """
        return self.variables[scope][name].get('address', None)

    def clean_variables(self, scope):
        """
        Clears all variables in the specified scope.
        This is useful when exiting a scope to remove local variables.

        Args:
            scope (str): The scope whose variables are to be cleared.
        """
        self.variables[scope].clear()

    def find_scope(self, name, current_scope):
        """
        Searches for the scope in which a variable is declared.
        It first checks the current scope, then the global scope.

        Args:
            name (str): The name of the variable to search for.
            current_scope (str): The current scope during execution.

        Returns:
            str or None: The scope where the variable is found ('current_scope' or 'global'), or None if not found.
        """
        if name in self.variables.get(current_scope, {}):
            return current_scope
        elif name in self.variables.get("global", {}):
            return "global"
        return None

    def clean_variables(self, scope):
        """
        Clears all variables in the specified scope.
        This is useful when exiting a scope to remove local variables.

        Args:
            scope (str): The scope whose variables are to be cleared.
        """
        if scope in self.variables:
            del self.variables[scope]