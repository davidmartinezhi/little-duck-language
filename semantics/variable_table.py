# semantics/variable_table.py

class VariableTable:
    def __init__(self):
        # Structure: {scope: {var_name: {'type': var_type, 'initialized': bool}}}
        self.variables = {}
        self.current_scope = "global"

    def set_scope(self, scope):
        """
        Sets the current scope. Initializes the scope in the variable table if it doesn't exist.
        """
        self.current_scope = scope
        if scope not in self.variables:
            self.variables[scope] = {}

    def add_variable(self, scope, var_name, var_type):
        """
        Adds a variable to the specified scope with its type.
        """
        if scope not in self.variables:
            self.variables[scope] = {}
        self.variables[scope][var_name] = {'type': var_type, 'initialized': False}

    def get_variable_type(self, scope, var_name):
        """
        Retrieves the type of a variable from the specified scope.
        """
        return self.variables.get(scope, {}).get(var_name, {}).get('type')

    def find_scope(self, var_name):
        """
        Finds the scope in which a variable is declared.
        Searches from the current scope outward to the global scope.
        """
        scopes = list(self.variables.keys())
        if self.current_scope in scopes:
            scopes.remove(self.current_scope)
            scopes.insert(0, self.current_scope)
        for scope in scopes:
            if var_name in self.variables.get(scope, {}):
                return scope
        return None

    def is_initialized(self, scope, var_name):
        """
        Checks if a variable has been initialized.
        """
        return self.variables.get(scope, {}).get(var_name, {}).get('initialized', False)

    def set_initialized(self, scope, var_name):
        """
        Marks a variable as initialized.
        """
        if var_name in self.variables.get(scope, {}):
            self.variables[scope][var_name]['initialized'] = True

    def clean_variables(self, scope):
        """
        Removes all variables from the specified scope.
        """
        if scope in self.variables:
            del self.variables[scope]
