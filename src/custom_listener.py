from antlr4 import *
from generated.little_duckParser import little_duckParser
from generated.little_duckListener import little_duckListener

# Import semantic modules
from semantics.semantic_cube import SemanticCube
from semantics.variable_table import VariableTable
from semantics.stack import Stack
from semantics.quadruple import Quadruple
from semantics.virtual_memory import VirtualMemory


class LittleDuckCustomListener(little_duckListener):
    """
    Custom listener for the Little Duck language parser to perform semantic analysis.
    This listener overrides methods to handle variable declarations, assignments, expressions,
    conditional statements and while loops, integrating semantic checks and quadruple generation.
    """

    def __init__(self, print_traversal: bool = False):
        """
        Initialize semantic structures and variables needed for semantic analysis.
        """
        self.print_traversal = print_traversal

        # Initialize semantic structures
        self.variable_table = (
            VariableTable()
        )  # Symbol table to store variables and their attributes
        self.semantic_cube = (
            SemanticCube()
        )  # Semantic cube for type checking and operation validation
        self.quadruple_manager = (
            Quadruple()
        )  # Manages quadruples (intermediate code representation)
        self.virtual_memory = VirtualMemory()  # Add this line

        self.current_scope = "global"  # Tracks the current scope (e.g., global)

        self.var_stack = (  # Stack to temporarily store variable identifiers during parsing
            []
        )
        self.operand_stack = (  # Stack to manage operands in expression evaluation
            Stack()
        )
        self.type_stack = (  # Stack to manage operand types in expression evaluation
            Stack()
        )

        self.temp_var_counter = (  # Counter for generating unique temporary variable names
            0
        )
        self.label_counter = 0  # Counter for generating unique labels
        self.jump_stack = Stack()  # Stack to manage jumps for conditional statements

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

        if self.print_traversal:
            print("\n=============")
            print(f"Entering program: {program_name}")  # Print program name
            print("=============\n")

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
        self.quadruple_manager.push(
            end_quadruple
        )  # Push the END quadruple to the quadruple manager

        # Print the generated quadruples and memory contents
        if self.print_traversal:
            print(
                f"Generated END quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {end_quadruple}"
            )

            # Print the generated quadruples
            print("\nGenerated Quadruples:")
            for idx, quad in enumerate(self.quadruple_manager.quadruples):
                print(f"{idx}: {quad}")

            # Print the memory addresses with their values
            self.virtual_memory.print_memory()

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
                address = self.virtual_memory.get_address(var_type, self.current_scope)
                # Add the variable to the variable table with its address
                self.variable_table.add_variable(
                    self.current_scope, var_name, var_type, address
                )

                # Print the variable declaration information
                if self.print_traversal:
                    print(
                        f"Variable declaration: {var_name} : {var_type}, Address: {address}"
                    )

                # Initialize the variable in virtual memory with default value
                if var_type == "entero":
                    self.virtual_memory.set_value(address, 0)
                elif var_type == "flotante":
                    self.virtual_memory.set_value(address, 0.0)
                else:
                    self.virtual_memory.set_value(address, None)

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
        Perform type checking, generate condicion quadruples, and update jump stack.
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

            # Generate the GOTOF quadruple and push it to the quadruple manager
            quadruple = (
                "GOTOF",
                condition_result,
                None,
                None,
            )
            self.quadruple_manager.push(quadruple)

            # Push the GOTOF quadruple's index onto the jump stack for future patching
            self.jump_stack.push(
                len(self.quadruple_manager.quadruples) - 1
            )  # Push the index of the quadruple to the jump stack

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
            false_jump_index = (  # Pop the index of the quadruple from the jump stack
                self.jump_stack.pop()
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

        # Check if there is an 'sino' clause
        if ctx.SINO():

            # Print that we are entering the 'sino' clause
            if self.print_traversal:
                print("\n============= Entering 'sino' clause =============")

            # Pop the false jump index from the jump stack
            false_jump_index = self.jump_stack.pop()

            # Generate a GOTO to skip the else block after the if block executes
            quadruple = ("GOTO", None, None, None)
            self.quadruple_manager.push(quadruple)

            self.jump_stack.push(  # Push the GOTO's index onto the jump_stack for later patching
                len(self.quadruple_manager.quadruples) - 1
            )

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

        # Check if there is an 'sino' clause
        if ctx.SINO():

            # Print that we are exiting the 'sino' clause
            if self.print_traversal:
                print("============= Exiting 'sino' clause =============\n")

            # Pop the GOTO index from the jump stack
            end_jump_index = self.jump_stack.pop()

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

        # Save the current position (start of the loop condition) to the jump stack
        loop_start = len(
            self.quadruple_manager.quadruples
        )  # Get the current quadruple index
        self.jump_stack.push(
            loop_start
        )  # Push the loop start position onto the jump stack

        # Print the loop start position
        if self.print_traversal:
            print(f"Pushed loop start position {loop_start} onto the jump stack")

        # Evaluate the loop condition expression
        expr_type = self.get_expression_type(ctx.expresion())

        # Check if the expression is not boolean
        if expr_type != "bool":
            raise Exception("Error: Loop condition expression must be of type 'bool'.")

        # If the expression is boolean
        else:
            # Pop the condition result from the operand stack
            condition_result = self.operand_stack.pop()

            # Print the condition result
            if self.print_traversal:
                print(f"Operand in operand stack: {condition_result}")

            # Generate the GOTOF quadruple and push it to the quadruple manager
            self.quadruple_manager.push(("GOTOF", condition_result, None, None))

            # Get the index of the GOTOF quadruple
            false_jump_quad_index = len(self.quadruple_manager.quadruples) - 1

            # Print the generated GOTOF quadruple
            if self.print_traversal:
                print(
                    f"Generated GOTOF quadruple at index {false_jump_quad_index}: ('GOTOF', {condition_result}, None, None)"
                )

            # Push the GOTOF quadruple's index onto the jump stack for future patching
            self.jump_stack.push(false_jump_quad_index)

    def exitCiclo(self, ctx: little_duckParser.CicloContext):
        """
        Exit a 'ciclo' (while loop).
        Generate the appropriate quadruples to handle looping.
        """

        # Print that we are exiting the while loop
        if self.print_traversal:
            print("============= Exiting 'ciclo' (while loop) =============\n")

        # Pop the false jump index and the loop start position from the jump stack
        false_jump_quad_index = (
            self.jump_stack.pop()
        )  # Get the false jump index, after the loop start
        loop_start = self.jump_stack.pop()  # Get the loop start position

        # Generate a GOTO quadruple to return to the loop start
        self.quadruple_manager.push(("GOTO", None, None, loop_start))
        goto_quad_index = len(self.quadruple_manager.quadruples) - 1

        if self.print_traversal:
            print(
                f"Generated GOTO quadruple at index {goto_quad_index}: ('GOTO', None, None, {loop_start})"
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
                self.create_temp_quadruple(left_type, right_type, operator, result_type)

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
        # Check if the expression contains an arithmetic operator add or substraction
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

                # Push the result onto the stacks
                if self.print_traversal:
                    print(
                        f"Generated quadruple: {left_type} {operator} {right_type} -> {result_type}"
                    )

                # Push the result onto the stacks
                self.create_temp_quadruple(left_type, right_type, operator, result_type)

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
                self.create_temp_quadruple(left_type, right_type, operator, result_type)
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
            # Recursively check the expression type, Check next in hierarchy
            return self.get_expression_type(ctx.expresion())

        else:
            raise Exception("Error: Invalid factor.")
            return "error"

    def create_temp_quadruple(self, left_type, right_type, operator, result_type):
        """
        Create a temporary quadruple for intermediate operations, allocate memory, and update stacks.
        """
        try:
            # Pop the right and left operands from the operand stack
            right_operand = self.operand_stack.pop()
            left_operand = self.operand_stack.pop()

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
                    quadruple = ("print", expr_operand, None, None) # Generate a 'print' quadruple
                    self.quadruple_manager.push(quadruple) # Push the quadruple to the quadruple manager
                    
                    # Print the generated quadruple
                    if self.print_traversal:
                        print(f"Generated quadruple for printing expression: {quadruple}")
                else:
                    raise Exception("Error: Got an error in expression validation.")
            
            # Check if the item is a variable
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
