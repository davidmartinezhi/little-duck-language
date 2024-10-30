from src.semantics.semantic_cube import SemanticCube
from src.semantics.variable_table import VariableTable
from src.semantics.function_table import FunctionTable
from src.semantics.stack import Stack

# Global variables and structures
variable_table = VariableTable()
function_table = FunctionTable()
semantic_cube = SemanticCube()
current_scope = "global"
current_function = None
var_stack = []
operand_stack = Stack()
operator_stack = Stack()
type_stack = Stack()


def set_scope(scope):
    """
    Sets the current scope and creates the scope in the variable table if it does not exist.

    Args:
        scope (str): Name of the new scope.
    """
    global current_scope
    current_scope = scope
    variable_table.set_scope(scope)


def save_variable(var_id):
    """
    Temporarily saves a variable for later declaration.

    Args:
        var_id (str): Identifier of the variable.

    Raises:
        Exception: If the variable has already been declared in the current scope.
    """
    if var_id in variable_table.variables[current_scope] or var_id in var_stack:
        raise Exception(f"Variable {var_id} already declared in scope {current_scope}.")
    var_stack.append(var_id)


def save_type(var_type):
    """
    Assigns the type to the temporarily saved variables and adds them to the variable table.

    Args:
        var_type (str): Type of the variables.
    """
    for var_id in var_stack:
        variable_table.add_variable(var_id, var_type, current_scope)
    var_stack.clear()


def save_function(func_id, func_type=None):
    """
    Saves a new function in the function table.

    Args:
        func_id (str): Identifier of the function.
        func_type (str, optional): Return type of the function. Defaults to None, which is interpreted as "void".

    Raises:
        Exception: If the function has already been declared.
    """
    global current_function
    current_function = func_id
    if func_type is not None:
        function_table.add_function(func_id)
    else:
        function_table.add_function(func_id)


def save_parameter(param_id, param_type):
    """
    Saves a function parameter in the function's parameter table and the variable table.

    Args:
        func_id (str): Identifier of the function.
        param_id (str): Identifier of the parameter.
        param_type (str): Type of the parameter.
    """
    function_table.add_function_param(func_id=current_function, param={param_id: param_type})
    variable_table.add_variable(current_scope, param_id, param_type)


def stack_constant(number):
    """
    Pushes a numeric constant onto the operand stack and its type onto the type stack.

    Args:
        number (str): Numeric value as a string.
    """
    result = parse_number(number)
    operand_stack.push(result)
    type_stack.push(identify_number_type(number))


def stack_id(id):
    """
    Pushes an identifier onto the operand stack and its type onto the type stack.

    Args:
        id (str): Identifier of the variable.
    """
    var_type = variable_table.get_variable_type(id, current_scope)
    if var_type is None:
        # Search in higher scopes
        scope = variable_table.find_scope(id)
        if scope is not None:
            var_type = variable_table.get_variable_type(id, scope)
        else:
            raise Exception(f"Variable {id} not declared.")
    operand_stack.push(id)
    type_stack.push(var_type)


def identify_number_type(num_str):
    """
    Identifies the type of a number represented as a string.

    Args:
        num_str (str): String representing a number.

    Returns:
        str: 'int' if integer, 'float' if float, or 'Not a valid number' if not a number.
    """
    try:
        int(num_str)
        return "int"
    except ValueError:
        try:
            float(num_str)
            return "float"
        except ValueError:
            return "Not a valid number"


def parse_number(num_str):
    """
    Converts a numeric string into its corresponding numeric value.

    Args:
        num_str (str): String representing a number.

    Returns:
        int or float: Corresponding numeric value.

    Raises:
        ValueError: If the string does not represent a valid number.
    """
    if isinstance(num_str, (int, float)):
        return num_str
    try:
        return int(num_str)
    except ValueError:
        return float(num_str)


def sum_res():
    """
    Handles addition and subtraction operations, performing type checking.

    Raises:
        Exception: If the types are not compatible for the operation.
    """
    if not operator_stack.is_empty():
        if operator_stack.peek() == "+" or operator_stack.peek() == "-":
            right_operand = operand_stack.pop()
            right_type = type_stack.pop()
            left_operand = operand_stack.pop()
            left_type = type_stack.pop()
            operator = operator_stack.pop()
            result_type = semantic_cube.get_type(left_type, right_type, operator)
            if result_type != "error":
                # In semantic analysis, we verify types
                operand_stack.push("temp_result")  # Placeholder
                type_stack.push(result_type)
            else:
                raise Exception(f"Type mismatch in operation {left_type} {operator} {right_type}")


def mult_div():
    """
    Handles multiplication and division operations, performing type checking.

    Raises:
        Exception: If the types are not compatible for the operation.
    """
    if not operator_stack.is_empty():
        if operator_stack.peek() == "*" or operator_stack.peek() == "/":
            right_operand = operand_stack.pop()
            right_type = type_stack.pop()
            left_operand = operand_stack.pop()
            left_type = type_stack.pop()
            operator = operator_stack.pop()
            result_type = semantic_cube.get_type(left_type, right_type, operator)
            if result_type != "error":
                # In semantic analysis, we verify types
                operand_stack.push("temp_result")  # Placeholder
                type_stack.push(result_type)
            else:
                raise Exception(f"Type mismatch in operation {left_type} {operator} {right_type}")


def compare_exp():
    """
    Handles comparison operations, performing type checking.

    Raises:
        Exception: If the types are not compatible for the operation.
    """
    if not operator_stack.is_empty():
        if operator_stack.peek() in ("<", ">", "!="):
            right_operand = operand_stack.pop()
            right_type = type_stack.pop()
            left_operand = operand_stack.pop()
            left_type = type_stack.pop()
            operator = operator_stack.pop()
            result_type = semantic_cube.get_type(left_type, right_type, operator)
            if result_type != "error":
                # In semantic analysis, we verify types
                operand_stack.push("temp_result")  # Placeholder
                type_stack.push(result_type)
            else:
                raise Exception(f"Type mismatch in operation {left_type} {operator} {right_type}")


def add_sum_sub(operator):
    """
    Pushes an addition or subtraction operator onto the operator stack.

    Args:
        operator (str): Operator ('+' or '-').
    """
    operator_stack.push(operator)


def add_mult_div(operator):
    """
    Pushes a multiplication or division operator onto the operator stack.

    Args:
        operator (str): Operator ('*' or '/').
    """
    operator_stack.push(operator)


def add_compare(operator):
    """
    Pushes a comparison operator onto the operator stack.

    Args:
        operator (str): Operator ('<', '>', '!=').
    """
    operator_stack.push(operator)


def assign_expression(id):
    """
    Handles the assignment of an expression to a variable, performing type checking.

    Args:
        id (str): Identifier of the variable to assign.

    Raises:
        Exception: If the types are not compatible for the assignment.
    """
    operand = operand_stack.pop()
    operand_type = type_stack.pop()
    var_type = variable_table.get_variable_type(id, current_scope)
    if var_type is None:
        # Search in higher scopes
        scope = variable_table.find_scope(id)
        if scope is not None:
            var_type = variable_table.get_variable_type(id, scope)
        else:
            raise Exception(f"Variable {id} not declared.")
    if semantic_cube.get_type(var_type, operand_type, '=') == "error":
        raise Exception(f"Type mismatch in assignment to variable {id}.")
    else:
        # Valid assignment in semantic terms
        pass


def end_global():
    """
    Clears global functions and variables at the end of the program.
    """
    function_table.clean_functions()
    variable_table.clean_variables("global")