from antlr4 import *
from generated.little_duckParser import little_duckParser
from generated.little_duckListener import little_duckListener

# Import semantic modules
from semantics.semantic_cube import SemanticCube
from semantics.variable_table import VariableTable
from semantics.function_table import FunctionTable
from semantics.stack import Stack
from semantics.quadruple import Quadruple
from semantics.virtual_memory import VirtualMemory


class LittleDuckCustomListener(little_duckListener):
    """
    Custom listener for the Little Duck language parser to perform semantic analysis.
    This listener overrides methods to handle variable declarations, assignments, expressions,
    conditional statements, while loops, and function declarations/calls,
    integrating semantic checks and quadruple generation.
    """

    def __init__(self, print_traversal: bool = False):
        """
        Initialize semantic structures and variables needed for semantic analysis.
        """
        self.print_traversal = print_traversal

        # Initialize semantic structures
        self.variable_table = VariableTable()  # Symbol table to store variables and their attributes
        self.semantic_cube = SemanticCube()    # Semantic cube for type checking and operation validation
        self.function_table = FunctionTable()  # Function table to store function attributes
        self.quadruple_manager = Quadruple()   # Manages quadruples (intermediate code representation)
        self.virtual_memory = VirtualMemory()   # Manages virtual memory

        self.current_scope = "global"  # Tracks the current scope (e.g., global)

        self.var_stack = []            # Stack to temporarily store variable identifiers during parsing
        self.operand_stack = Stack()   # Stack to manage operands in expression evaluation
        self.type_stack = Stack()      # Stack to manage operand types in expression evaluation

        self.temp_var_counter = 0      # Counter for generating unique temporary variable names
        self.label_counter = 0         # Counter for generating unique labels

        # Separate stacks for different control flows
        self.initial_goto_stack = Stack()     # Stack for initial GOTO in the program
        self.condition_goto_stack = Stack()   # Stack for GOTOF in conditionals
        self.loop_start_stack = Stack()       # Stack for loop starts

        self.current_function = None   # Tracks the current function being parsed

    # ************************************** PROGRAM **************************************#
    # Program entry and exit - scope management
    def enterPrograma(self, ctx: little_duckParser.ProgramaContext):
        """
        Enter the root of the parse tree (program).
        Initialize the program and set the global scope.
        """

        self.variable_table.set_scope(
            self.current_scope
        )  # Set current scope to global scope
        program_name = ctx.ID().getText()  # Get program name from the text of the ID

        # Generate initial GOTO quadruple to jump to 'inicio' block
        quadruple = ('GOTO', None, None, None)
        self.quadruple_manager.push(quadruple)

        # Push the index of this GOTO onto the initial_goto_stack to patch later
        self.initial_goto_stack.push(len(self.quadruple_manager.quadruples) - 1)

        if self.print_traversal:
            print("\n=============")
            print(f"Entering program: {program_name}")  # Print program name
            print("=============\n")
            print(f"Generated initial GOTO quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {quadruple}")

    def exitPrograma(self, ctx: little_duckParser.ProgramaContext):
        """
        Exit the root of the parse tree (program).
        Perform cleanup, output the generated quadruples, and print memory contents.
        """
        if self.print_traversal:
            print("\n=============")
            print("Exiting program")
            print("=============\n")

        self.variable_table.clean_variables(self.current_scope)  # Clean up variables

        # Add END quadruple to signify the end of the program
        end_quadruple = ("END", None, None, None)  # Quadruple for program end
        self.quadruple_manager.push(end_quadruple)    # Push the END quadruple to the quadruple manager

        # Print the generated quadruples and memory contents
        if self.print_traversal:
            print(f"Generated END quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {end_quadruple}")

            # Print the generated quadruples
            print("\nGenerated Quadruples:")
            for idx, quad in enumerate(self.quadruple_manager.quadruples):
                print(f"{idx}: {quad}")

            # Print the memory addresses with their values
            self.virtual_memory.print_memory()

            print(f"Operand stack: {self.operand_stack.stack}")
            print(f"Type stack: {self.type_stack.stack}")

    # ************************************** VARIABLES **************************************#
    # Variable declaration - add variables to scope
    def enterVars(self, ctx: little_duckParser.VarsContext):
        """
        Enter a variable declaration block.
        """
        if self.print_traversal:
            print("\n=====Entering variable declaration=====")

    def exitVars(self, ctx: little_duckParser.VarsContext):
        """
        Exit a variable declaration block.
        """
        if self.print_traversal:
            print("=====Exit variable declaration=====\n")

    def exitVar_decl(self, ctx: little_duckParser.Var_declContext):
        """
        Exit a variable declaration.
        Assign types to variables, allocate memory addresses, and add them to the variable table.
        Also, initialize the variable in virtual memory with default values.
        """
        var_type = ctx.tipo().getText()  # Get the type of the variable
        ids = ctx.id_list().ID()  # Get the list of variable identifiers

        for id_token in ids:  # Iterate over each variable identifier
            var_name = id_token.getText()  # Get the text of the ID token

            # Check if the variable is already declared in the current scope
            if var_name in self.variable_table.variables[self.current_scope]:
                raise Exception(
                    f"Error: Variable '{var_name}' is already declared in scope '{self.current_scope}'."
                )

            # If the variable is not declared in the current scope
            else:
                # Allocate memory address for the variable
                address = self.virtual_memory.get_address(var_type, 'global' if self.current_scope == 'global' else 'local')
                # Add the variable to the variable table with its address
                self.variable_table.add_variable(
                    self.current_scope, var_name, var_type, address
                )

                # Initialize the variable in virtual memory with default value
                if var_type == "entero":
                    self.virtual_memory.set_value(address, 0)
                elif var_type == "flotante":
                    self.virtual_memory.set_value(address, 0.0)
                else:
                    self.virtual_memory.set_value(address, None)

                # Print the variable declaration information
                if self.print_traversal:
                    print(
                        f"Variable declaration: {var_name} : {var_type}, Address: {address}"
                    )

    # ************************************** ASSIGNMENT **************************************#
    # Assignment statement
    def exitAsigna(self, ctx: little_duckParser.AsignaContext):
        """
        Exit an assignment statement.
        Perform type checking, generate assignment quadruples, and update memory.
        """
        var_name = ctx.ID().getText()  # Get the variable name from the ID token
        scope = self.variable_table.find_scope(
            var_name, self.current_scope
        )  # Find the scope of the variable

        # Check if the variable is declared
        if not scope:
            raise Exception(f"Error: Variable '{var_name}' is not declared.")

        # If the variable is declared
        else:
            # Get the type of the expression on the right-hand side and the variable's type
            expr_type = self.get_expression_type(
                ctx.expresion()
            )  # Get the type of the expression
            var_type = self.variable_table.get_variable_type(
                scope, var_name
            )  # Get the type of the variable

            try:
                result_type = self.semantic_cube.get_type(
                    var_type, expr_type, "="
                )  # Get the result type of the assignment
                operand_address = (
                    self.operand_stack.pop()
                )  # Retrieve the operand's address from the operand stack
                self.type_stack.pop()  # Pop the operand's type from the type stack
                var_address = self.variable_table.get_variable_address(
                    scope, var_name
                )  # Get the variable's address

                # Generate the assignment quadruple using addresses
                quadruple = ("=", operand_address, None, var_address)
                self.quadruple_manager.push(quadruple)

                # Update memory with the new value
                value = self.virtual_memory.get_value(operand_address)
                self.virtual_memory.set_value(var_address, value)

                # Print the generated quadruple
                if self.print_traversal:
                    print(f"Generated quadruple: {quadruple}")

            except TypeError as e:
                raise Exception(f"Type mismatch in assignment to variable '{var_name}'. {str(e)}")

    # ************************************** CONDITIONAL STATEMENTS **************************************#
    # Conditional statement - si (if)
    def enterCondicion(self, ctx: little_duckParser.CondicionContext):
        """
        Enter condition statement.
        Perform type checking, generate condicion quadruples, and update condition_goto_stack.
        """
        if self.print_traversal:
            print("\n============= Entering 'si' condition =============")

        # Get the type of the condition expression
        expr_type = self.get_expression_type(ctx.expresion())

        # Print the condition expression
        if self.print_traversal:
            print(
                f"Expresion: {ctx.expresion().getText()}, type: {expr_type}"
            )  # Print the condition expression

        # Check if the type of the expression is not boolean
        if expr_type != "bool":
            raise Exception("Error: Condition expression must be of type 'bool'.")

        # If the type of the expression is boolean
        else:
            condition_result = (  # Pop the condition result from the operand stack
                self.operand_stack.pop()
            )
            self.type_stack.pop()  # Pop the operand's type from the type stack

            # Generate the GOTOF quadruple and push it to the condition_goto_stack
            quadruple = (
                "GOTOF",
                condition_result,
                None,
                None,
            )
            self.quadruple_manager.push(quadruple)

            # Push the GOTOF quadruple's index onto the condition_goto_stack for future patching
            self.condition_goto_stack.push(
                len(self.quadruple_manager.quadruples) - 1
            )  # Push the index of the quadruple to the condition_goto_stack

            # Print the generated quadruple
            if self.print_traversal:
                print(
                    f"Generated GOTOF quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {quadruple}"
                )

    def exitCondicion(self, ctx: little_duckParser.CondicionContext):
        """
        Exit condition statement.
        Patch GOTOF quadruples if 'sino' clause is not present.
        """
        if self.print_traversal:
            print("============= Exiting 'si' condition =============\n")

        # Check if there is no 'sino' clause
        if not ctx.condicion_else().SINO():
            # No else clause; patch the GOTOF here
            false_jump_index = (  # Pop the index of the quadruple from the condition_goto_stack
                self.condition_goto_stack.pop()
            )

            # Patch the GOTOF quadruple
            self.quadruple_manager.quadruples[false_jump_index] = (
                "GOTOF",
                self.quadruple_manager.quadruples[false_jump_index][1],
                None,
                len(self.quadruple_manager.quadruples),  # Point to the next quadruple
            )

            # Print the patched quadruple
            if self.print_traversal:
                print(
                    f"Patched GOTOF at index {false_jump_index} to point to {len(self.quadruple_manager.quadruples)}"
                )

    def enterCondicion_else(self, ctx: little_duckParser.Condicion_elseContext):
        """
        Enter condition_else statement.
        Generate GOTO quadruples to skip the else block after the if block executes.
        """
        # Check if there is a 'sino' clause
        if ctx.SINO():

            # Print that we are entering the 'sino' clause
            if self.print_traversal:
                print("\n============= Entering 'sino' clause =============")

            # Pop the false jump index from the condition_goto_stack
            false_jump_index = self.condition_goto_stack.pop()

            # Generate a GOTO to skip the else block after the if block executes
            quadruple = ("GOTO", None, None, None)
            self.quadruple_manager.push(quadruple)

            # Push the GOTO's index onto the condition_goto_stack for later patching
            self.condition_goto_stack.push(len(self.quadruple_manager.quadruples) - 1)

            # Print the generated GOTO quadruple
            if self.print_traversal:
                print(
                    f"Generated GOTO quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {quadruple}"
                )

            # Now patch the GOTOF to point to the instruction after the GOTO (start of else block)
            self.quadruple_manager.quadruples[false_jump_index] = (
                "GOTOF",
                self.quadruple_manager.quadruples[false_jump_index][1],
                None,
                len(self.quadruple_manager.quadruples),
            )

            # Print the patched GOTOF quadruple
            if self.print_traversal:
                print(
                    f"Patched GOTOF at index {false_jump_index} to point to else block at {len(self.quadruple_manager.quadruples)}"
                )

    def exitCondicion_else(self, ctx: little_duckParser.Condicion_elseContext):
        """
        Exit condition_else statement.
        Patch GOTO quadruples to skip the else block after the if block executes.
        """
        # Check if there is a 'sino' clause
        if ctx.SINO():

            # Print that we are exiting the 'sino' clause
            if self.print_traversal:
                print("============= Exiting 'sino' clause =============\n")

            # Pop the GOTO index from the condition_goto_stack
            end_jump_index = self.condition_goto_stack.pop()

            # Update the GOTO to point to the instruction after the else block (or to END)
            self.quadruple_manager.quadruples[end_jump_index] = (
                "GOTO",
                None,
                None,
                len(self.quadruple_manager.quadruples),
            )

            # Print the patched GOTO quadruple
            if self.print_traversal:
                print(
                    f"Patched GOTO at index {end_jump_index} to point to {len(self.quadruple_manager.quadruples)}"
                )

    # ************************************** LOOP STATEMENTS **************************************#
    # While loop - ciclo
    def enterCiclo(self, ctx: little_duckParser.CicloContext):
        """
        Enter a 'mientras' (while loop).
        Generate the beginning of the loop and manage jump positions.
        """
        if self.print_traversal:
            print("\n============= Entering 'mientras' (while loop) =============")

        # Save the current position (start of the loop condition) to the loop_start_stack
        loop_start = len(
            self.quadruple_manager.quadruples
        )  # Get the current quadruple index
        self.loop_start_stack.push(loop_start)  # Push the loop start position onto the loop_start_stack

        # Print the loop start position
        if self.print_traversal:
            print(f"Pushed loop start position {loop_start} onto the loop_start_stack")

        # Evaluate the loop condition expression
        expr_type = self.get_expression_type(ctx.expresion())

        # Check if the expression is not boolean
        if expr_type != "bool":
            raise Exception("Error: Loop condition expression must be of type 'bool'.")

        # If the expression is boolean
        else:
            # Pop the condition result from the operand stack
            condition_result = self.operand_stack.pop()
            self.type_stack.pop()  # Pop the operand's type from the type stack

            # Print the condition result
            if self.print_traversal:
                print(f"Operand in operand stack: {condition_result}")

            # Generate the GOTOF quadruple and push it to the condition_goto_stack
            quadruple = ("GOTOF", condition_result, None, None)
            self.quadruple_manager.push(quadruple)

            # Get the index of the GOTOF quadruple
            false_jump_quad_index = len(self.quadruple_manager.quadruples) - 1

            # Print the generated GOTOF quadruple
            if self.print_traversal:
                print(
                    f"Generated GOTOF quadruple at index {false_jump_quad_index}: {quadruple}"
                )

            # Push the GOTOF quadruple's index onto the condition_goto_stack for future patching
            self.condition_goto_stack.push(false_jump_quad_index)

    def exitCiclo(self, ctx: little_duckParser.CicloContext):
        """
        Exit a 'ciclo' (while loop).
        Generate the appropriate quadruples to handle looping.
        """
        # Print that we are exiting the while loop
        if self.print_traversal:
            print("============= Exiting 'ciclo' (while loop) =============\n")

        # Pop the false jump index from the condition_goto_stack
        false_jump_quad_index = (
            self.condition_goto_stack.pop()
        )  # Get the false jump index, after the loop condition

        # Pop the loop start position from the loop_start_stack
        loop_start = self.loop_start_stack.pop()

        # Generate a GOTO quadruple to return to the loop start
        quadruple = ("GOTO", None, None, loop_start)
        self.quadruple_manager.push(quadruple)
        goto_quad_index = len(self.quadruple_manager.quadruples) - 1

        if self.print_traversal:
            print(
                f"Generated GOTO quadruple at index {goto_quad_index}: {quadruple}"
            )

        # Patch the GOTOF quadruple to point to the instruction after the loop
        self.quadruple_manager.quadruples[false_jump_quad_index] = (
            "GOTOF",
            self.quadruple_manager.quadruples[false_jump_quad_index][1],
            None,
            len(self.quadruple_manager.quadruples),
        )

        # Print the patched GOTOF quadruple
        if self.print_traversal:
            print(
                f"Patched GOTOF at index {false_jump_quad_index} to point to {len(self.quadruple_manager.quadruples)}"
            )

    # ************************************** EXPRESSION HANDLING **************************************#
    # Get the type of an expression
    def get_expression_type(self, ctx: little_duckParser.ExpresionContext):
        """
        Determine the type of an expression by recursively analyzing its components.
        """
        # Check if the expression contains a comparison operator, the lowest in hierarchy
        if ctx.op_comparacion():
            # Comparison expression
            left_type = self.get_exp_type(
                ctx.exp(0)
            )  # Get the type of the left expression
            right_type = self.get_exp_type(
                ctx.exp(1)
            )  # Get the type of the right expression
            operator = ctx.op_comparacion().getText()  # Get the comparison operator

            # Print the comparison operation
            if self.print_traversal:
                print(f"Comparing {left_type} {operator} {right_type}")

            try:
                # Get the result type of the comparison operation
                result_type = self.semantic_cube.get_type(
                    left_type, right_type, operator
                )

                # Push the result onto the stacks
                self.create_temp_quadruple(operator, result_type)

                return result_type

            except TypeError as e:
                raise Exception(
                    f"Error: Incompatible types in expression: {left_type} {operator} {right_type}. {str(e)}"
                )
                return "error"
        else:
            # Single expression
            return self.get_exp_type(
                ctx.exp(0)
            )  # No comparison operator joining expressions, Check next in hierarchy

    def get_exp_type(self, ctx: little_duckParser.ExpContext):
        """
        Determine the type of an arithmetic expression (addition/subtraction).
        """
        # Check if the expression contains an arithmetic operator add or subtraction
        if len(ctx.termino()) > 1:
            # Check if left or right expression is a term
            left_type = self.get_termino_type(ctx.termino(0))
            right_type = self.get_termino_type(ctx.termino(1))
            operator = ctx.getChild(1).getText()  # Get the arithmetic operator

            # Print the arithmetic operation
            if self.print_traversal:
                print(f"Exp Type {left_type} {operator} {right_type}")

            try:
                # Get the result type of the arithmetic operation
                result_type = self.semantic_cube.get_type(
                    left_type, right_type, operator
                )

                # Print the generated quadruple
                if self.print_traversal:
                    print(
                        f"Generated quadruple: {left_type} {operator} {right_type} -> {result_type}"
                    )

                # Push the result onto the stacks
                self.create_temp_quadruple(operator, result_type)

                return result_type

            except TypeError as e:
                raise Exception(
                    f"Error: Incompatible types in expression: {left_type} {operator} {right_type}. {str(e)}"
                )
                return "error"
        else:
            return self.get_termino_type(
                ctx.termino(0)
            )  # No exp operator joining terms, Check next in hierarchy

    def get_termino_type(self, ctx: little_duckParser.TerminoContext):
        """
        Determine the type of a term (multiplication/division).
        """
        # Check if the term contains an arithmetic operator multiplication or division
        if len(ctx.factor()) > 1:
            # Check if left or right term is a factor
            left_type = self.get_factor_type(ctx.factor(0))
            right_type = self.get_factor_type(ctx.factor(1))
            operator = ctx.getChild(1).getText()  # Get the arithmetic operator

            # Print the term operation
            if self.print_traversal:
                print(f"Termino type {left_type} {operator} {right_type}")

            try:
                # Get the result type of the term operation
                result_type = self.semantic_cube.get_type(
                    left_type, right_type, operator
                )

                # Print the generated quadruple
                if self.print_traversal:
                    print(
                        f"Generated quadruple: {left_type} {operator} {right_type} -> {result_type}"
                    )

                # Push the result onto the stacks
                self.create_temp_quadruple(operator, result_type)
                return result_type

            except TypeError as e:
                raise Exception(
                    f"Error: Incompatible types in term: {left_type} {operator} {right_type}. {str(e)}"
                )
                return "error"
        else:
            return self.get_factor_type(ctx.factor(0))

    def get_factor_type(self, ctx: little_duckParser.FactorContext):
        """
        Determine the type of a factor (variable, constant, or expression) and manage operands.
        """
        # Check if the factor is a variable, constant, or expression
        if ctx.ID():  # Variable
            var_name = ctx.ID().getText()
            scope = self.variable_table.find_scope(var_name, self.current_scope)

            # Check if the variable is declared
            if scope:
                # Get the variable's type and address
                var_type = self.variable_table.get_variable_type(scope, var_name)
                var_address = self.variable_table.get_variable_address(scope, var_name)

                # Push the variable's address and type to their respective stacks
                self.operand_stack.push(var_address)
                self.type_stack.push(var_type)

                return var_type

            else:
                raise Exception(f"Error: Variable '{var_name}' is not declared.")
                return "error"

        elif ctx.cte():  # Constant
            if ctx.cte().CTE_ENT():  # Integer
                value = ctx.cte().CTE_ENT().getText()  # Get the integer value
                var_type = "entero"  # Set the type to integer
                value = int(value)  # Convert to integer

            elif ctx.cte().CTE_FLOT():  # Float
                value = ctx.cte().CTE_FLOT().getText()  # Get the float value
                var_type = "flotante"  # Set the type to float
                value = float(value)  # Convert to float

            else:
                raise Exception("Error: Invalid constant.")
                return "error"

            # Allocate or get the address of the constant
            address = self.virtual_memory.get_constant_address(value, var_type)

            # Ensure the constant is stored with the correct data type
            if address not in self.virtual_memory.constants_memory:
                self.virtual_memory.constants_memory[address] = value

            # Push the constant's address and type onto the operand stack
            self.operand_stack.push(address)
            self.type_stack.push(var_type)

            return var_type

        elif ctx.expresion():  # Expression
            # Recursively check the expression type
            return self.get_expression_type(ctx.expresion())

        else:
            raise Exception("Error: Invalid factor.")
            return "error"

    def create_temp_quadruple(self, operator, result_type):
        """
        Create a temporary quadruple for intermediate operations, allocate memory, and update stacks.
        """
        try:
            # Pop the right and left operands from the operand stack
            right_operand = self.operand_stack.pop()
            left_operand = self.operand_stack.pop()
            self.type_stack.pop()  # Pop the right operand's type
            self.type_stack.pop()  # Pop the left operand's type

            # Allocate a temporary address for the result
            temp_address = self.virtual_memory.get_temp_address(result_type)

            # Initialize the temporary variable in memory
            if result_type == "entero":
                self.virtual_memory.set_value(temp_address, 0)

            elif result_type == "flotante":
                self.virtual_memory.set_value(temp_address, 0.0)

            elif result_type == "bool":
                self.virtual_memory.set_value(temp_address, False)

            else:
                self.virtual_memory.set_value(temp_address, None)

            # Push the temporary address onto the operand and type stacks
            self.operand_stack.push(temp_address)
            self.type_stack.push(result_type)

            # Generate the quadruple using addresses
            quadruple = (operator, left_operand, right_operand, temp_address)
            self.quadruple_manager.push(quadruple)

            # Print the generated quadruple
            if self.print_traversal:
                print(f"Generated temp quadruple: {quadruple}")

        except Exception as e:
            raise Exception(f"Error creating temporary quadruple: {e}")

    # ************************************** FUNCTION STATEMENT **************************************#
    def enterFunc_decl(self, ctx: little_duckParser.Func_declContext):
        """
        Enter a function declaration.
        Set up the function scope, record the function's starting quadruple index,
        and process parameters.
        """
        func_name = ctx.ID().getText()  # Get the function name
        self.current_scope = func_name  # Set the current scope to the function name
        self.current_function = func_name  # Set the current function name

        # Initialize the function scope in the variable table
        self.variable_table.set_scope(self.current_scope)

        # Initialize function information
        self.function_table.add_function(func_name, len(self.quadruple_manager.quadruples))

        # Generate FUNC_START quadruple
        quadruple = ('FUNC_START', func_name, None, None)
        self.quadruple_manager.push(quadruple)

        # Print function entry
        if self.print_traversal:
            print(f"\nEntering function '{func_name}'")
            print(f"Generated FUNC_START quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {quadruple}")

        # Push a new local memory onto the stack
        self.virtual_memory.push_local_memory()

        # Process parameters
        if ctx.param_list():
            params = ctx.param_list().param()
            for param in params:
                param_name = param.ID().getText()  # Get the parameter name
                param_type = param.tipo().getText()  # Get the parameter type

                # Allocate address for parameter
                address = self.virtual_memory.get_address(param_type, 'local')  # Get the address of the parameter

                # Add parameter to variable table
                self.variable_table.add_variable(self.current_scope, param_name, param_type, address)  # Add the parameter to the variable table

                # Add parameter to function table
                self.function_table.add_parameter(func_name, param_name, param_type, address)  # Add the parameter to the function table

                if self.print_traversal:
                    print(f"Parameter: {param_name} : {param_type}, Address: {address}")

    def exitFunc_decl(self, ctx: little_duckParser.Func_declContext):
        """
        Exit a function declaration.
        Generate ENDFUNC quadruple and reset scope.
        """
        # Generate ENDFUNC quadruple
        quadruple = ('ENDFUNC', None, None, None)
        self.quadruple_manager.push(quadruple)

        if self.print_traversal:
            print(f"Generated ENDFUNC quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {quadruple}")
            print(f"Exiting function '{self.current_function}'\n")

        # Pop local memory for the function
        self.virtual_memory.pop_local_memory()

        # Clean up variables in the function scope before resetting the scope
        self.variable_table.clean_variables(self.current_scope)

        # Reset scope
        self.current_scope = 'global'
        self.current_function = None

    def enterInicio(self, ctx: little_duckParser.InicioContext):
        """
        Enter the 'inicio' block.
        Patch the initial GOTO quadruple to jump here.
        """
        # Pop the initial GOTO index from the initial_goto_stack
        if self.initial_goto_stack.is_empty():
            raise Exception("Error: initial_goto_stack is empty. Cannot patch initial GOTO.")
        goto_index = self.initial_goto_stack.pop()

        # Patch the GOTO to point to the current quadruple index
        self.quadruple_manager.quadruples[goto_index] = (
            'GOTO', None, None, len(self.quadruple_manager.quadruples)
        )

        if self.print_traversal:
            print(f"Patched initial GOTO at index {goto_index} to point to {len(self.quadruple_manager.quadruples)}")

    def exitLlamada(self, ctx: little_duckParser.LlamadaContext):
        """
        Exit a function call.
        Generate ERA, PARAM, and GOSUB quadruples.
        """
        func_name = ctx.ID().getText() # Get the function name

        # Check if function exists
        if func_name not in self.function_table.functions:
            raise Exception(f"Error: Function '{func_name}' is not declared.")

        function_info = self.function_table.get_function(func_name) # Get the function information
        num_params = self.function_table.get_function_param_count(func_name) # Get the number of parameters

        # Generate ERA quadruple
        quadruple = ('ERA', func_name, None, None)
        self.quadruple_manager.push(quadruple)

        if self.print_traversal:
            print(f"Generated ERA quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {quadruple}")

        # Handle arguments
        arg_list = ctx.arg_list().expresion() if ctx.arg_list() else [] # Get the list of arguments

        # Check if the number of arguments matches the number of parameters
        if len(arg_list) != num_params:
            raise Exception(f"Error: Function '{func_name}' expects {num_params} arguments, but {len(arg_list)} were provided.")

        # Iterate over each argument
        for idx, arg_expr in enumerate(arg_list):
            # Evaluate argument expression
            arg_type = self.get_expression_type(arg_expr) # Get the type of the argument expression
            arg_operand = self.operand_stack.pop() # Pop the argument's operand
            self.type_stack.pop() # Pop the argument's type

            param = function_info['params'][idx] # Get the parameter info dict
            param_type = param['type']
            param_address = param['address']

            # Type checking
            if arg_type != param_type: # Check if the argument type matches the parameter type
                raise Exception(f"Error: Type mismatch in argument {idx+1} of function '{func_name}': expected '{param_type}', got '{arg_type}'.")

            # Generate PARAM quadruple
            quadruple = ('PARAM', arg_operand, None, param_address) # Use the parameter's address
            self.quadruple_manager.push(quadruple)

            if self.print_traversal:
                print(f"Generated PARAM quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {quadruple}")

        # Generate GOSUB quadruple
        func_start_quad = function_info['quad_start']
        quadruple = ('GOSUB', func_name, None, func_start_quad)
        self.quadruple_manager.push(quadruple)

        if self.print_traversal:
            print(f"Generated GOSUB quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {quadruple}")

        # No need to handle return values as functions are void


    # ************************************** PRINT STATEMENT **************************************#
    # Method for imprime (print) statement
    def exitImprime(self, ctx: little_duckParser.ImprimeContext):
        """
        Exit the 'imprime' statement.
        Generate quadruples for each item in the print list to be printed on the same line.
        At the end, generate a 'print_newline' quadruple to add a newline.
        """
        # Get the list of items to print
        print_items = ctx.print_list().print_item()

        # Iterate over each item in the print list
        for item in print_items:

            # Check if the item is an expression
            if item.expresion():
                expr_type = self.get_expression_type(item.expresion())

                if expr_type != "error":
                    expr_operand = self.operand_stack.pop() # Pop the expression's operand
                    self.type_stack.pop() # Pop the expression's type
                    quadruple = ("print", expr_operand, None, None) # Generate a 'print' quadruple
                    self.quadruple_manager.push(quadruple) # Push the quadruple to the quadruple manager

                    # Print the generated quadruple
                    if self.print_traversal:
                        print(f"Generated quadruple for printing expression: {quadruple}")
                else:
                    raise Exception("Error: Got an error in expression validation.")

            # Check if the item is a string literal
            elif item.STRING_LITERAL():
                string_value = item.STRING_LITERAL().getText() # Get the string value
                string_value = string_value[1:-1]  # Remove the quotes
                address = self.virtual_memory.get_constant_address(string_value, "string") # Get the address of the string
                quadruple = ("print_str", address, None, None) # Generate a 'print_str' quadruple
                self.quadruple_manager.push(quadruple) # Push the quadruple to the quadruple manager

                # Print the generated quadruple
                if self.print_traversal:
                    print(f"Generated quadruple for printing string: {quadruple}")

            else:
                raise Exception("Error: Invalid print item encountered.")

        # After all items, add a 'print_newline' quadruple
        quadruple = ("print_newline", None, None, None)
        self.quadruple_manager.push(quadruple)

        # Print the generated quadruple
        if self.print_traversal:
            print(f"Generated quadruple for printing newline: {quadruple}")

    # ************************************** SCOPE MANAGEMENT **************************************#
    def enterCuerpo(self, ctx: little_duckParser.CuerpoContext):
        """
        Enter a block of statements (cuerpo).
        """
        # This method can be used to handle scope or other setup if needed
        pass

    def exitCuerpo(self, ctx: little_duckParser.CuerpoContext):
        """
        Exit a block of statements (cuerpo).
        """
        pass

    # ************************************** ERROR HANDLING **************************************#
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Custom syntax error handler.
        """
        print(f"Syntax error at line {line}, column {column}: {msg}")
