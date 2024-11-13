class VariableTable:
    def __init__(self):
        self.variables = {"global": {}}

    def set_scope(self, scope):
        if scope not in self.variables:
            self.variables[scope] = {}

    def add_variable(self, scope, name, var_type, address):
        if name in self.variables[scope]:
            raise Exception(f"Variable '{name}' is already declared in scope '{scope}'.")
        self.variables[scope][name] = {
            'type': var_type,
            'address': address
        }

    def get_variable_type(self, scope, name):
        return self.variables[scope][name].get('type', None)

    def get_variable_address(self, scope, name):
        return self.variables[scope][name].get('address', None)

    def clean_variables(self, scope):
        self.variables[scope].clear()

    def find_scope(self, name, current_scope):
        if name in self.variables.get(current_scope, {}):
            return current_scope
        elif name in self.variables.get("global", {}):
            return "global"
        return None
