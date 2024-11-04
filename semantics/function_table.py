class FunctionTable:
    """
    Class representing the function directory used by the compiler to manage functions.
    It stores information about functions such as their parameters,
    and quadruple counts for code generation.

    Attributes:
        functions (dict): A dictionary where each key is a function identifier (name),
                          and each value is a dictionary containing details about the function.
    """

    def __init__(self):
        """
        Initializes the FunctionTable with an empty functions dictionary.
        """
        self.functions = {}

    def add_function(self, func_id):
        """
        Adds a new function to the function table.

        Args:
            func_id (str): The identifier (name) of the function.

        Raises:
            Exception: If a function with the same identifier already exists.

        Returns:
            bool: True if the function was added successfully.

        Complexity:
            Runtime: O(1), we store a key, value pair in a dictionary
        """
        if func_id in self.functions:
            raise Exception(f"Function {func_id} already declared.")
        # Add the function to the function table with its attributes
        self.functions[func_id] = {
            "params": {},          # Dictionary of parameters (param_name: param_type)
            "quad_count": 0,       # Quadruple count for code generation
        }
        return True

    def get_function(self, func_id):
        """
        Retrieves the function information from the function table.

        Args:
            func_id (str): The identifier (name) of the function.

        Returns:
            dict or None: The function's information dictionary if found, else None.

        Complexity:
            Runtime: O(1), we get the id of a function stored in a dictionary
        """
        return self.functions.get(func_id, None)

    def add_function_param(self, func_id: str | None, param):
        """
        Adds a new parameter to a function in the functions dictionary.

        Args:
            func_id (str): The identifier (name) of the function.
            param (dict): A dictionary containing the name of the parameter and its data type.

        Returns:
            bool: True if the function was added successfully.

        Complexity:
            Runtime: O(1)
        """

        # Check the function is declared
        if func_id not in self.functions:
            raise Exception(f"Function {func_id} not declared.")

        # Check that parameter name has not been declared before
        if param["name"] in self.functions[func_id]["params"]:
            raise Exception(f"Parameter {func_id} previously declared in the function.")

        # Add parameter
        self.functions[func_id]["params"][param["name"]] = param["type"]
        return True


    def get_function_params(self, func_id):
        """
        Retrieves the parameters of the specified function.

        Args:
            func_id (str): The identifier (name) of the function.

        Returns:
            dict: A dictionary of parameters (param_name: param_type) for the function.

        Raises:
            KeyError: If the function is not found in the function table.

        Complexity:
            Runtime: O(1), we get the parameters of a function stored in a dictionary
        """
        return self.functions[func_id]["params"]

    def get_function_param(self, func_id, param_id):
        """
        Retrieves the type of a specific parameter of a function.

        Args:
            func_id (str): The identifier (name) of the function.
            param_id (str): The identifier (name) of the parameter.

        Returns:
            str or None: The type of the parameter if found, else None.

        Raises:
            KeyError: If the function is not found in the function table.

        Complexity:
            Runtime: O(1), we get the type of a parameter of a function stored in a dictionary
        """
        return self.functions[func_id]["params"].get(param_id, None)

    def get_function_param_id(self, func_id, index):
        """
        Retrieves the parameter name at the specified index for a function.

        Args:
            func_id (str): The identifier (name) of the function.
            index (int): The index of the parameter in the function's parameter list.

        Returns:
            str: The parameter name at the specified index.

        Raises:
            KeyError: If the function is not found in the function table.
            IndexError: If the index is out of range.

        Complexity:
            Runtime: O(n), all keys are traversed to get a list
        """
        # Get the list of parameter names and return the one at the specified index
        return list(self.functions[func_id]["params"].keys())[index]

    def get_function_param_type(self, func_id, param_id):
        """
        Retrieves the type of a specific parameter of a function.

        Args:
            func_id (str): The identifier (name) of the function.
            param_id (str): The identifier (name) of the parameter.

        Returns:
            str: The type of the parameter.

        Raises:
            KeyError: If the function or parameter is not found in the function table.

        Complexity:
            Runtime: O(1), we get the id of a parameter of a function stored in a dictionary
        """
        return self.functions[func_id]["params"][param_id]

    def get_function_param_count(self, func_id):
        """
        Retrieves the number of parameters for a specified function.

        Args:
            func_id (str): The identifier (name) of the function.

        Returns:
            int: The number of parameters the function has.

        Raises:
            KeyError: If the function is not found in the function table.

        Complexity:
            Runtime: O(1)
        """
        return len(self.functions[func_id]["params"])

    def clean_functions(self):
        """
        Clears all functions from the function table.

        Complexity:
            Runtime: O(1)
        """
        self.functions.clear()
