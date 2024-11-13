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
        if scope == "global":
            if var_type == "entero":
                address = self.global_int
                self.global_int += 1
            elif var_type == "flotante":
                address = self.global_float
                self.global_float += 1
            self.global_memory[address] = None
        elif scope == "local":
            if var_type == "entero":
                address = self.local_int
                self.local_int += 1
            elif var_type == "flotante":
                address = self.local_float
                self.local_float += 1
            self.local_memory[address] = None
        return address
    
    def get_temp_address(self, var_type):
        """
        Allocates a virtual address for a temporary variable based on its type.

        Args:
            var_type (str): The type of the temporary variable ('entero', 'flotante', 'bool').

        Returns:
            int: The allocated virtual address.

        Raises:
            Exception: If an unknown type is provided.
        """
        if var_type == "entero":
            address = self.temp_int
            self.temp_int += 1
        elif var_type == "flotante":
            address = self.temp_float
            self.temp_float += 1
        elif var_type == "bool":
            address = self.temp_bool
            self.temp_bool += 1
        else:
            raise Exception(f"Unknown type '{var_type}' in get_temp_address")
        self.temp_memory[address] = None
        return address
    
    def get_constant_address(self, value, var_type):
        """
        Allocates a virtual address for a constant value. If the constant already exists, returns its address.
        
        Args:
            value (str): The constant value.
            var_type (str): The type of the constant ('entero', 'flotante', 'string').
        
        Returns:
            int: The allocated virtual address.
        """
        if value in self.constants_table:
            return self.constants_table[value]
        else:
            if var_type == "entero":
                address = self.constant_int
                self.constant_int += 1
            elif var_type == "flotante":
                address = self.constant_float
                self.constant_float += 1
            elif var_type == "string":
                address = self.constant_string
                self.constant_string += 1
            self.constants_memory[address] = value
            self.constants_table[value] = address
            return address
    
    def set_value(self, address, value):
        """
        Sets the value at a given virtual address in the appropriate memory segment.
        
        Args:
            address (int): The virtual address.
            value: The value to set.
        """
        if address in self.global_memory:
            self.global_memory[address] = value
        elif address in self.local_memory:
            self.local_memory[address] = value
        elif address in self.temp_memory:
            self.temp_memory[address] = value
        elif address in self.constants_memory:
            self.constants_memory[address] = value
        else:
            print(f"Address {address} not found in any memory segment.")
    
    def get_value(self, address):
        """
        Retrieves the value stored at a given virtual address.
        
        Args:
            address (int): The virtual address.
        
        Returns:
            The value stored at the address.
        """
        if address in self.global_memory:
            return self.global_memory[address]
        elif address in self.local_memory:
            return self.local_memory[address]
        elif address in self.temp_memory:
            return self.temp_memory[address]
        elif address in self.constants_memory:
            return self.constants_memory[address]
        else:
            print(f"Address {address} not found in any memory segment.")
            return None
    
    def print_memory(self):
        """
        Prints the memory addresses and their values for all memory segments.
        """
        print("\n===== Global Memory =====")
        for address, value in self.global_memory.items():
            print(f"Address {address}: {value}")
        
        print("\n===== Local Memory =====")
        for address, value in self.local_memory.items():
            print(f"Address {address}: {value}")
        
        print("\n===== Temporary Memory =====")
        for address, value in self.temp_memory.items():
            print(f"Address {address}: {value}")
        
        print("\n===== Constants Memory =====")
        for address, value in self.constants_memory.items():
            print(f"Address {address}: {value}")
