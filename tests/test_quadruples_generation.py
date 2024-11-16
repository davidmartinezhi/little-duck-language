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
            print(f"Mismatch at quadruple {idx}:\nExpected: {exp}\nGot:      {gen}")
            return False
    
    return True


def test_simple_assignment():
    """
    Test simple variable assignments and verify the generated quadruples.
    The program assigns the value 5 to the variable 'a'.
    Expected quadruples:
    0: ('=', 10000, None, 1000)
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
        ('=', 10000, None, 1000),  # a = 5
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
    0: ('=', 10000, None, 1001)      # b = 2
    1: ('=', 10001, None, 1002)      # c = 3
    2: ('=', 10002, None, 1003)      # d = 4
    3: ('*', 1002, 1003, 7000)       # t0 = c * d
    4: ('+', 1001, 7000, 7001)       # t1 = b + t0
    5: ('=', 7001, None, 1000)       # a = t1
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
        ('=', 10000, None, 1001),      # b = 2
        ('=', 10001, None, 1002),      # c = 3
        ('=', 10002, None, 1003),      # d = 4
        ('*', 1002, 1003, 7000),       # t0 = c * d
        ('+', 1001, 7000, 7001),       # t1 = b + t0
        ('=', 7001, None, 1000),       # a = t1
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
    0: ('=', 10000, None, 1000)          # a = 5
    1: ('=', 10001, None, 1001)          # b = 3
    2: ('>', 1000, 1001, 9000)           # t0 = a > b
    3: ('GOTOF', 9000, None, 5)          # if not t0, jump to quad 5
    4: ('print_str', 12000, None, None)  # print "a is greater"
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
        ('=', 10000, None, 1000),          # a = 5
        ('=', 10001, None, 1001),          # b = 3
        ('>', 1000, 1001, 9000),           # t0 = a > b
        ('GOTOF', 9000, None, 5),          # if not t0, jump to quad 5
        ('print_str', 12000, None, None),  # print "a is greater"
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
    The program checks if 'a > b' and prints messages accordingly.
    Expected quadruples:
    0: ('=', 10000, None, 1000)          # a = 5
    1: ('=', 10000, None, 1001)          # b = 5
    2: ('>', 1000, 1001, 9000)           # t0 = a > b
    3: ('GOTOF', 9000, None, 6)          # if not t0, jump to quad 6
    4: ('print_str', 12000, None, None)  # print "a is greater to b"
    5: ('GOTO', None, None, 7)           # jump to quad 7
    6: ('print_str', 12001, None, None)  # print "a is not greater to b"
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
        ('=', 10000, None, 1000),          # a = 5
        ('=', 10000, None, 1001),          # b = 5
        ('>', 1000, 1001, 9000),           # t0 = a > b
        ('GOTOF', 9000, None, 6),          # if not t0, jump to quad 6
        ('print_str', 12000, None, None),  # print "a is greater to b"
        ('GOTO', None, None, 7),           # jump to quad 7
        ('print_str', 12001, None, None),  # print "a is not greater to b"
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
    The program prints numbers from 1 to 2 using a loop.
    Expected quadruples:
    0: ('=', 10000, None, 1000)         # i = 1
    1: ('<', 1000, 10001, 9000)         # t0 = i < 3
    2: ('GOTOF', 9000, None, 7)         # if not t0, jump to quad 7
    3: ('print', 1000, None, None)      # print i
    4: ('+', 1000, 10000, 7000)         # t1 = i + 1
    5: ('=', 7000, None, 1000)          # i = t1
    6: ('GOTO', None, None, 1)          # jump back to quad 1
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
        ('=', 10000, None, 1000),       # i = 1
        ('<', 1000, 10001, 9000),       # t0 = i < 3
        ('GOTOF', 9000, None, 7),       # if not t0, jump to quad 7
        ('print', 1000, None, None),    # print i
        ('+', 1000, 10000, 7000),       # t1 = i + 1
        ('=', 7000, None, 1000),        # i = t1
        ('GOTO', None, None, 1),        # jump back to quad 1
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
    Expected quadruples:
    0: ('=', 10000, None, 1000)          # n = 5
    1: ('=', 10001, None, 1001)          # result = 1
    2: ('>', 1000, 10001, 9000)          # t0 = n > 1
    3: ('GOTOF', 9000, None, 9)          # if not t0, jump to quad 9
    4: ('*', 1001, 1000, 7000)           # t1 = result * n
    5: ('=', 7000, None, 1001)           # result = t1
    6: ('-', 1000, 10001, 7001)          # t2 = n - 1
    7: ('=', 7001, None, 1000)           # n = t2
    8: ('GOTO', None, None, 2)           # jump back to quad 2
    9: ('print_str', 12000, None, None)  # print "Factorial is:"
    10: ('print', 1001, None, None)      # print result
    11: ('END', None, None, None)
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
        ('=', 10000, None, 1000),          # n = 5
        ('=', 10001, None, 1001),          # result = 1
        ('>', 1000, 10001, 9000),          # t0 = n > 1
        ('GOTOF', 9000, None, 9),          # if not t0, jump to quad 9
        ('*', 1001, 1000, 7000),           # t1 = result * n
        ('=', 7000, None, 1001),           # result = t1
        ('-', 1000, 10001, 7001),          # t2 = n - 1
        ('=', 7001, None, 1000),           # n = t2
        ('GOTO', None, None, 2),           # jump back to quad 2
        ('print_str', 12000, None, None),  # print "Factorial is:"
        ('print', 1001, None, None),       # print result
        ('END', None, None, None)
    ]
    
    generated_quadruples = compile_and_get_quadruples(code)
    
    print("Test: Combined Operations (Factorial Calculation)")
    print("Generated Quadruples:")
    for idx, quad in enumerate(generated_quadruples):
        print(f"{idx}: {quad}")
    
    assert compare_quadruples(generated_quadruples, expected_quadruples), "Combined Operations Test Failed"
    print("Combined Operations Test Passed!\n" + "-"*50 + "\n")


def test_print_statements():
    """
    Test 'escribe' statements with both strings and expressions.
    The program prints a greeting and the sum of two numbers.
    Expected quadruples:
    0: ('=', 10000, None, 1000)          # a = 2
    1: ('=', 10001, None, 1001)          # b = 3
    2: ('print_str', 12000, None, None)  # print "Hello, World!"
    3: ('+', 1000, 1001, 7000)           # t0 = a + b
    4: ('print', 7000, None, None)       # print t0
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
        ('=', 10000, None, 1000),          # a = 2
        ('=', 10001, None, 1001),          # b = 3
        ('print_str', 12000, None, None),  # print "Hello, World!"
        ('+', 1000, 1001, 7000),           # t0 = a + b
        ('print', 7000, None, None),       # print t0
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
