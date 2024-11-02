# Custom listener for the Little Duck language
from antlr4 import *
from generated.little_duckParser import little_duckParser
from generated.little_duckListener import little_duckListener

# Import semantic modules
from semantics.semantic_cube import SemanticCube
from semantics.variable_table import VariableTable
from semantics.stack import Stack
from semantics.quadruple import Quadruple

class LittleDuckCustomListener(little_duckListener):
    """
    Custom listener for the Little Duck language parser to perform semantic analysis.
    This listener overrides methods to handle variable declarations, assignments, expressions,
    and conditional statements, integrating semantic checks and quadruple generation.
    """

    def __init__(self):
        """
        Initialize semantic structures and variables needed for semantic analysis.
        """
        # Initialize semantic structures
        self.variable_table = VariableTable()       # Symbol table to store variables and their attributes
        self.semantic_cube = SemanticCube()         # Semantic cube for type checking and operation validation
        self.quadruple_manager = Quadruple()        # Manages quadruples (intermediate code representation)
        
        self.current_scope = "global"               # Tracks the current scope (e.g., global)
        
        self.var_stack = []                         # Stack to temporarily store variable identifiers during parsing
        self.operand_stack = Stack()                # Stack to manage operands in expression evaluation
        self.operator_stack = Stack()               # Stack to manage operators in expression evaluation
        self.type_stack = Stack()                   # Stack to manage operand types in expression evaluation
        
        self.temp_var_counter = 0                   # Counter for generating unique temporary variable names
        self.label_counter = 0                      # Counter for generating unique labels
        self.jump_stack = Stack()                   # Stack to manage jumps for conditional statements

    #************************************** PROGRAM **************************************#
    # Program entry and exit - scope management
    def enterPrograma(self, ctx: little_duckParser.ProgramaContext):
        """
        Enter the root of the parse tree (program).
        Initialize the program and set the global scope.
        """
        self.variable_table.set_scope(self.current_scope)  # Set current scope to global scope
        program_name = ctx.ID().getText()                  # Get program name from the text of the ID
        print("\n=============") 
        print(f"Entering program: {program_name}")          # Print program name
        print("=============\n") 

    def exitPrograma(self, ctx: little_duckParser.ProgramaContext):
        """
        Exit the root of the parse tree (program).
        Perform cleanup and output the generated quadruples.
        """
        self.variable_table.clean_variables(self.current_scope)  # Clean up variables in the global scope
        print("\n=============") 
        print("Exiting program")                                 # Print exit message
        print("=============\n") 

        # Add END quadruple to signify the end of the program
        end_quadruple = ('END', None, None, None)
        self.quadruple_manager.push(end_quadruple)
        print(f"Generated END quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {end_quadruple}")
        
        # Print the generated quadruples
        print("\nGenerated Quadruples:")
        for idx, quad in enumerate(self.quadruple_manager.quadruples):
            print(f"{idx}: {quad}")

    #************************************** VARIABLES **************************************#
    # Variable declaration - add variables to scope
    def enterVars(self, ctx: little_duckParser.VarsContext):
        """
        Enter a variable declaration block.
        """
        print("\n=====Entering variable declaration=====")
        
    def exitVars(self, ctx: little_duckParser.VarsContext):
        """
        Exit a variable declaration block.
        """
        print("=====Exit variable declaration=====\n")
                
    def exitVar_decl(self, ctx: little_duckParser.Var_declContext):
        """
        Exit a variable declaration.
        Assign types to variables and add them to the variable table.
        """
        var_type = ctx.tipo().getText()                  # Get the type of the variable
        ids = ctx.id_list().ID()                         # Get the list of variable identifiers
        for id_token in ids:                             # Iterate over each variable identifier
            var_name = id_token.getText()
            if var_name in self.variable_table.variables[self.current_scope]:
                print(f"Error: Variable '{var_name}' is already declared in scope '{self.current_scope}'.")
            else:
                self.variable_table.add_variable(self.current_scope, var_name, var_type)
                print(f"Variable declaration: {var_name} : {var_type}")

    #************************************** ASSIGNMENT **************************************#
    # Assignment statement
    def exitAsigna(self, ctx: little_duckParser.AsignaContext):
        """
        Exit an assignment statement.
        Perform type checking and generate assignment quadruples.
        """
        var_name = ctx.ID().getText()
        # Pass self.current_scope to find_scope
        scope = self.variable_table.find_scope(var_name, self.current_scope)
        if not scope:
            print(f"Error: Variable '{var_name}' is not declared.")
        else:
            expr_type = self.get_expression_type(ctx.expresion())
            var_type = self.variable_table.get_variable_type(scope, var_name)
            try:
                result_type = self.semantic_cube.get_type(var_type, expr_type, '=')
                # Generate quadruple
                operand = self.operand_stack.pop()
                quadruple = ('=', operand, None, var_name)
                self.quadruple_manager.push(quadruple)
                print(f"Generated quadruple: {quadruple}")
            except TypeError as e:
                print(f"Type mismatch in assignment to variable '{var_name}'. {str(e)}")

    #************************************** CONDITIONAL STATEMENTS **************************************#
    # Conditional statement - si (if)
    def enterCondicion(self, ctx: little_duckParser.CondicionContext):
        print("Entering 'si' condition")
        expr_type = self.get_expression_type(ctx.expresion())
        if expr_type != 'bool':
            print("Error: Condition expression must be of type 'bool'.")
        else:
            condition_result = self.operand_stack.pop()
            quadruple = ('GOTOF', condition_result, None, None)
            self.quadruple_manager.push(quadruple)
            self.jump_stack.push(len(self.quadruple_manager.quadruples) - 1)
            print(f"Generated GOTOF quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {quadruple}")

    def exitCondicion(self, ctx: little_duckParser.CondicionContext):
        print("Exiting 'si' condition")
        if not ctx.condicion_else().SINO():
            # No else clause; patch the GOTOF here
            false_jump_index = self.jump_stack.pop()
            self.quadruple_manager.quadruples[false_jump_index] = (
                'GOTOF',
                self.quadruple_manager.quadruples[false_jump_index][1],
                None,
                len(self.quadruple_manager.quadruples)
            )
            print(f"Patched GOTOF at index {false_jump_index} to point to {len(self.quadruple_manager.quadruples)}")

    def enterCondicion_else(self, ctx: little_duckParser.Condicion_elseContext):
        if ctx.SINO():
            print("Entering 'sino' clause")
            # Pop the false jump index from the jump stack
            false_jump_index = self.jump_stack.pop()
            # Generate a GOTO to skip the else block after the if block executes
            quadruple = ('GOTO', None, None, None)
            self.quadruple_manager.push(quadruple)
            # Push the GOTO's index onto the jump_stack for later patching
            self.jump_stack.push(len(self.quadruple_manager.quadruples) - 1)
            print(f"Generated GOTO quadruple at index {len(self.quadruple_manager.quadruples) - 1}: {quadruple}")
            # Now patch the GOTOF to point to the instruction after the GOTO (start of else block)
            self.quadruple_manager.quadruples[false_jump_index] = (
                'GOTOF',
                self.quadruple_manager.quadruples[false_jump_index][1],
                None,
                len(self.quadruple_manager.quadruples)
            )
            print(f"Patched GOTOF at index {false_jump_index} to point to else block at {len(self.quadruple_manager.quadruples)}")

    def exitCondicion_else(self, ctx: little_duckParser.Condicion_elseContext):
        if ctx.SINO():
            print("Exiting 'sino' clause")
            # Pop the GOTO index from the jump stack
            end_jump_index = self.jump_stack.pop()
            # Update the GOTO to point to the instruction after the else block (or to END)
            self.quadruple_manager.quadruples[end_jump_index] = (
                'GOTO',
                None,
                None,
                len(self.quadruple_manager.quadruples)
            )
            print(f"Patched GOTO at index {end_jump_index} to point to {len(self.quadruple_manager.quadruples)}")
        # No else clause handling here, as it's already managed in exitCondicion

    #************************************** EXPRESSION HANDLING **************************************#
    # Get the type of an expression
    def get_expression_type(self, ctx: little_duckParser.ExpresionContext):
        """
        Determine the type of an expression by recursively analyzing its components.
        """
        if ctx.op_comparacion():
            # Comparison expression
            left_type = self.get_exp_type(ctx.exp(0))
            right_type = self.get_exp_type(ctx.exp(1))
            operator = ctx.op_comparacion().getText()
            try:
                result_type = self.semantic_cube.get_type(left_type, right_type, operator)
                # Push the result onto the stacks
                self.create_temp_quadruple(left_type, right_type, operator, result_type)
                return result_type
            except TypeError as e:
                print(f"Error: Incompatible types in expression: {left_type} {operator} {right_type}. {str(e)}")
                return 'error'
        else:
            # Single expression
            return self.get_exp_type(ctx.exp(0))

    def get_exp_type(self, ctx: little_duckParser.ExpContext):
        """
        Determine the type of an arithmetic expression (addition/subtraction).
        """
        if len(ctx.termino()) > 1:
            left_type = self.get_termino_type(ctx.termino(0))
            right_type = self.get_termino_type(ctx.termino(1))
            operator = ctx.getChild(1).getText()
            try:
                result_type = self.semantic_cube.get_type(left_type, right_type, operator)
                # Push the result onto the stacks
                print(f"Generated quadruple: {left_type} {operator} {right_type} -> {result_type}")
                self.create_temp_quadruple(left_type, right_type, operator, result_type)
                return result_type
            except TypeError as e:
                print(f"Error: Incompatible types in expression: {left_type} {operator} {right_type}. {str(e)}")
                return 'error'
        else:
            return self.get_termino_type(ctx.termino(0))

    def get_termino_type(self, ctx: little_duckParser.TerminoContext):
        """
        Determine the type of a term (multiplication/division).
        """
        if len(ctx.factor()) > 1:
            left_type = self.get_factor_type(ctx.factor(0))
            right_type = self.get_factor_type(ctx.factor(1))
            operator = ctx.getChild(1).getText()
            try:
                result_type = self.semantic_cube.get_type(left_type, right_type, operator)
                # Push the result onto the stacks
                print(f"Generated quadruple: {left_type} {operator} {right_type} -> {result_type}")
                self.create_temp_quadruple(left_type, right_type, operator, result_type)
                return result_type
            except TypeError as e:
                print(f"Error: Incompatible types in term: {left_type} {operator} {right_type}. {str(e)}")
                return 'error'
        else:
            return self.get_factor_type(ctx.factor(0))

    def get_factor_type(self, ctx: little_duckParser.FactorContext):
        """
        Determine the type of a factor (variable, constant, or expression).
        """
        if ctx.ID():
            var_name = ctx.ID().getText()
            # Pass self.current_scope to find_scope
            scope = self.variable_table.find_scope(var_name, self.current_scope)
            if scope:
                var_type = self.variable_table.get_variable_type(scope, var_name)
                # Push the variable onto the operand and type stacks
                self.operand_stack.push(var_name)
                self.type_stack.push(var_type)
                return var_type
            else:
                print(f"Error: Variable '{var_name}' is not declared.")
                return 'error'
        elif ctx.cte():
            if ctx.cte().CTE_ENT():
                value = ctx.cte().CTE_ENT().getText()
                var_type = 'entero'
            elif ctx.cte().CTE_FLOT():
                value = ctx.cte().CTE_FLOT().getText()
                var_type = 'flotante'
            else:
                print("Error: Invalid constant.")
                return 'error'
            # Push the constant onto the operand and type stacks
            self.operand_stack.push(value)
            self.type_stack.push(var_type)
            return var_type
        elif ctx.expresion():
            return self.get_expression_type(ctx.expresion())
        else:
            print("Error: Invalid factor.")
            return 'error'

    def create_temp_quadruple(self, left_type, right_type, operator, result_type):
        """
        Create a temporary quadruple for intermediate operations and update the stacks.
        """
        try:
            right_operand = self.operand_stack.pop()
            left_operand = self.operand_stack.pop()
            temp_var = f"t{self.temp_var_counter}"
            self.temp_var_counter += 1
            # Add temporary variable to variable table
            self.variable_table.add_variable(self.current_scope, temp_var, result_type)
            # Push the temporary variable onto the operand and type stacks
            self.operand_stack.push(temp_var)
            self.type_stack.push(result_type)
            # Generate the quadruple
            quadruple = (operator, left_operand, right_operand, temp_var)
            self.quadruple_manager.push(quadruple)
            print(f"Generated temp quadruple: {quadruple}")
        except Exception as e:
            print(f"Error creating temporary quadruple: {e}")

    #************************************** OTHER STATEMENTS **************************************#
    # Methods for loops, print statements, etc.
    def exitImprime(self, ctx: little_duckParser.ImprimeContext):
        """
        Handle the exit of a print statement.
        Generate quadruples for each item to be printed.
        """
        # Retrieve all print items from the print_list
        print_items = ctx.print_list().print_item()
        
        for item in print_items:
            if item.expresion():
                # Handle expression
                expr_type = self.get_expression_type(item.expresion())
                if expr_type != 'error':
                    # Retrieve the operand from the operand stack
                    expr_operand = self.operand_stack.pop()
                    # Generate quadruple for print operation
                    quadruple = ('print', expr_operand, None, None)
                    self.quadruple_manager.push(quadruple)
                    print(f"Generated quadruple for printing expression: {quadruple}")
                else:
                    print("Error: Cannot print an expression with type 'error'.")
            elif item.STRING_LITERAL():
                # Handle string literal
                string_value = item.STRING_LITERAL().getText()
                # Remove the surrounding quotes from the string
                string_value = string_value[1:-1]
                # Generate quadruple for printing a string literal
                quadruple = ('print_str', string_value, None, None)
                self.quadruple_manager.push(quadruple)
                print(f"Generated quadruple for printing string: {quadruple}")
            else:
                print("Error: Invalid print item encountered.")

    #************************************** SCOPE MANAGEMENT **************************************#
    def enterCuerpo(self, ctx: little_duckParser.CuerpoContext):
        """
        Enter a block of statements (cuerpo).
        """
        # Scope management if needed
        pass

    def exitCuerpo(self, ctx: little_duckParser.CuerpoContext):
        """
        Exit a block of statements (cuerpo).
        """
        # Scope management if needed
        pass

    #************************************** ERROR HANDLING **************************************#
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Custom syntax error handler.
        """
        print(f"Syntax error at line {line}, column {column}: {msg}")
