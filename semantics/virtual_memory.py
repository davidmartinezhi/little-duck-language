class VirtualMemory:
    """
    Class representing the virtual memory of the compiler.
    Manages different memory segments and their allocations.
    """

    def __init__(self):
        """
        Initializes memory segments with their starting addresses and storage dictionaries.
        """
        # Starting addresses for each memory segment
        self.global_int = 1000
        self.global_float = 2000
        self.global_bool = 3000

        self.local_int = 4000
        self.local_float = 5000
        self.local_bool = 6000

        self.temp_int = 7000
        self.temp_float = 8000
        self.temp_bool = 9000

        self.constant_int = 10000
        self.constant_float = 11000
        self.constant_string = 12000
        self.constant_bool = 13000

        # Memory segments as dictionaries
        self.global_memory = {}
        self.local_memory = {}
        self.temp_memory = {}
        self.constants_memory = {}

        # Constants table to avoid duplicates
        self.constants_table = {}

    def get_address(self, var_type, scope):
        """
        Allocates a virtual address for a variable based on its type and scope.

        Args:
            var_type (str): The type of the variable ('entero', 'flotante').
            scope (str): The scope of the variable ('global', 'local').

        Returns:
            int: The allocated virtual address.
        """
        if scope == "global":  # Global scope
            if var_type == "entero":  # Integer
                address = self.global_int  # Get the next available address
                self.global_int += 1  # Increment the address counter

            elif var_type == "flotante":  # Float
                address = self.global_float  # Get the next available address
                self.global_float += 1  # Increment the address counter

            self.global_memory[address] = None  # Initialize the memory with None

        elif scope == "local":  # Local scope
            if var_type == "entero":  # Integer
                address = self.local_int  # Get the next available address
                self.local_int += 1  # Increment the address counter

            elif var_type == "flotante":  # Float
                address = self.local_float  # Get the next available address
                self.local_float += 1  # Increment the address counter

            self.local_memory[address] = None  # Initialize the memory with None

        return address  # Return the allocated address

    def get_temp_address(self, var_type):
        """
        Allocates a virtual address for a temporary variable based on its type.
        """
        if var_type == "entero":
            address = self.temp_int  # Get the next available address
            self.temp_int += 1  # Increment the address counter
            self.temp_memory[address] = 0  # Initialize with default integer value

        elif var_type == "flotante":
            address = self.temp_float  # Get the next available address
            self.temp_float += 1  # Increment the address counter
            self.temp_memory[address] = 0.0  # Initialize with default float value

        elif var_type == "bool":
            address = self.temp_bool  # Get the next available address
            self.temp_bool += 1  # Increment the address counter
            self.temp_memory[address] = False  # Initialize with default boolean value

        else:
            raise Exception(f"Unknown type '{var_type}' in get_temp_address")

        return address

    def get_constant_address(self, value, var_type):
        """
        Allocates a virtual address for a constant value. If the constant already exists, returns its address.
        """
        if value in self.constants_table:  # Check if the constant already exists
            return self.constants_table[
                value
            ]  # Return the address of the existing constant

        else:
            if var_type == "entero":
                address = self.constant_int  # Get the next available address
                self.constant_int += 1  # Increment the address counter

            elif var_type == "flotante":
                address = self.constant_float  # Get the next available address
                self.constant_float += 1  # Increment the address counter

            elif var_type == "string":
                address = self.constant_string  # Get the next available address
                self.constant_string += 1  # Increment the address counter

            else:
                raise Exception(f"Unknown constant type '{var_type}'")

            # Store the value with the correct data type
            self.constants_memory[address] = (
                value  # Store the value in the constants memory
            )
            self.constants_table[value] = (
                address  # Store the address in the constants table
            )

            return address

    def set_value(self, address, value):
        """
        Sets the value at a given virtual address in the appropriate memory segment.

        Args:
            address (int): The virtual address.
            value: The value to set.
        """
        if address in self.global_memory:  # Global memory
            self.global_memory[address] = value  # Set the value

        elif address in self.local_memory:  # Local memory
            self.local_memory[address] = value

        elif address in self.temp_memory:  # Temporary memory
            self.temp_memory[address] = value  # Set the value

        else:
            raise Exception(f"Address {address} not found in any memory segment.")

    def get_value(self, address):
        """
        Retrieves the value stored at a given virtual address.
        """
        if address in self.global_memory:  # Global memory
            return self.global_memory[address]  # Return the value

        elif address in self.local_memory:  # Local memory
            return self.local_memory[address]  # Return the value

        elif address in self.temp_memory:  # Temporary memory
            return self.temp_memory[address]  # Return the value

        elif address in self.constants_memory:  # Constants memory
            value = self.constants_memory[address]  # Get the value

            # Convert constants to appropriate types
            if isinstance(value, str):
                if value.isdigit():
                    return int(value)
                try:
                    return float(value)
                except ValueError:
                    return value  # It's a string literal
            else:
                return value
        else:
            raise Exception(f"Address {address} not found in any memory segment.")

    def print_memory(self):
        """
        Prints the memory addresses and their values for all memory segments.
        """
        print("\n===== Global Memory =====")
        for (
            address,
            value,
        ) in self.global_memory.items():  # Iterate over the global memory
            print(f"Address {address}: {value}")

        print("\n===== Local Memory =====")
        for (
            address,
            value,
        ) in self.local_memory.items():  # Iterate over the local memory
            print(f"Address {address}: {value}")

        print("\n===== Temporary Memory =====")
        for (
            address,
            value,
        ) in self.temp_memory.items():  # Iterate over the temporary memory
            print(f"Address {address}: {value}")

        print("\n===== Constants Memory =====")
        for (
            address,
            value,
        ) in self.constants_memory.items():  # Iterate over the constants memory
            print(f"Address {address}: {value}")
