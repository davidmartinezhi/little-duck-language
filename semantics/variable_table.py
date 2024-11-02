class VariableTable:
    """
    Class representing the variable table used by the compiler to manage variables
    in different scopes (e.g., global and local scopes). This table keeps track of
    variable names, types, memory addresses, and values.
    """

    def __init__(self):
        """
        Initialize the VariableTable with a 'global' scope.
        """
        self.variables = {"global": {}}

    def set_scope(self, scope):
        """
        Create a new scope in the variable table if it doesn't already exist.
        """
        if scope not in self.variables:
            # Initialize a new scope with an empty dictionary
            self.variables[scope] = {}

    def add_variable(self, scope, name, var_type):
        """
        Add a new variable to the specified scope in the variable table.
        """
        if name in self.variables[scope]:
            raise Exception(f"Variable '{name}' is already declared in scope '{scope}'.")
        # Assign the variable to the corresponding scope and save its type
        self.variables[scope][name] = {
            'type': var_type
        }

    def get_variable_type(self, scope, name):
        """
        Retrieve the type of a variable from the specified scope.
        """
        return self.variables[scope][name].get('type', None)

    def clean_variables(self, scope):
        """
        Clear all variables from the specified scope.
        """
        self.variables[scope].clear()

    def find_scope(self, name, current_scope):
        """
        Search for the scope where a variable with the given name is declared.

        Args:
            name (str): The name of the variable to search for.
            current_scope (str): The current scope to check first.

        Returns:
            str or None: The name of the scope where the variable is found,
                         or None if the variable is not found in any scope.
        """
        # Check current scope first
        if name in self.variables.get(current_scope, {}):
            return current_scope
        # Then check global scope
        elif name in self.variables.get("global", {}):
            return "global"
        # Variable not found
        return None
