class VirtualMachine:
    """
    A class representing the virtual machine that executes the quadruples.

    Attributes:
        print_traversal (bool): Whether to print the traversal of the virtual machine.
        quadruples (list): The list of quadruples to execute.
        virtual_memory (VirtualMemory): An instance of VirtualMemory to manage memory.
        IP (int): Instruction Pointer, the index of the current quadruple.
    """

    def __init__(self, quadruples, virtual_memory, print_traversal=False):
        """
        Initializes the virtual machine with quadruples and virtual memory.

        Args:
            quadruples (list): The list of quadruples to execute.
            virtual_memory (VirtualMemory): The virtual memory manager instance.
            print_traversal (bool): Whether to print the traversal of the virtual machine.
        """
        self.print_traversal = print_traversal

        self.quadruples = quadruples
        self.virtual_memory = virtual_memory
        self.IP = 0  # Instruction Pointer

    def run(self):
        """
        Executes the quadruples using the virtual machine.

        Processes each quadruple based on its operation code and manipulates memory accordingly.
        """
        while self.IP < len(self.quadruples):  # Iterate over the quadruples
            quad = self.quadruples[self.IP]  # Get the current quadruple
            op = quad[0]  # Get current operation code

            if op == "=":
                self.handle_assignment(quad)
            elif op in ["+", "-", "*", "/"]:
                self.handle_arithmetic(quad)
            elif op in ["<", ">", "==", "!="]:
                self.handle_relational(quad)
            elif op == "GOTOF":
                self.handle_gotof(quad)
            elif op == "GOTO":
                self.handle_goto(quad)
            elif op == "print":
                self.handle_print(quad)
            elif op == "print_str":
                self.handle_print_str(quad)
            elif op == 'print_newline':
                self.handle_print_newline(quad)
            elif op == "END":
                break
            else:
                raise Exception(f"Unknown operation: {op}")

    def handle_assignment(self, quad):
        """
        Handles the assignment operation '='.

        Args:
            quad (tuple): The quadruple representing the assignment operation.
        """
        source = quad[1]  # Address of the value to assign
        target = quad[3]  # Address of the variable to assign the value to
        value = self.virtual_memory.get_value(
            source
        )  # Get the value from the source address
        self.virtual_memory.set_value(
            target, value
        )  # Assign the value to the target address
        self.IP += 1  # Move to the next quadruple

        if self.print_traversal:
            print(f"Assigned value {value} to address {target}")

    def handle_arithmetic(self, quad):
        """
        Handles arithmetic operations '+', '-', '*', '/'.
        """
        op = quad[0]  # Get the operation code
        left_operand = quad[1]  # Address of the left operand
        right_operand = quad[2]  # Address of the right operand
        result_address = quad[3]  # Address to store the result

        left_value = self.virtual_memory.get_value(
            left_operand
        )  # Get the value of the left operand
        right_value = self.virtual_memory.get_value(
            right_operand
        )  # Get the value of the right operand

        # Ensure operands are numbers
        if isinstance(
            left_value, str
        ):  # Convert to int or float if the value is a string
            left_value = int(left_value) if left_value.isdigit() else float(left_value)
        if isinstance(
            right_value, str
        ):  # Convert to int or float if the value is a string
            right_value = (
                int(right_value) if right_value.isdigit() else float(right_value)
            )

        # Print operation being performed
        if self.print_traversal:
            print(f"Performing {left_value} {op} {right_value}")

        # Perform the arithmetic operation
        if op == "+":
            result = left_value + right_value
        elif op == "-":
            result = left_value - right_value
        elif op == "*":
            result = left_value * right_value
        elif op == "/":
            if right_value == 0:  # Check for division by zero
                raise Exception("Division by zero")
            result = left_value / right_value

        # Store the result in the virtual memory
        self.virtual_memory.set_value(result_address, result)
        self.IP += 1  # Move to the next quadruple

        if self.print_traversal:
            print(f"Assigned value {result} to address {result_address}")

    def handle_relational(self, quad):
        """
        Handles relational operations '<', '>', '==', '!='.
        """
        op = quad[0]  # Get the operation code
        left_operand = quad[1]  # Address of the left operand
        right_operand = quad[2]  # Address of the right operand
        result_address = quad[3]  # Address to store the result

        # Retrieve operand values from memory
        left_value = self.virtual_memory.get_value(left_operand)
        right_value = self.virtual_memory.get_value(right_operand)

        # Ensure operands are numbers
        if isinstance(left_value, str):
            left_value = int(left_value) if left_value.isdigit() else float(left_value)
        if isinstance(right_value, str):
            right_value = (
                int(right_value) if right_value.isdigit() else float(right_value)
            )

        # Print evaluation being performed
        if self.print_traversal:
            print(f"Evaluating {left_value} {op} {right_value}")

        # Perform the relational operation
        if op == "<":
            result = left_value < right_value
        elif op == ">":
            result = left_value > right_value
        elif op == "==":
            result = left_value == right_value
        elif op == "!=":
            result = left_value != right_value

        # Store the boolean result in the virtual memory
        self.virtual_memory.set_value(result_address, result)
        self.IP += 1

        if self.print_traversal:
            print(f"Storing boolean result {result} at address {result_address}")

    def handle_gotof(self, quad):
        """
        Handles the 'GOTOF' (Go To False) operation.

        Args:
            quad (tuple): The quadruple representing the 'GOTOF' operation.
        """
        condition_address = quad[1]  # Address of the condition to evaluate
        jump_to = quad[3]  # Quadruple index to jump to if the condition is False
        condition_value = self.virtual_memory.get_value(
            condition_address
        )  # Get the value of the condition

        # If the condition is False, jump to the specified quadruple index
        if not condition_value:
            self.IP = jump_to  # Jump to the specified quadruple index
        else:
            self.IP += 1  # Move to the next quadruple

    def handle_goto(self, quad):
        """
        Handles the unconditional 'GOTO' operation.

        Args:
            quad (tuple): The quadruple representing the 'GOTO' operation.
        """
        self.IP = quad[3]  # Jump to the specified quadruple index

    def handle_print(self, quad):
        """
        Handles the 'print' operation to output variable values.

        Args:
            quad (tuple): The quadruple representing the 'print' operation.
        """
        value_address = quad[1]  # Address of the value to print
        value = self.virtual_memory.get_value(
            value_address
        )  # Get the value from the address
        print(value, end='')  # Print the value
        self.IP += 1  # Move to the next quadruple

    def handle_print_str(self, quad):
        """
        Handles the 'print_str' operation to output string constants.

        Args:
            quad (tuple): The quadruple representing the 'print_str' operation.
        """
        string_address = quad[1]  # Address of the string to print
        string_value = self.virtual_memory.get_value(
            string_address
        )  # Get the string from the address
        print(string_value, end='')  # Print the string
        self.IP += 1  # Move to the next quadruple
        
    def handle_print_newline(self, quad):
        """
        Handles the 'print_newline' operation to output a newline character.
        """
        print()  # Print newline
        self.IP += 1
