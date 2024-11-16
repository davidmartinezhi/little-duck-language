class VirtualMachine:
    """
    A class representing the virtual machine that executes the quadruples.

    Attributes:
        quadruples (list): The list of quadruples to execute.
        virtual_memory (VirtualMemory): An instance of VirtualMemory to manage memory.
        IP (int): Instruction Pointer, the index of the current quadruple.
    """

    def __init__(self, quadruples, virtual_memory):
        """
        Initializes the virtual machine with quadruples and virtual memory.

        Args:
            quadruples (list): The list of quadruples to execute.
            virtual_memory (VirtualMemory): The virtual memory manager instance.
        """
        self.quadruples = quadruples
        self.virtual_memory = virtual_memory
        self.IP = 0  # Instruction Pointer

    def run(self):
        """
        Executes the quadruples using the virtual machine.

        Processes each quadruple based on its operation code and manipulates memory accordingly.
        """
        while self.IP < len(self.quadruples):
            quad = self.quadruples[self.IP]
            op = quad[0]

            if op == '=':
                self.handle_assignment(quad)
            elif op in ['+', '-', '*', '/']:
                self.handle_arithmetic(quad)
            elif op in ['<', '>', '==', '!=']:
                self.handle_relational(quad)
            elif op == 'GOTOF':
                self.handle_gotof(quad)
            elif op == 'GOTO':
                self.handle_goto(quad)
            elif op == 'print':
                self.handle_print(quad)
            elif op == 'print_str':
                self.handle_print_str(quad)
            elif op == 'END':
                break
            else:
                raise Exception(f"Unknown operation: {op}")

    def handle_assignment(self, quad):
        """
        Handles the assignment operation '='.
        
        Args:
            quad (tuple): The quadruple representing the assignment operation.
        """
        source = quad[1]
        target = quad[3]
        value = self.virtual_memory.get_value(source)
        self.virtual_memory.set_value(target, value)
        print(f"Assigned value {value} to address {target}")
        self.IP += 1

    def handle_arithmetic(self, quad):
        """
        Handles arithmetic operations '+', '-', '*', '/'.
        """
        op = quad[0]
        left_operand = quad[1]
        right_operand = quad[2]
        result_address = quad[3]

        left_value = self.virtual_memory.get_value(left_operand)
        right_value = self.virtual_memory.get_value(right_operand)

        # Ensure operands are numbers
        if isinstance(left_value, str):
            left_value = int(left_value) if left_value.isdigit() else float(left_value)
        if isinstance(right_value, str):
            right_value = int(right_value) if right_value.isdigit() else float(right_value)

        print(f"Performing {left_value} {op} {right_value}")
        # Perform the arithmetic operation
        if op == '+':
            result = left_value + right_value
        elif op == '-':
            result = left_value - right_value
        elif op == '*':
            result = left_value * right_value
        elif op == '/':
            if right_value == 0:
                raise Exception("Division by zero")
            result = left_value / right_value

        # Store the result in the virtual memory
        self.virtual_memory.set_value(result_address, result)
        print(f"Assigned value {result} to address {result_address}")
        self.IP += 1


    def handle_relational(self, quad):
        """
        Handles relational operations '<', '>', '==', '!='.
        """
        op = quad[0]
        left_operand = quad[1]
        right_operand = quad[2]
        result_address = quad[3]

        # Retrieve operand values from memory
        left_value = self.virtual_memory.get_value(left_operand)
        right_value = self.virtual_memory.get_value(right_operand)

        # Ensure operands are numbers
        if isinstance(left_value, str):
            left_value = int(left_value) if left_value.isdigit() else float(left_value)
        if isinstance(right_value, str):
            right_value = int(right_value) if right_value.isdigit() else float(right_value)

        print(f"Evaluating {left_value} {op} {right_value}")
        # Perform the relational operation
        if op == '<':
            result = left_value < right_value
        elif op == '>':
            result = left_value > right_value
        elif op == '==':
            result = left_value == right_value
        elif op == '!=':
            result = left_value != right_value

        # Store the boolean result in the virtual memory
        self.virtual_memory.set_value(result_address, result)
        print(f"Storing boolean result {result} at address {result_address}")
        self.IP += 1


    def handle_gotof(self, quad):
        """
        Handles the 'GOTOF' (Go To False) operation.

        Args:
            quad (tuple): The quadruple representing the 'GOTOF' operation.
        """
        condition_address = quad[1]
        jump_to = quad[3]
        condition_value = self.virtual_memory.get_value(condition_address)

        # If the condition is False, jump to the specified quadruple index
        if not condition_value:
            self.IP = jump_to
        else:
            self.IP += 1

    def handle_goto(self, quad):
        """
        Handles the unconditional 'GOTO' operation.

        Args:
            quad (tuple): The quadruple representing the 'GOTO' operation.
        """
        self.IP = quad[3]

    def handle_print(self, quad):
        """
        Handles the 'print' operation to output variable values.

        Args:
            quad (tuple): The quadruple representing the 'print' operation.
        """
        value_address = quad[1]
        value = self.virtual_memory.get_value(value_address)
        print(value)
        self.IP += 1

    def handle_print_str(self, quad):
        """
        Handles the 'print_str' operation to output string constants.

        Args:
            quad (tuple): The quadruple representing the 'print_str' operation.
        """
        string_address = quad[1]
        string_value = self.virtual_memory.get_value(string_address)
        print(string_value)
        self.IP += 1