# listeners/little_duck_custom_listener.py

from antlr4 import *
from generated.little_duckParser import little_duckParser
from generated.little_duckListener import little_duckListener

# Import your semantic modules
from semantics.function_table import FunctionTable
from semantics.semantic_cube import SemanticCube
from semantics.variable_table import VariableTable
from semantics.stack import Stack
from semantics.quadruple import Quadruple

class LittleDuckCustomListener(little_duckListener):
    """
    Custom listener for the Little Duck language parser to perform semantic analysis.
    This listener overrides methods to handle variable declarations, function declarations,
    assignments, expressions, print statements, conditionals, and loops,
    integrating semantic checks and quadruple generation.
    """

    def __init__(self):
        """
        Initializes semantic structures and variables needed for semantic analysis.
        """
        # Initialize semantic structures
        self.variable_table = VariableTable()       # Symbol table to store variables and their attributes
        self.function_table = FunctionTable()       # Symbol table to store functions and their attributes
        self.semantic_cube = SemanticCube()         # Semantic cube for type checking and operation validation
        self.quadruple_manager = Quadruple()        # Manages quadruples (intermediate code representation)
        
        self.current_scope = "global"               # Tracks the current scope (e.g., global, function)
        self.current_function = None                # Tracks the currently processing function
        
        self.var_stack = []                          # Stack to temporarily store variable identifiers during parsing
        self.operand_stack = Stack()                 # Stack to manage operands in expression evaluation
        self.operator_stack = Stack()                # Stack to manage operators in expression evaluation
        self.type_stack = Stack()                    # Stack to manage operand types in expression evaluation
        
        self.temp_var_counter = 0                    # Counter for generating unique temporary variable names

    #************************************** PROGRAM **************************************#
    # Program entry and exit - scope management
    def enterPrograma(self, ctx: little_duckParser.ProgramaContext):
        """
        Enter the root of the parse tree (program).
        Initializes the program and sets the global scope.
        """
        self.variable_table.set_scope(self.current_scope)  # Sets current scope to global scope
        program_name = ctx.ID().getText()  # Gets program name from the ID token
        print("\n=============") 
        print(f"Entering program: {program_name}")  # Prints program name
        print("=============\n") 

    def exitPrograma(self, ctx: little_duckParser.ProgramaContext):
        """
        Exit the root of the parse tree (program).
        Performs cleanup and outputs the generated quadruples.
        """
        self.variable_table.clean_variables(self.current_scope)  # Cleans up variables in the global scope
        print("\n=============") 
        print("Exiting program")  # Prints exit message
        print("=============\n") 
        
        # Prints the generated quadruples
        print("\nGenerated Quadruples:")
        for quad in self.quadruple_manager.get_quadruples():
            print(quad)

    #************************************** VARIABLES **************************************#
    # Variable declaration - add variables to scope
    def enterVars(self, ctx: little_duckParser.VarsContext):
        """
        Enter a variable declaration section.
        """
        print("\n===== Entering Variable Declarations =====")
        # Additional preparatory actions can be added here if needed.

    def exitVars(self, ctx: little_duckParser.VarsContext):
        """
        Exit a variable declaration section.
        """
        print("===== Exiting Variable Declarations =====\n")
        # Additional cleanup actions can be added here if needed.

    def exitVar_decl(self, ctx: little_duckParser.Var_declContext):
        """
        Exit a variable declaration.
        Assigns types to variables and adds them to the variable table.
        """
        var_type = ctx.tipo().getText()  # Gets the type of the variable from the 'tipo' rule
        ids = ctx.id_list().ID()  # Gets the list of variable identifiers from the 'id_list' rule
        for id_token in ids:  # Iterates over each variable identifier
            var_name = id_token.getText()  # Gets the text of the ID token
            if var_name in self.variable_table.variables[self.current_scope]:
                # Checks if the variable is already declared in the current scope
                print(f"Error: Variable '{var_name}' is already declared in scope '{self.current_scope}'.")
            else:
                # Adds the variable to the variable table with its type
                self.variable_table.add_variable(self.current_scope, var_name, var_type)
                print(f"Variable declaration: {var_name} : {var_type}")

    #************************************** FUNCTIONS **************************************#
    # Function declaration entry and exit
    def enterFunc_decl(self, ctx: little_duckParser.Func_declContext):
        """
        Enter a function declaration.
        Sets up a new scope for the function and adds parameters to the variable table.
        """
        print("\n===== Entering Function Declaration =====")
        function_name = ctx.ID().getText()  # Gets the function name from the ID token
        self.function_table.add_function(function_name)  # Adds the function to the function table
        self.current_scope = function_name  # Sets the current scope to the function name
        self.variable_table.set_scope(self.current_scope)  # Sets the scope in the variable table to the current scope
        print(f"Entering function: {function_name}")

        # Handle parameters if any
        if ctx.param_list():  # Checks if the function has parameters
            for param_ctx in ctx.param_list().param():  # Iterates over each parameter
                param_name = param_ctx.ID().getText()  # Gets the parameter name
                param_type = param_ctx.tipo().getText()  # Gets the parameter type
                # Add parameter to function table and variable table
                self.function_table.add_function_param(self.current_scope, {'name': param_name, 'type': param_type})
                self.variable_table.add_variable(self.current_scope, param_name, param_type)
                print(f"Parameter declaration: {param_name} : {param_type}")

    def exitFunc_decl(self, ctx: little_duckParser.Func_declContext):
        """
        Exit a function declaration.
        Cleans up the function scope.
        """
        print(f"Exiting function: {self.current_scope}")
        self.variable_table.clean_variables(self.current_scope)  # Cleans up variables in the function scope
        self.current_scope = "global"  # Resets the current scope to global scope
        print("===== Exiting Function Declaration =====\n")

    #************************************** FUNCTION CALLS **************************************#
    def exitLlamada(self, ctx: little_duckParser.LlamadaContext):
        """
        Exit a function call.
        Checks if the function exists and validates arguments against parameters.
        Generates quadruples for the function call.
        """
        function_name = ctx.ID().getText()  # Gets the function name from the ID token

        if not self.function_table.get_function(function_name):
            # Checks if the function exists in the function table
            print(f"Error: Function '{function_name}' is not declared.")
        else:
            expected_params = self.function_table.get_function_params(function_name)  # Gets expected parameters
            expected_count = len(expected_params)  # Number of expected parameters
            arg_count = len(ctx.arg_list().expresion()) if ctx.arg_list() else 0  # Number of provided arguments

            if arg_count != expected_count:
                # Checks if the number of arguments matches the number of expected parameters
                print(f"Error: Argument count mismatch for function '{function_name}'. Expected {expected_count}, but got {arg_count}")
            else:
                # Validates each argument's type against the expected parameter type
                for i in range(arg_count):
                    arg_expr = ctx.arg_list().expresion(i)  # Gets the argument expression
                    arg_type = self.get_expression_type(arg_expr)  # Determines the argument type
                    param = expected_params[i]  # Gets the corresponding parameter
                    expected_type = param['type']  # Expected parameter type

                    if arg_type != expected_type:
                        # Checks for type mismatch
                        print(f"Error: Argument type mismatch for parameter {i+1} in function '{function_name}'. Expected: {expected_type}, but got: {arg_type}")
                    else:
                        print(f"Argument {i+1} matches expected type '{expected_type}'.")

            # Generate quadruple for function call
            # Assuming a 'call' operator with function name and number of arguments
            quadruple = ('call', function_name, arg_count, None)
            self.quadruple_manager.push(quadruple)
            print(f"Generated quadruple: {quadruple}")

    #************************************** ASSIGNMENT **************************************#
    # Assignment statement
    def exitAsigna(self, ctx: little_duckParser.AsignaContext):
        """
        Exit an assignment statement.
        Performs type checking and generates assignment quadruples.
        """
        var_name = ctx.ID().getText()  # Gets the variable name from the ID token
        scope = self.variable_table.find_scope(var_name)  # Finds the scope where the variable is declared

        if not scope:
            # Checks if the variable is declared
            print(f"Error: Variable '{var_name}' is not declared.")
        else:
            expr_type = self.get_expression_type(ctx.expresion())  # Gets the type of the expression
            var_type = self.variable_table.get_variable_type(scope, var_name)  # Gets the type of the variable

            try:
                # Checks if the assignment is semantically valid using the semantic cube
                result_type = self.semantic_cube.get_type(var_type, expr_type, '=')
                # Generate quadruple for assignment
                operand = self.operand_stack.pop()  # Pops the operand from the operand stack
                quadruple = ('=', operand, None, var_name)  # Creates the assignment quadruple
                self.quadruple_manager.push(quadruple)  # Pushes the quadruple to the quadruple manager
                print(f"Generated quadruple: {quadruple}")
                # Mark the variable as initialized
                self.variable_table.set_initialized(scope, var_name)
            except TypeError as e:
                # Handles type mismatch errors
                print(f"Type mismatch in assignment to variable '{var_name}'. {str(e)}")

    #************************************** EXPRESSION HANDLING **************************************#
    def get_expression_type(self, ctx: little_duckParser.ExpresionContext):
        """
        Determines the type of an expression by analyzing its components.
        Handles comparison expressions and arithmetic expressions.
        """
        if ctx.op_comparacion():
            # If there's a comparison operator, it's a comparison expression
            left_type = self.get_exp_type(ctx.exp(0))  # Gets the type of the left expression
            right_type = self.get_exp_type(ctx.exp(1))  # Gets the type of the right expression
            operator = ctx.op_comparacion().getText()  # Gets the comparison operator

            try:
                # Determines the result type using the semantic cube
                result_type = self.semantic_cube.get_type(left_type, right_type, operator)
                # Generate a quadruple for the comparison
                self.create_temp_quadruple(left_type, right_type, operator, result_type)
                return result_type
            except TypeError as e:
                # Handles type mismatch errors
                print(f"Error: Incompatible types in expression: {left_type} {operator} {right_type}")
                return 'error'
        else:
            # If there's no comparison operator, it's an arithmetic expression
            return self.get_exp_type(ctx.exp(0))  # Gets the type of the arithmetic expression

    def get_exp_type(self, ctx: little_duckParser.ExpContext):
        """
        Determines the type of an arithmetic expression (addition/subtraction).
        Handles multiple terms connected by '+' or '-'.
        """
        if len(ctx.termino()) > 1:
            # If there are multiple terms, it's a binary operation
            left_type = self.get_termino_type(ctx.termino(0))  # Gets the type of the left term
            right_type = self.get_termino_type(ctx.termino(1))  # Gets the type of the right term
            operator = ctx.getChild(1).getText()  # Gets the operator ('+' or '-')

            try:
                # Determines the result type using the semantic cube
                result_type = self.semantic_cube.get_type(left_type, right_type, operator)
                # Generate a quadruple for the arithmetic operation
                self.create_temp_quadruple(left_type, right_type, operator, result_type)
                return result_type
            except TypeError as e:
                # Handles type mismatch errors
                print(f"Error: Incompatible types in expression: {left_type} {operator} {right_type}")
                return 'error'
        else:
            # If there's only one term, return its type
            return self.get_termino_type(ctx.termino(0))

    def get_termino_type(self, ctx: little_duckParser.TerminoContext):
        """
        Determines the type of a term (multiplication/division).
        Handles multiple factors connected by '*' or '/'.
        """
        if len(ctx.factor()) > 1:
            # If there are multiple factors, it's a binary operation
            left_type = self.get_factor_type(ctx.factor(0))  # Gets the type of the left factor
            right_type = self.get_factor_type(ctx.factor(1))  # Gets the type of the right factor
            operator = ctx.getChild(1).getText()  # Gets the operator ('*' or '/')

            try:
                # Determines the result type using the semantic cube
                result_type = self.semantic_cube.get_type(left_type, right_type, operator)
                # Generate a quadruple for the multiplication/division operation
                self.create_temp_quadruple(left_type, right_type, operator, result_type)
                return result_type
            except TypeError as e:
                # Handles type mismatch errors
                print(f"Error: Incompatible types in term: {left_type} {operator} {right_type}")
                return 'error'
        else:
            # If there's only one factor, return its type
            return self.get_factor_type(ctx.factor(0))

    def get_factor_type(self, ctx: little_duckParser.FactorContext):
        """
        Determines the type of a factor (variable, constant, or expression).
        """
        if ctx.ID():
            # If the factor is a variable
            var_name = ctx.ID().getText()  # Gets the variable name
            scope = self.variable_table.find_scope(var_name)  # Finds the scope where the variable is declared

            if scope:
                var_type = self.variable_table.get_variable_type(scope, var_name)  # Gets the variable type
                # Push the variable onto the operand and type stacks
                self.operand_stack.push(var_name)
                self.type_stack.push(var_type)
                return var_type
            else:
                # Variable not declared
                print(f"Error: Variable '{var_name}' is not declared.")
                return 'error'
        elif ctx.cte():
            # If the factor is a constant
            if ctx.cte().CTE_ENT():
                # Integer constant
                value = ctx.cte().CTE_ENT().getText()  # Gets the integer value
                var_type = 'entero'  # Sets the type to 'entero'
            elif ctx.cte().CTE_FLOT():
                # Float constant
                value = ctx.cte().CTE_FLOT().getText()  # Gets the float value
                var_type = 'flotante'  # Sets the type to 'flotante'
            else:
                # Invalid constant
                print("Error: Invalid constant.")
                return 'error'
            # Push the constant onto the operand and type stacks
            self.operand_stack.push(value)
            self.type_stack.push(var_type)
            return var_type
        elif ctx.expresion():
            # If the factor is a nested expression
            return self.get_expression_type(ctx.expresion())  # Recursively get the type of the expression
        else:
            # Invalid factor
            print("Error: Invalid factor.")
            return 'error'

    def create_temp_quadruple(self, left_type, right_type, operator, result_type):
        """
        Creates a temporary quadruple for intermediate operations and updates the stacks.
        """
        right_operand = self.operand_stack.pop()  # Pops the right operand from the operand stack
        left_operand = self.operand_stack.pop()   # Pops the left operand from the operand stack
        temp_var = f"t{self.temp_var_counter}"    # Generates a unique temporary variable name
        self.temp_var_counter += 1                 # Increments the temporary variable counter
        # Add temporary variable to the variable table with its type
        self.variable_table.add_variable(self.current_scope, temp_var, result_type)
        # Push the temporary variable onto the operand and type stacks
        self.operand_stack.push(temp_var)
        self.type_stack.push(result_type)
        # Generate the quadruple
        quadruple = (operator, left_operand, right_operand, temp_var)
        self.quadruple_manager.push(quadruple)  # Pushes the quadruple to the quadruple manager
        print(f"Generated temp quadruple: {quadruple}")

    #************************************** PRINT STATEMENT **************************************#
    def enterImprime(self, ctx: little_duckParser.ImprimeContext):
        """
        Enter a print statement.
        Prepares any necessary actions before processing the print statement.
        """
        print("\n===== Entering Print Statement =====")
        # Additional preparatory actions can be added here if needed.

    def exitImprime(self, ctx: little_duckParser.ImprimeContext):
        """
        Exit a print statement.
        Evaluates the expressions to print and generates the corresponding quadruples.
        """
        
        # Retrieve the list of items to print
        print_items = ctx.print_list().print_item()
        
        for item in print_items:
            if item.expresion():
                # If the item is an expression, evaluate its type and generate quadruples
                expr_type = self.get_expression_type(item.expresion())
                expr_result = self.evaluate_expression(item.expresion())
                
                # Generate a quadruple for printing the expression result
                quadruple = ('print', expr_result, None, None)
                self.quadruple_manager.push(quadruple)
                print(f"Generated quadruple: {quadruple}")
            elif item.STRING_LITERAL():
                # If the item is a string literal, generate a quadruple to print it directly
                string_value = item.STRING_LITERAL().getText().strip('"')
                quadruple = ('print_string', string_value, None, None)
                self.quadruple_manager.push(quadruple)
                print(f"Generated quadruple: {quadruple}")
                
            print(f"Printed item: {item.getText()}")
            print("===== Exiting Print Statement =====\n")

    #************************************** CONDITION STATEMENT **************************************#
    def enterCondicion(self, ctx: little_duckParser.CondicionContext):
        """
        Enter a condition statement (si).
        Prepares any necessary actions before processing the condition.
        """
        print("\n===== Entering Condition Statement =====")
        # Additional preparatory actions can be added here if needed.

    def exitCondicion(self, ctx: little_duckParser.CondicionContext):
        """
        Exit a condition statement (si).
        Evaluates the condition and generates the corresponding quadruples for branching.
        """
        print("===== Exiting Condition Statement =====\n")
        
        # Evaluate the condition expression
        condition_expr = ctx.expresion()
        condition_type = self.get_expression_type(condition_expr)
        
        # Ensure the condition is of a valid type (boolean or integer)
        if condition_type not in ['bool', 'int']:
            print("Error: The condition expression must be of type 'bool' or 'int'.")
            return
        
        # Evaluate the condition expression and obtain the result
        condition_result = self.evaluate_expression(condition_expr)
        
        # Generate a quadruple for conditional branching (if_false jumps to else label)
        quadruple_if_false = ('if_false', condition_result, None, 'label_else')
        self.quadruple_manager.push(quadruple_if_false)
        print(f"Generated quadruple: {quadruple_if_false}")
        
        # Generate a quadruple for unconditional jump to the end of the if statement
        quadruple_goto = ('goto', None, None, 'label_end_if')
        self.quadruple_manager.push(quadruple_goto)
        print(f"Generated quadruple: {quadruple_goto}")
        
        # Assign the 'label_else' label to mark the beginning of the else block
        self.quadruple_manager.add_label('label_else')
        
        # Assign the 'label_end_if' label to mark the end of the conditional statement
        self.quadruple_manager.add_label('label_end_if')

    #************************************** LOOP STATEMENT **************************************#
    def enterCiclo(self, ctx: little_duckParser.CicloContext):
        """
        Enter a loop statement (mientras).
        Prepares any necessary actions before processing the loop.
        """
        print("\n===== Entering Loop Statement =====")
        # Additional preparatory actions can be added here if needed.

    def exitCiclo(self, ctx: little_duckParser.CicloContext):
        """
        Exit a loop statement (mientras).
        Evaluates the loop condition and generates the corresponding quadruples for looping.
        """
        print("===== Exiting Loop Statement =====\n")
        
        # Evaluate the loop condition expression
        condition_expr = ctx.expresion()
        condition_type = self.get_expression_type(condition_expr)
        
        # Ensure the condition is of a valid type (boolean or integer)
        if condition_type not in ['bool', 'int']:
            print("Error: The loop condition expression must be of type 'bool' or 'int'.")
            return
        
        # Evaluate the condition expression and obtain the result
        condition_result = self.evaluate_expression(condition_expr)
        
        # Generate a quadruple for conditional branching to exit the loop if the condition is false
        quadruple_if_false = ('if_false', condition_result, None, 'label_end_loop')
        self.quadruple_manager.push(quadruple_if_false)
        print(f"Generated quadruple: {quadruple_if_false}")
        
        # Generate a quadruple for unconditional jump back to the start of the loop
        quadruple_goto = ('goto', None, None, 'label_start_loop')
        self.quadruple_manager.push(quadruple_goto)
        print(f"Generated quadruple: {quadruple_goto}")
        
        # Assign the 'label_end_loop' label to mark the end of the loop
        self.quadruple_manager.add_label('label_end_loop')

    #************************************** HELPER FUNCTIONS **************************************#
    def evaluate_expression(self, ctx):
        """
        Evaluates an expression and returns the result or a temporary representation.
        This function generates a temporary variable to store the result of the expression.
        """
        # Generate a unique temporary variable name
        temp_var = f"t{self.temp_var_counter}"
        self.temp_var_counter += 1
        # Add temporary variable to the variable table with its type
        self.variable_table.add_variable(self.current_scope, temp_var, 'temp')
        # Push the temporary variable onto the operand and type stacks
        self.operand_stack.push(temp_var)
        self.type_stack.push('temp')
        return temp_var

    def add_label(self, label_name=None):
        """
        Assigns a label to the current position in the quadruples.
        If no label name is provided, generates a unique label.
        """
        label = self.quadruple_manager.add_label(label_name)
        print(f"Assigned label: {label}")

    #************************************** SCOPE MANAGEMENT **************************************#
    def enterCuerpo(self, ctx: little_duckParser.CuerpoContext):
        """
        Enter a block of statements (cuerpo).
        """
        # Additional scope management actions can be added here if needed.
        pass

    def exitCuerpo(self, ctx: little_duckParser.CuerpoContext):
        """
        Exit a block of statements (cuerpo).
        """
        pass
        # Additional cleanup actions can be added here if needed.

    #************************************** ERROR HANDLING **************************************#
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Custom syntax error handler.
        """
        print(f"Syntax error at line {line}, column {column}: {msg}")
