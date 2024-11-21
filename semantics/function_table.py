class FunctionTable:
    """
    Class to manage function declarations and their attributes within the compiler.

    Attributes:
        functions (dict): A dictionary storing function information.
                          Key: Function name (str)
                          Value: Dictionary containing:
                                 - 'quad_start' (int): The starting index of the function's quadruples.
                                 - 'params' (list): A list of dictionaries for each parameter with keys:
                                                   'name' (str), 'type' (str), 'address' (int)
    """
    def __init__(self):
        """
    Initializes the FunctionTable with an empty functions dictionary.
    """
        self.functions = {}  # Stores function information

    def add_function(self, func_name, quad_start):
        """
        Adds a new function to the function table.

        Args:
            func_name (str): The name of the function to add.
            quad_start (int): The starting index of the function's quadruples.

        Raises:
            Exception: If the function is already declared.
        """
        if func_name in self.functions:
            raise Exception(f"Function '{func_name}' is already declared.")
        self.functions[func_name] = {
            'quad_start': quad_start,
            'params': []
        }

    def add_parameter(self, func_name, param_name, param_type, param_address):
        """
        Adds a parameter to a specified function.

        Args:
            func_name (str): The name of the function to which the parameter is added.
            param_name (str): The name of the parameter.
            param_type (str): The data type of the parameter ('entero', 'flotante', 'bool', etc.).
            param_address (int): The virtual memory address allocated for the parameter.

        Raises:
            Exception: If the function is not declared.
        """
        if func_name not in self.functions:
            raise Exception(f"Function '{func_name}' is not declared.")
        self.functions[func_name]['params'].append({
            'name': param_name,
            'type': param_type,
            'address': param_address
        })

    def get_function(self, func_name):
        """
        Retrieves the function information from the function table.

        Args:
            func_id (str): The identifier (name) of the function.

        Returns:
            dict: The function's information dictionary if found.

        Raises:
            Exception: If the function is not found.
        """
        if func_name not in self.functions:
            raise Exception(f"Function '{func_name}' is not declared.")
        return self.functions[func_name]

    def get_function_param_count(self, func_name):
        """
        Retrieves the number of parameters for a specified function.

        Args:
            func_id (str): The identifier (name) of the function.

        Returns:
            int: The number of parameters the function has.

        Raises:
            Exception: If the function is not found.
        """
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
