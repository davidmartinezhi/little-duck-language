# Custom listener for the Little Duck language
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
    assignments, and expressions, integrating semantic checks and quadruple generation.
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
        self.current_function = None                 # Tracks the currently processing function
        
        self.var_stack = []                          # Stack to temporarily store variable identifiers during parsing. It's mainly for storing we don't need LIFO operations
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
        self.variable_table.set_scope(self.current_scope) # Sets current scope to global scope
        program_name = ctx.ID().getText() # Gets program name from the text of the ID in the context of the Programa rul
        print("\n=============") 
        print(f"Entering program: {program_name}") # Prints program name
        print("=============\n") 
    
    def exitPrograma(self, ctx: little_duckParser.ProgramaContext):
        """
        Exit the root of the parse tree (program).
        Performs cleanup and outputs the generated quadruples.
        """
        self.variable_table.clean_variables(self.current_scope) # Cleans up variables in the global scope
        print("\n=============") 
        print("Exiting program") # Prints program name
        print("=============\n") 
        
        # Prints the generated quadruples
        print("\nGenerated Quadruples:")
        for quad in self.quadruple_manager.quadruples:
            print(quad)

    #************************************** VARIABLES **************************************#
    # Variable declaration - add variables to scope
    def enterVars(self, ctx: little_duckParser.Var_declContext):
        """
        Enter a variable declaration.
        """
        print("\n=====Entering variable declaration=====")
        
    # Variable declaration - add variables to scope
    def exitVars(self, ctx: little_duckParser.Var_declContext):
        """
        Exit a variable declaration.
        """
        print("=====Exit variable declaration=====\n")
                
    def exitVar_decl(self, ctx: little_duckParser.Var_declContext):
        """
        Exit a variable declaration.
        Assigns types to variables and adds them to the variable table.
        """
        var_type = ctx.tipo().getText() # Gets the type of the variable from the text of the tipo in the context of the Var_decl rule
        ids = ctx.id_list().ID() # Gets the list of variable identifiers from the context of the id_list in the context of the Var_decl rule
        for id_token in ids: # Iterates over the list of variable identifiers
            var_name = id_token.getText() # Gets the text of the token
            if var_name in self.variable_table.variables[self.current_scope]: # Checks if the variable is already declared in the current scope
                print(f"Error: Variable '{var_name}' is already declared in scope '{self.current_scope}'.")
            else:
                self.variable_table.add_variable(self.current_scope, var_name, var_type) # Adds the variable to the variable table
                print(f"Variable declaration: {var_name} : {var_type}") # Prints the variable declaration

    #************************************** FUNCTIONS **************************************#
    # Function declaration entry and exit
    def enterFunc_decl(self, ctx: little_duckParser.Func_declContext):
        """
        Enter a function declaration.
        Sets up a new scope for the function and adds parameters to the variable table.
        """
        print("\n=====Function declaration=====")
        function_name = ctx.ID().getText() # Gets the function name from the text of the ID in the context of the Func_decl rule
        self.function_table.add_function(function_name) # Adds the function to the function table
        self.current_scope = function_name # Sets the current scope to the function name
        self.variable_table.set_scope(self.current_scope) # Sets the scope in the variable table to the current scope
        print(f"Entering function: {function_name}")

        # Handle parameters
        if ctx.param_list(): # Checks if the function has parameters
            for param_ctx in ctx.param_list().param(): # Iterates over the parameters
                param_name = param_ctx.ID().getText() # Gets the parameter name from the text of the ID in the context of the param rule
                param_type = param_ctx.tipo().getText() # Gets the parameter type from the text of the tipo in the context of the param rule
                # Add parameter to function table and variable table
                self.function_table.add_function_param(self.current_scope, {'name': param_name, 'type': param_type}) # current scope is the name of the function in this point
                self.variable_table.add_variable(self.current_scope, param_name, param_type)
                print(f"Parameter declaration: {param_name} : {param_type}")

    def exitFunc_decl(self, ctx: little_duckParser.Func_declContext):
        """
        Exit a function declaration.
        Cleans up the function scope.
        """
        print(f"Exiting function: {self.current_scope}")
        self.variable_table.clean_variables(self.current_scope) # Cleans up variables in the function scope
        self.current_scope = "global" # Resets the current scope to global scope
        print("=====Exit function declaration=====\n")
 
    #************************************** FUNCTION CALLS **************************************#
    def exitLlamada(self, ctx: little_duckParser.LlamadaContext):
        """
        Exit a function call.
        Checks if the function exists and validates arguments against parameters.
        """
        function_name = ctx.ID().getText() # Gets the function name from the text of the ID in the context of the Llamada rule

        if not self.function_table.get_function(function_name): # Checks if the function exists in the functions table
            print(f"Error: Function '{function_name}' is not declared.")
        else:
            expected_params = self.function_table.get_function_params(function_name) # Gets the expected parameters of the function
            expected_count = len(expected_params) # Gets the number of expected parameters
            arg_count = len(ctx.arg_list().expresion()) if ctx.arg_list() else 0 # Gets the number of arguments passed to the function

            if arg_count != expected_count: # Checks if the number of arguments matches the number of expected parameters
                print(f"Error: Argument count mismatch for function '{function_name}'. Expected {expected_count}, but got {arg_count}")
            else:
                for i in range(arg_count): # Iterates over the arguments
                    arg_expr = ctx.arg_list().expresion(i) # Gets the parameter of the argument
                    arg_type = self.get_expression_type(arg_expr) # Gets the type of the argument
                    param_name = self.function_table.get_function_param_id(function_name, i) # Gets the name of the parameter in hte specified id
                    expected_type = self.function_table.get_function_param_type(function_name, param_name) # Gets the type of the parameter
                    if arg_type != expected_type: # Checks if the type of the argument matches the type of the parameter
                        print(f"Error: Argument type mismatch for parameter {i+1} in function '{function_name}'. Expected: {expected_type}, but got: {arg_type}")
                    else: # If the argument type matches the parameter type
                        print(f"Argument {i+1} matches expected type '{expected_type}'.")

    #************************************** ASSIGNMENT **************************************#
    # Assignment statement
    def exitAsigna(self, ctx: little_duckParser.AsignaContext):
        """
        Exit an assignment statement.
        Performs type checking and generates assignment quadruples.
        """
        var_name = ctx.ID().getText() # Gets the variable name from the text of the ID in the context of the Asigna rule
        scope = self.variable_table.find_scope(var_name) # Finds the scope where the variable is declared
        if not scope: # Checks if the variable is declared
            print(f"Error: Variable '{var_name}' is not declared.")
        else: # If the variable is declared
            expr_type = self.get_expression_type(ctx.expresion()) # Gets the type of the expression
            var_type = self.variable_table.get_variable_type(scope, var_name) # Gets the type of the variable
            try:
                result_type = self.semantic_cube.get_type(var_type, expr_type, '=') # Gets the result type of the assignment
                # Generate quadruple
                operand = self.operand_stack.pop() # Pops the operand from the stack
                quadruple = ('=', operand, None, var_name) # Creates the quadruple
                self.quadruple_manager.push(quadruple) # Pushes the quadruple to the quadruple manager
                print(f"Generated quadruple: {quadruple}")
            except TypeError as e:
                print(f"Type mismatch in assignment to variable '{var_name}'. {str(e)}")

    #************************************** EXPRESSION HANDLING **************************************#
    # Get the type of an expression
    def get_expression_type(self, ctx: little_duckParser.ExpresionContext):
        """
        Determines the type of an expression by recursively analyzing its components.
        """
        if ctx.op_comparacion(): # Checks if the expression has a comparison operator
            # Comparison expression
            left_type = self.get_exp_type(ctx.exp(0)) # Gets the type of the left expression
            right_type = self.get_exp_type(ctx.exp(1)) # Gets the type of the right expression
            operator = ctx.op_comparacion().getText() # Gets the comparison operator
            try:
                result_type = self.semantic_cube.get_type(left_type, right_type, operator) # Gets the result type of the comparison
                # Push the result onto the stacks
                self.create_temp_quadruple(left_type, right_type, operator, result_type) # Creates a temporary quadruple
                return result_type # Returns the result type
            except TypeError as e:
                print(f"Error: Incompatible types in expression: {left_type} {operator} {right_type}") 
                return 'error'
        else:
            # Single expression
            return self.get_exp_type(ctx.exp(0)) # Gets the type of the expression

    def get_exp_type(self, ctx: little_duckParser.ExpContext):
        """
        Determines the type of an arithmetic expression (addition/subtraction).
        """
        if len(ctx.termino()) > 1:
            left_type = self.get_termino_type(ctx.termino(0)) # Gets the type of the left term
            right_type = self.get_termino_type(ctx.termino(1)) # Gets the type of the right term
            operator = ctx.getChild(1).getText() # Gets the operator
            try:
                result_type = self.semantic_cube.get_type(left_type, right_type, operator)
                # Push the result onto the stacks
                self.create_temp_quadruple(left_type, right_type, operator, result_type)
                return result_type
            except TypeError as e:
                print(f"Error: Incompatible types in expression: {left_type} {operator} {right_type}")
                return 'error'
        else:
            return self.get_termino_type(ctx.termino(0)) # Gets the type of the term

    def get_termino_type(self, ctx: little_duckParser.TerminoContext):
        """
        Determines the type of a term (multiplication/division).
        """
        if len(ctx.factor()) > 1:
            left_type = self.get_factor_type(ctx.factor(0)) # Gets the type of the left factor
            right_type = self.get_factor_type(ctx.factor(1)) # Gets the type of the right factor
            operator = ctx.getChild(1).getText() # Gets the operator
            try:
                result_type = self.semantic_cube.get_type(left_type, right_type, operator) # Gets the result type of the operation
                # Push the result onto the stacks
                self.create_temp_quadruple(left_type, right_type, operator, result_type) # Creates a temporary quadruple
                return result_type # Returns the result type
            except TypeError as e:
                print(f"Error: Incompatible types in term: {left_type} {operator} {right_type}")
                return 'error'
        else:
            return self.get_factor_type(ctx.factor(0))

    def get_factor_type(self, ctx: little_duckParser.FactorContext):
        """
        Determines the type of a factor (variable, constant, or expression).
        """
        if ctx.ID(): # Checks if the factor is a variable
            var_name = ctx.ID().getText() # Gets the variable name
            scope = self.variable_table.find_scope(var_name) # Finds the scope where the variable is declared
            if scope:
                var_type = self.variable_table.get_variable_type(scope, var_name) # Gets the type of the variable
                # Push the variable onto the operand and type stacks
                self.operand_stack.push(var_name) # Pushes the variable name onto the operand stack
                self.type_stack.push(var_type) # Pushes the variable type onto the type stack
                return var_type
            else:
                print(f"Error: Variable '{var_name}' is not declared.")
                return 'error'
        elif ctx.cte(): # Checks if the factor is a constant
            if ctx.cte().CTE_ENT(): # Checks if the constant is an integer
                value = ctx.cte().CTE_ENT().getText() # Gets the integer value
                var_type = 'entero' # Sets the type to integer
            elif ctx.cte().CTE_FLOT():
                value = ctx.cte().CTE_FLOT().getText() # Gets the float value
                var_type = 'flotante' # Sets the type to float
            else:
                print("Error: Invalid constant.") # Prints an error message
                return 'error'
            # Push the constant onto the operand and type stacks
            self.operand_stack.push(value) # Pushes the constant value onto the operand stack
            self.type_stack.push(var_type) # Pushes the constant type onto the type stack
            return var_type
        elif ctx.expresion():
            return self.get_expression_type(ctx.expresion()) # Gets the type of the expression
        else:
            print("Error: Invalid factor.")
            return 'error'

    def create_temp_quadruple(self, left_type, right_type, operator, result_type):
        """
        Creates a temporary quadruple for intermediate operations and updates the stacks.
        """
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

    #************************************** OTHER STATEMENTS **************************************#
    # methods for loops, conditionals, print statements, etc.

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

