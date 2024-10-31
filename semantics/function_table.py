# semantics/function_table.py

class FunctionTable:
    def __init__(self):
        # Structure: {function_name: {'params': [{'name': param_name, 'type': param_type}], 'return_type': return_type}}
        self.functions = {}

    def add_function(self, function_name, return_type=None):
        """
        Adds a function to the function table.
        """
        if function_name not in self.functions:
            self.functions[function_name] = {'params': [], 'return_type': return_type}

    def add_function_param(self, function_name, param):
        """
        Adds a parameter to a specified function.
        """
        if function_name in self.functions:
            self.functions[function_name]['params'].append(param)

    def get_function(self, function_name):
        """
        Retrieves a function's details from the function table.
        """
        return self.functions.get(function_name, None)

    def get_function_params(self, function_name):
        """
        Retrieves the list of parameters for a specified function.
        """
        if function_name in self.functions:
            return self.functions[function_name]['params']
        return []

    def get_function_param_type(self, function_name, param_index):
        """
        Retrieves the type of a specific parameter in a function.
        """
        if function_name in self.functions and param_index < len(self.functions[function_name]['params']):
            return self.functions[function_name]['params'][param_index]['type']
        return None

    def get_function_param_id(self, function_name, param_index):
        """
        Retrieves the name of a specific parameter in a function.
        """
        if function_name in self.functions and param_index < len(self.functions[function_name]['params']):
            return self.functions[function_name]['params'][param_index]['name']
        return None
