class MemorySegment:
    GLOBAL_START = 1000
    LOCAL_START = 5000
    TEMP_START = 9000
    CONSTANT_START = 13000

    INT_OFFSET = 0
    FLOAT_OFFSET = 1000
    BOOL_OFFSET = 2000
    STRING_OFFSET = 3000

    SEGMENT_SIZE = 1000

class VirtualMemory:
    def __init__(self):
        self.next_global_int = MemorySegment.GLOBAL_START + MemorySegment.INT_OFFSET
        self.next_global_float = MemorySegment.GLOBAL_START + MemorySegment.FLOAT_OFFSET
        self.next_local_int = MemorySegment.LOCAL_START + MemorySegment.INT_OFFSET
        self.next_local_float = MemorySegment.LOCAL_START + MemorySegment.FLOAT_OFFSET
        self.next_temp_int = MemorySegment.TEMP_START + MemorySegment.INT_OFFSET
        self.next_temp_float = MemorySegment.TEMP_START + MemorySegment.FLOAT_OFFSET
        self.next_constant_int = MemorySegment.CONSTANT_START + MemorySegment.INT_OFFSET
        self.next_constant_float = MemorySegment.CONSTANT_START + MemorySegment.FLOAT_OFFSET
        self.constants_table = {}

    def get_address(self, var_type, scope):
        if scope == "global":
            if var_type == "entero":
                addr = self.next_global_int
                self.next_global_int += 1
            elif var_type == "flotante":
                addr = self.next_global_float
                self.next_global_float += 1
        else:
            if var_type == "entero":
                addr = self.next_local_int
                self.next_local_int += 1
            elif var_type == "flotante":
                addr = self.next_local_float
                self.next_local_float += 1
        return addr

    def get_temp_address(self, var_type):
        if var_type == "entero":
            addr = self.next_temp_int
            self.next_temp_int += 1
        elif var_type == "flotante":
            addr = self.next_temp_float
            self.next_temp_float += 1
        return addr

    def get_constant_address(self, value, var_type):
        if value in self.constants_table:
            return self.constants_table[value]
        else:
            if var_type == "entero":
                addr = self.next_constant_int
                self.next_constant_int += 1
            elif var_type == "flotante":
                addr = self.next_constant_float
                self.next_constant_float += 1
            elif var_type == "string":
                addr = MemorySegment.CONSTANT_START + MemorySegment.STRING_OFFSET + len(self.constants_table)
            self.constants_table[value] = addr
            return addr

