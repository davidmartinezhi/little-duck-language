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

        self.local_int_start = 4000
        self.local_float_start = 5000
        self.local_bool_start = 6000

        self.temp_int = 7000
        self.temp_float = 8000
        self.temp_bool = 9000

        self.constant_int = 10000
        self.constant_float = 11000
        self.constant_string = 12000
        self.constant_bool = 13000

        # Memory segments as dictionaries
        self.global_memory = {}
        self.local_memory_stack = []  # Stack for local memory dictionaries
        self.temp_memory = {}
        self.constants_memory = {}

        # Constants table to avoid duplicates
        self.constants_table = {}
        
        # Address counters for local memory
        self.local_int = self.local_int_start
        self.local_float = self.local_float_start
        self.local_bool = self.local_bool_start

    def get_address(self, var_type, scope):
        """
        Allocates a virtual address for a variable based on its type and scope.

        Args:
            var_type (str): The type of the variable ('entero', 'flotante', 'bool').
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

            elif var_type == "bool":  # Bool
                address = self.global_bool
                self.global_bool +=1

            else:
                raise Exception(f"Unknown variable type '{var_type}' in global memory allocation.")

            self.global_memory[address] = None  # Initialize the memory with None

        elif scope == "local":
            if not self.local_memory_stack:
                self.push_local_memory()
            current_local_memory = self.local_memory_stack[-1]
            if var_type == "entero":
                address = self.local_int
                self.local_int += 1
            elif var_type == "flotante":
                address = self.local_float
                self.local_float += 1
            elif var_type == "bool":
                address = self.local_bool
                self.local_bool += 1
            else:
                raise Exception(f"Unknown variable type '{var_type}' in local memory allocation.")
            current_local_memory[address] = None
            return address  # Return the allocated address

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
            existing_address = self.constants_table[value]
            # Verify type consistency
            expected_type = self.get_type_by_address(existing_address)
            if expected_type == var_type:
                return existing_address
            else:
                raise Exception(f"Type mismatch for constant '{value}'. Expected '{expected_type}', got '{var_type}'.")
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

            elif var_type == "bool":
                address = self.constant_bool  # Get the next available address
                self.constant_bool += 1  # Increment the address counter

            else:
                raise Exception(f"Unknown constant type '{var_type}'")

            # Store the value with the correct data type
            self.constants_memory[address] = value  # Store the value in the constants memory
            self.constants_table[value] = address  # Store the address in the constants table

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

        elif self.is_in_local_memory(address):  # Local memory
            self.local_memory_stack[-1][address] = value  # Set the value in the current local frame

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

        elif self.is_in_local_memory(address):
            return self.local_memory_stack[-1][address]

        elif address in self.temp_memory:  # Temporary memory
            return self.temp_memory[address]  # Return the value

        elif address in self.constants_memory:  # Constants memory
            value = self.constants_memory[address]  # Get the value
            return value  # Assuming values are already correctly typed

        else:
            raise Exception(f"Address {address} not found in any memory segment.")

    def print_memory(self):
        """
        Prints the memory addresses and their values for all memory segments.
        """
        print("\n===== Global Memory =====")
        for address, value in sorted(self.global_memory.items()):
            print(f"Address {address}: {value}")

        print("\n===== Local Memory =====")
        for frame_idx, local_mem in enumerate(self.local_memory_stack):
            print(f"Frame {frame_idx}:")
            for address, value in sorted(local_mem.items()):
                print(f"  Address {address}: {value}")

        print("\n===== Temporary Memory =====")
        for address, value in sorted(self.temp_memory.items()):
            print(f"Address {address}: {value}")

        print("\n===== Constants Memory =====")
        for address, value in sorted(self.constants_memory.items()):
            print(f"Address {address}: {value}")

    def push_local_memory(self):
        """
        Pushes a new local memory dictionary onto the stack and resets local address counters.
        """
        self.local_memory_stack.append({})
        # Reset local address counters for the new function
        self.local_int = self.local_int_start
        self.local_float = self.local_float_start
        self.local_bool = self.local_bool_start

    def pop_local_memory(self):
        """
        Pops the local memory dictionary from the stack.
        """
        if self.local_memory_stack:
            self.local_memory_stack.pop()
        else:
            raise Exception("Local memory stack underflow.")

    def is_in_local_memory(self, address):
        """
        Checks if an address exists in the current local memory frame.

        Args:
            address (int): The virtual address.

        Returns:
            bool: True if address is in local memory, False otherwise.
        """
        if self.local_memory_stack:
            return address in self.local_memory_stack[-1]
        return False

    def get_type_by_address(self, address):
        """
        Determines the type of a variable based on its address.

        Args:
            address (int): The memory address.

        Returns:
            str: The type of the variable ('entero', 'flotante', 'bool', 'string').
        """
        if 1000 <= address < 4000:
            if 1000 <= address < 2000:
                return 'entero'
            elif 2000 <= address < 3000:
                return 'flotante'
            elif 3000 <= address < 4000:
                return 'bool'
        elif 4000 <= address < 7000:
            if 4000 <= address < 5000:
                return 'entero'
            elif 5000 <= address < 6000:
                return 'flotante'
            elif 6000 <= address < 7000:
                return 'bool'
        elif 7000 <= address < 10000:
            if 7000 <= address < 8000:
                return 'entero'
            elif 8000 <= address < 9000:
                return 'flotante'
            elif 9000 <= address < 10000:
                return 'bool'
        elif 10000 <= address < 14000:
            if 10000 <= address < 11000:
                return 'entero'
            elif 11000 <= address < 12000:
                return 'flotante'
            elif 12000 <= address < 13000:
                return 'string'
            elif 13000 <= address < 14000:
                return 'bool'
        return 'unknown'
