class VariableTable:
    """
    Class representing the variable table used by the compiler to manage variables
    in different scopes (e.g., global and local scopes). This table keeps track of
    variable names, types, memory addresses, and values.

    Attributes:
    variables (dict): A dictionary where keys are scope names and values are
                      dictionaries of variables in that scope.
    """

    def __init__(self):
        """
        Initializes the VariableTable with a 'global' scope.
        """
        self.variables = {"global": {}}

    def set_scope(self, scope):
        """
        Creates a new scope in the variable table if it doesn't already exist.

        Args:
            scope (str): The name of the new scope to be added.

        Complexity:
            runtime: O(1)
        """
        if scope not in self.variables:
            # Initialize a new scope with an empty dictionary
            self.variables[scope] = {}

    def add_variable(self, scope, name, var_type):
        """
        Adds a new variable to the specified scope in the variable table.

        Args:
            scope (str): The scope in which the variable is declared.
            name (str): The name of the variable.
            var_type (str): The data type of the variable (e.g., 'int', 'float').

        Raises:
            Exception: If the variable already exists in the given scope.

        Complexity:
            runtime: O(1)
        """
        if name in self.variables[scope]:
            # Variable already declared in this scope
            raise Exception(f"Variable {name} already declared.")
        # Assign the variable to the corresponding scope and save its type
        self.variables[scope][name] = {
            'type': var_type
        }

    def get_variable_type(self, scope, name):
        """
        Retrieves the type of a variable from the specified scope.

        Args:
            scope (str): The scope in which to look for the variable.
            name (str): The name of the variable.

        Returns:
            str or None: The type of the variable if found, else None.

        Complexity:
            runtime: O(1)
        """
        return self.variables[scope][name].get('type', None)

    def get_variable_value(self, scope, name):
        """
        Retrieves the current value of a variable from the specified scope.

        Args:
            scope (str): The scope in which to look for the variable.
            name (str): The name of the variable.

        Returns:
            Any or None: The value of the variable if it has been set, else None.

        Complexity:
            runtime: O(1)
        """
        return self.variables[scope][name].get('value', None)

    def set_variable_value(self, scope, name, value):
        """
        Sets or updates the value of a variable in the specified scope.

        Args:
            scope (str): The scope in which the variable exists.
            name (str): The name of the variable.
            value (Any): The value to assign to the variable.

        Complexity:
            runtime: O(1)
        """
        self.variables[scope][name]['value'] = value

    def clean_variables(self, scope):
        """
        Clears all variables from the specified scope.

        Args:
            scope (str): The scope from which to remove all variables.

        Complexity:
            runtime: O(n), n being the number of variables
        """
        self.variables[scope].clear()

    def find_scope(self, name):
        """
        Searches for the scope where a variable with the given name is declared.

        Args:
            name (str): The name of the variable to search for.

        Returns:
            str or None: The name of the scope where the variable is found,
                         or None if the variable is not found in any scope.

        Complexity:
            runtime: O(n), with n being the number of scopes
        """
        # Iterate over all scopes to find the variable
        for scope in self.variables:
            if name in self.variables[scope]:
                return scope  # Return the scope where the variable is found
        return None  # Variable not found in any scope
