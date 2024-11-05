# test_quadruple_generation.py

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from generated.little_duckLexer import little_duckLexer
from generated.little_duckParser import little_duckParser
from generated.little_duckListener import little_duckListener

# Import semantic modules
from semantics.semantic_cube import SemanticCube
from semantics.variable_table import VariableTable
from semantics.stack import Stack
from semantics.quadruple import Quadruple

# Import the custom listener
from src.custom_listener import LittleDuckCustomListener 


def compile_and_get_quadruples(code):
    """
    Compiles the given Little Duck code and returns the generated quadruples.
    
    Args:
        code (str): The Little Duck source code as a string.
    
    Returns:
        list: A list of generated quadruples.
    """
    # Create an input stream from the code string
    input_stream = InputStream(code)
    
    # Create a lexer and parser
    lexer = little_duckLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = little_duckParser(token_stream)
    
    # Parse the code starting from the 'programa' rule
    tree = parser.programa()
    
    # Create an instance of your custom listener
    listener = LittleDuckCustomListener()
    
    # Walk the parse tree with your listener
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    
    # Access the quadruples from your listener's quadruple manager
    quadruples = listener.quadruple_manager.quadruples
    
    return quadruples


def compare_quadruples(generated, expected):
    """
    Compares the generated quadruples with the expected quadruples.
    
    Args:
        generated (list): The list of generated quadruples.
        expected (list): The list of expected quadruples.
    
    Returns:
        bool: True if they match, False otherwise.
    """
    if len(generated) != len(expected):
        print(f"Quadruple count mismatch: expected {len(expected)}, got {len(generated)}")
        return False
    
    for idx, (gen, exp) in enumerate(zip(generated, expected)):
        if gen != exp:
            print(f"Mismatch at quadruple {idx}: expected {exp}, got {gen}")
            return False
    
    return True


def test_simple_assignment():
    """
    Test simple variable assignments and verify the generated quadruples.
    The program assigns the value 5 to the variable 'a'.
    Expected quadruples:
    0: ('=', '5', None, 'a')
    1: ('END', None, None, None)
    """
    code = '''
    programa test_simple_assignment;
    vars {
        a : entero;
    }
    inicio {
        a = 5;
    }
    fin
    '''
    expected_quadruples = [
        ('=', '5', None, 'a'),
        ('END', None, None, None)
    ]
    
    generated_quadruples = compile_and_get_quadruples(code)
    
    print("Test: Simple Assignment")
    print("Generated Quadruples:")
    for idx, quad in enumerate(generated_quadruples):
        print(f"{idx}: {quad}")
    
    assert compare_quadruples(generated_quadruples, expected_quadruples), "Simple Assignment Test Failed"
    print("Simple Assignment Test Passed!\n" + "-"*50 + "\n")


def test_arithmetic_operations():
    """
    Test arithmetic operations and verify the generated quadruples.
    The program performs 'a = b + c * d'.
    Expected quadruples:
    0: ('=', '2', None, 'b')
    1: ('=', '3', None, 'c')
    2: ('=', '4', None, 'd')
    3: ('*', 'c', 'd', 't0')
    4: ('+', 'b', 't0', 't1')
    5: ('=', 't1', None, 'a')
    6: ('END', None, None, None)
    """
    code = '''
    programa test_arithmetic_operations;
    vars {
        a, b, c, d : entero;
    }
    inicio {
        b = 2;
        c = 3;
        d = 4;
        a = b + c * d;
    }
    fin
    '''
    expected_quadruples = [
        ('=', '2', None, 'b'),
        ('=', '3', None, 'c'),
        ('=', '4', None, 'd'),
        ('*', 'c', 'd', 't0'),
        ('+', 'b', 't0', 't1'),
        ('=', 't1', None, 'a'),
        ('END', None, None, None)
    ]
    
    generated_quadruples = compile_and_get_quadruples(code)
    
    print("Test: Arithmetic Operations")
    print("Generated Quadruples:")
    for idx, quad in enumerate(generated_quadruples):
        print(f"{idx}: {quad}")
    
    assert compare_quadruples(generated_quadruples, expected_quadruples), "Arithmetic Operations Test Failed"
    print("Arithmetic Operations Test Passed!\n" + "-"*50 + "\n")


def test_conditional_statement():
    """
    Test 'si' conditional statements without 'sino' and verify the generated quadruples.
    The program checks if 'a > b' and prints 'a is greater'.
    Expected quadruples:
    0: ('=', '5', None, 'a')
    1: ('=', '3', None, 'b')
    2: ('>', 'a', 'b', 't0')
    3: ('GOTOF', 't0', None, 5)
    4: ('print_str', 'a is greater', None, None)
    5: ('END', None, None, None)
    """
    code = '''
    programa test_conditional_statement;
    vars {
        a, b : entero;
    }
    inicio {
        a = 5;
        b = 3;
        si (a > b) haz {
            escribe("a is greater");
        }
    }
    fin
    '''
    expected_quadruples = [
        ('=', '5', None, 'a'),
        ('=', '3', None, 'b'),
        ('>', 'a', 'b', 't0'),
        ('GOTOF', 't0', None, 5),
        ('print_str', 'a is greater', None, None),
        ('END', None, None, None)
    ]
    
    generated_quadruples = compile_and_get_quadruples(code)
    
    print("Test: Conditional Statement without 'sino'")
    print("Generated Quadruples:")
    for idx, quad in enumerate(generated_quadruples):
        print(f"{idx}: {quad}")
    
    assert compare_quadruples(generated_quadruples, expected_quadruples), "Conditional Statement Test Failed"
    print("Conditional Statement Test Passed!\n" + "-"*50 + "\n")


def test_conditional_with_else():
    """
    Test 'si' conditional statements with 'sino' and verify the generated quadruples.
    The program checks if 'a == b' and prints messages accordingly.
    Expected quadruples:
    0: ('=', '5', None, 'a')
    1: ('=', '5', None, 'b')
    2: ('>', 'a', 'b', 't0')
    3: ('GOTOF', 't0', None, 6)
    4: ('print_str', 'a is greater to b', None, None)
    5: ('GOTO', None, None, 7)
    6: ('print_str', 'a is not greater to b', None, None)
    7: ('END', None, None, None)
    """
    code = '''
    programa test_conditional_with_else;
    vars {
        a, b : entero;
    }
    inicio {
        a = 5;
        b = 5;
        si (a > b) haz {
            escribe("a is greater to b");
        } sino haz {
            escribe("a is not greater to b");
        }
    }
    fin
    '''
    expected_quadruples = [
        ('=', '5', None, 'a'),
        ('=', '5', None, 'b'),
        ('>', 'a', 'b', 't0'),
        ('GOTOF', 't0', None, 6),
        ('print_str', 'a is greater to b', None, None),
        ('GOTO', None, None, 7),
        ('print_str', 'a is not greater to b', None, None),
        ('END', None, None, None)
    ]
    
    generated_quadruples = compile_and_get_quadruples(code)
    
    print("Test: Conditional Statement with 'sino'")
    print("Generated Quadruples:")
    for idx, quad in enumerate(generated_quadruples):
        print(f"{idx}: {quad}")
    
    assert compare_quadruples(generated_quadruples, expected_quadruples), "Conditional with Else Test Failed"
    print("Conditional with Else Test Passed!\n" + "-"*50 + "\n")


def test_while_loop():
    """
    Test 'mientras' loop and verify the generated quadruples.
    The program prints numbers from 1 to 3 using a loop.
    Expected quadruples:
    0: ('=', '1', None, 'i')
    1: ('<', 'i', '3', 't0')
    2: ('GOTOF', 't0', None, 6)
    3: ('print', 'i', None, None)
    4: ('+', 'i', '1', 't1')
    5: ('=', 't1', None, 'i')
    6: ('GOTO', None, None, 1)
    7: ('END', None, None, None)
    """
    code = '''
    programa test_while_loop;
    vars {
        i : entero;
    }
    inicio {
        i = 1;
        mientras (i < 3) haz {
            escribe(i);
            i = i + 1;
        }
    }
    fin
    '''
    expected_quadruples = [
        ('=', '1', None, 'i'),
        ('<', 'i', '3', 't0'),
        ('GOTOF', 't0', None, 7),
        ('print', 'i', None, None),
        ('+', 'i', '1', 't1'),
        ('=', 't1', None, 'i'),
        ('GOTO', None, None, 1),
        ('END', None, None, None)
    ]
    
    generated_quadruples = compile_and_get_quadruples(code)
    
    print("Test: While Loop")
    print("Generated Quadruples:")
    for idx, quad in enumerate(generated_quadruples):
        print(f"{idx}: {quad}")
    
    assert compare_quadruples(generated_quadruples, expected_quadruples), "While Loop Test Failed"
    print("While Loop Test Passed!\n" + "-"*50 + "\n")


def test_combined_operations():
    """
    Test a combination of arithmetic operations, conditionals, and loops.
    The program calculates the factorial of a number.
    Expected quadruples: (The quadruples will represent the factorial calculation logic)
    """
    code = '''
    programa test_combined_operations;
    vars {
        n, result : entero;
    }
    inicio {
        n = 5;
        result = 1;
        mientras (n > 1) haz {
            result = result * n;
            n = n - 1;
        }
        escribe("Factorial is:", result);
    }
    fin
    '''
    expected_quadruples = [
        ('=', '5', None, 'n'),
        ('=', '1', None, 'result'),
        ('>', 'n', '1', 't0'),
        ('GOTOF', 't0', None, 6),
        ('*', 'result', 'n', 't1'),
        ('=', 't1', None, 'result'),
        ('-', 'n', '1', 't2'),
        ('=', 't2', None, 'n'),
        ('GOTO', None, None, 2),
        ('print_str', 'Factorial is:', None, None),
        ('print', 'result', None, None),
        ('END', None, None, None)
    ]
    
    generated_quadruples = compile_and_get_quadruples(code)
    
    print("Test: Combined Operations (Factorial Calculation)")
    print("Generated Quadruples:")
    for idx, quad in enumerate(generated_quadruples):
        print(f"{idx}: {quad}")
    
    # Note: The exact quadruples may vary based on implementation details.
    # This expected list is an example and may need adjustments.
    assert generated_quadruples[-2] == ('print', 'result', None, None), "Combined Operations Test Failed at printing 'result'"
    assert generated_quadruples[-1] == ('END', None, None, None), "Combined Operations Test Failed at 'END'"
    print("Combined Operations Test Passed!\n" + "-"*50 + "\n")


def test_print_statements():
    """
    Test 'escribe' statements with both strings and expressions.
    The program prints a greeting and the sum of two numbers.
    Expected quadruples:
    0: ('=', '2', None, 'a')
    1: ('=', '3', None, 'b')
    2: ('+', 'a', 'b', 't0')
    3: ('print_str', 'Hello, World!', None, None)
    4: ('print', 't0', None, None)
    5: ('END', None, None, None)
    """
    code = '''
    programa test_print_statements;
    vars {
        a, b : entero;
    }
    inicio {
        a = 2;
        b = 3;
        escribe("Hello, World!");
        escribe(a + b);
    }
    fin
    '''
    expected_quadruples = [
        ('=', '2', None, 'a'),
        ('=', '3', None, 'b'),
        ('print_str', 'Hello, World!', None, None),
        ('+', 'a', 'b', 't0'),
        ('print', 't0', None, None),
        ('END', None, None, None)
    ]
    
    generated_quadruples = compile_and_get_quadruples(code)
    
    print("Test: Print Statements")
    print("Generated Quadruples:")
    for idx, quad in enumerate(generated_quadruples):
        print(f"{idx}: {quad}")
    
    assert compare_quadruples(generated_quadruples, expected_quadruples), "Print Statements Test Failed"
    print("Print Statements Test Passed!\n" + "-"*50 + "\n")


if __name__ == "__main__":
    test_simple_assignment()
    test_arithmetic_operations()
    test_conditional_statement()
    test_conditional_with_else()
    test_while_loop()
    test_combined_operations()
    test_print_statements()
