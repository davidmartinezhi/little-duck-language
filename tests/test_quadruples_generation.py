# tests/test_quadruples_generation.py

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from generated.little_duckLexer import little_duckLexer
from generated.little_duckParser import little_duckParser
from generated.little_duckListener import little_duckListener

# Import semantic modules
from semantics.semantic_cube import SemanticCube
from semantics.variable_table import VariableTable
from semantics.function_table import FunctionTable
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
    0: ('GOTO', None, None, 1)          # Initial GOTO to 'inicio' block
    1: ('=', 10000, None, 1000)        # a = 5 (constant 5 at address 10000 to 'a' at 1000)
    2: ('END', None, None, None)        # End of program
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
        ('GOTO', None, None, 1),          # Initial GOTO to 'inicio' block
        ('=', 10000, None, 1000),         # a = 5
        ('END', None, None, None)         # End of program
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
    0: ('GOTO', None, None, 1)          # Initial GOTO to 'inicio' block
    1: ('=', 10000, None, 1001)        # b = 2 (constant 2 at address 10000 to 'b' at 1001)
    2: ('=', 10001, None, 1002)        # c = 3 (constant 3 at address 10001 to 'c' at 1002)
    3: ('=', 10002, None, 1003)        # d = 4 (constant 4 at address 10002 to 'd' at 1003)
    4: ('*', 1002, 1003, 7000)         # t0 = c * d
    5: ('+', 1001, 7000, 7001)         # t1 = b + t0
    6: ('=', 7001, None, 1000)         # a = t1 (temp 7001 to 'a' at 1000)
    7: ('END', None, None, None)        # End of program
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
        ('GOTO', None, None, 1),          # Initial GOTO to 'inicio' block
        ('=', 10000, None, 1001),         # b = 2
        ('=', 10001, None, 1002),         # c = 3
        ('=', 10002, None, 1003),         # d = 4
        ('*', 1002, 1003, 7000),          # t0 = c * d
        ('+', 1001, 7000, 7001),          # t1 = b + t0
        ('=', 7001, None, 1000),          # a = t1
        ('END', None, None, None)         # End of program
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
    0: ('GOTO', None, None, 1)          # Initial GOTO to 'inicio' block
    1: ('=', 10000, None, 1000)        # a = 5 (constant 5 at address 10000 to 'a' at 1000)
    2: ('=', 10001, None, 1001)        # b = 3 (constant 3 at address 10001 to 'b' at 1001)
    3: ('>', 1000, 1001, 9000)         # t0 = a > b
    4: ('GOTOF', 9000, None, 7)        # if not t0, jump to quad 7 (END)
    5: ('print_str', 12000, None, None)  # print "a is greater" (string at 12000)
    6: ('print_newline', None, None, None),
    7: ('END', None, None, None)        # End of program
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
        ('GOTO', None, None, 1),          # Initial GOTO to 'inicio' block
        ('=', 10000, None, 1000),         # a = 5
        ('=', 10001, None, 1001),         # b = 3
        ('>', 1000, 1001, 9000),          # t0 = a > b
        ('GOTOF', 9000, None, 7),         # if not t0, jump to quad 7
        ('print_str', 12000, None, None), # print "a is greater"
        ('print_newline', None, None, None),
        ('END', None, None, None)         # End of program
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
    0: ('GOTO', None, None, 1)          # Initial GOTO to 'inicio' block
    1: ('=', 10000, None, 1000)        # a = 5 (constant 5 at address 10000 to 'a' at 1000)
    2: ('=', 10000, None, 1001)        # b = 5 (constant 5 at address 10000 to 'b' at 1001)
    3: ('>', 1000, 1001, 9000)         # t0 = a > b
    4: ('GOTOF', 9000, None, 8)        # if not t0, jump to quad 8
    5: ('print_str', 12000, None, None), # print "a is greater to b" (string at 12000)
    6: ('print_newline', None, None, None),
    7: ('GOTO', None, None, 9),           # jump to quad 9 (END)
    8: ('print_str', 12001, None, None),  # print "a is not greater to b" (string at 12001)
    9: ('print_newline', None, None, None),
    10: ('END', None, None, None)         # End of program
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
        ('GOTO', None, None, 1),             # Initial GOTO to 'inicio' block
        ('=', 10000, None, 1000),            # a = 5
        ('=', 10000, None, 1001),            # b = 5
        ('>', 1000, 1001, 9000),             # t0 = a > b
        ('GOTOF', 9000, None, 8),            # if not t0, jump to quad 8
        ('print_str', 12000, None, None),    # print "a is greater to b"
        ('print_newline', None, None, None),
        ('GOTO', None, None, 10),             # jump to quad 10
        ('print_str', 12001, None, None),    # print "a is not greater to b"
        ('print_newline', None, None, None),
        ('END', None, None, None)             # End of program
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
    0: ('GOTO', None, None, 1)          # Initial GOTO to 'inicio' block
    1: ('=', 10000, None, 1000)        # i = 1 (constant 1 at address 10000 to 'i' at 1000)
    2: ('<', 1000, 10001, 9000)        # t0 = i < 3 (constant 3 at address 10001)
    3: ('GOTOF', 9000, None, 9)        # if not t0, jump to quad 9 (END)
    4: ('print', 1000, None, None),    # print i
    5: ('print_newline', None, None, None),
    6: ('+', 1000, 10000, 7000),       # t1 = i + 1 (constant 1 at 10000)
    7: ('=', 7000, None, 1000),        # i = t1
    8: ('GOTO', None, None, 2),         # jump back to quad 2
    9: ('END', None, None, None)        # End of program
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
        ('GOTO', None, None, 1),         # Initial GOTO to 'inicio' block
        ('=', 10000, None, 1000),        # i = 1
        ('<', 1000, 10001, 9000),        # t0 = i < 3
        ('GOTOF', 9000, None, 9),        # if not t0, jump to quad 9
        ('print', 1000, None, None),     # print i
        ('print_newline', None, None, None),
        ('+', 1000, 10000, 7000),        # t1 = i + 1
        ('=', 7000, None, 1000),         # i = t1
        ('GOTO', None, None, 2),          # jump back to quad 2
        ('END', None, None, None)         # End of program
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
    0: ('GOTO', None, None, 1)          # Initial GOTO to 'inicio' block
    1: ('=', 10000, None, 1000)        # n = 5 (constant 5 at address 10000 to 'n' at 1000)
    2: ('=', 10001, None, 1001)        # result = 1 (constant 1 at address 10001 to 'result' at 1001)
    3: ('>', 1000, 10001, 9000)        # t0 = n > 1
    4: ('GOTOF', 9000, None, 13),       # if not t0, jump to quad 13 (END)
    5: ('*', 1001, 1000, 7000),         # t1 = result * n
    6: ('=', 7000, None, 1001),         # result = t1
    7: ('-', 1000, 10001, 7001),        # t2 = n - 1
    8: ('=', 7001, None, 1000),         # n = t2
    9: ('GOTO', None, None, 3),          # jump back to quad 3
    10: ('print_str', 12000, None, None),# print "Factorial is:" (string at 12000)
    11: ('print', 1001, None, None),     # print result
    12: ('print_newline', None, None, None),
    13: ('END', None, None, None)        # End of program
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
        ('GOTO', None, None, 1),             # Initial GOTO to 'inicio' block
        ('=', 10000, None, 1000),            # n = 5
        ('=', 10001, None, 1001),            # result = 1
        ('>', 1000, 10001, 9000),            # t0 = n > 1
        ('GOTOF', 9000, None, 10),           # if not t0, jump to quad 13
        ('*', 1001, 1000, 7000),             # t1 = result * n
        ('=', 7000, None, 1001),             # result = t1
        ('-', 1000, 10001, 7001),            # t2 = n - 1
        ('=', 7001, None, 1000),             # n = t2
        ('GOTO', None, None, 3),             # jump back to quad 3
        ('print_str', 12000, None, None),     # print "Factorial is:"
        ('print', 1001, None, None),          # print result
        ('print_newline', None, None, None),
        ('END', None, None, None)             # End of program
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
    0: ('GOTO', None, None, 1)           # Initial GOTO to 'inicio' block
    1: ('=', 10000, None, 1000)          # a = 2 (constant 2 at address 10000 to 'a' at 1000)
    2: ('=', 10001, None, 1001)          # b = 3 (constant 3 at address 10001 to 'b' at 1001)
    3: ('print_str', 12000, None, None), # print "Hello, World!" (string at 12000)
    4: ('print_newline', None, None, None),
    5: ('+', 1000, 1001, 7000),           # t0 = a + b
    6: ('print', 7000, None, None),       # print t0
    7: ('print_newline', None, None, None),
    8: ('END', None, None, None)          # End of program
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
        ('GOTO', None, None, 1),             # Initial GOTO to 'inicio' block
        ('=', 10000, None, 1000),            # a = 2
        ('=', 10001, None, 1001),            # b = 3
        ('print_str', 12000, None, None),    # print "Hello, World!"
        ('print_newline', None, None, None),
        ('+', 1000, 1001, 7000),             # t0 = a + b
        ('print', 7000, None, None),         # print t0
        ('print_newline', None, None, None),
        ('END', None, None, None)            # End of program
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
