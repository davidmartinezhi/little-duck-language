# function_table.py

class FunctionTable:
    def __init__(self):
        self.functions = {}  # Stores function information

    def add_function(self, func_name, quad_start):
        if func_name in self.functions:
            raise Exception(f"Function '{func_name}' is already declared.")
        self.functions[func_name] = {
            'quad_start': quad_start,
            'params': []
        }

    def add_parameter(self, func_name, param_name, param_type, param_address):
        if func_name not in self.functions:
            raise Exception(f"Function '{func_name}' is not declared.")
        self.functions[func_name]['params'].append({
            'name': param_name,
            'type': param_type,
            'address': param_address
        })

    def get_function(self, func_name):
        if func_name not in self.functions:
            raise Exception(f"Function '{func_name}' is not declared.")
        return self.functions[func_name]

    def get_function_param_count(self, func_name):
        if func_name not in self.functions:
            raise Exception(f"Function '{func_name}' is not declared.")
        return len(self.functions[func_name]['params'])

    def get_function(self, func_id):
        """
        Retrieves the function information from the function table.

        Args:
            func_id (str): The identifier (name) of the function.

        Returns:
            dict: The function's information dictionary if found.

        Raises:
            Exception: If the function is not found.
        """
        if func_id not in self.functions:
            raise Exception(f"Function '{func_id}' not found in function table.")
        return self.functions[func_id]

    def get_function_param_count(self, func_id):
        """
        Retrieves the number of parameters for a specified function.

        Args:
            func_id (str): The identifier (name) of the function.

        Returns:
            int: The number of parameters the function has.

        Raises:
            Exception: If the function is not found.
        """
        if func_id not in self.functions:
            raise Exception(f"Function '{func_id}' not found in function table.")
        return len(self.functions[func_id]["params"])

    def clean_functions(self):
        """
        Clears all functions from the function table.
        """
        self.functions.clear()
