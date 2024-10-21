"""
Test suite for the Little Duck language parser.

This module contains tests for the ANTLR-generated parser of the Little Duck language.
It verifies that the parser correctly accepts valid code and rejects invalid code according
to the language grammar.
"""

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from generated.little_duckLexer import little_duckLexer
from generated.little_duckParser import little_duckParser


class SyntaxErrorListener(ErrorListener):
    """
    Custom error listener to capture syntax errors during parsing.
    ErrorListener is inherited from the ErrorListener base class.
    """

    def __init__(self):
        super(
            SyntaxErrorListener, self
        ).__init__()  # Calls constructor of the base class
        self.syntax_errors = []  # Store syntax errors that appear in the analysis

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Called automatically when a syntax error is encountered in the parser.

        Args:
            recognizer: The parser instance.
            offendingSymbol: The offending token (Token that raised the syntax error).
            line (int): Line number where the error occurred.
            column (int): Column number where the error occurred.
            msg (str): The error message.
            e: The exception.
        """
        error_message = f"Syntax error at line {line}, column {column}: {msg}"
        self.syntax_errors.append(error_message)


def parse_input(input_text):
    """
    Helper function to parse input text and return the parse tree.

    Args:
        input_text (str): The Little Duck language code to parse.

    Returns:
        ParseTree: The root of the parse tree.

    Raises:
        Exception: If syntax errors are encountered during parsing.
    """
    input_stream = InputStream(input_text)  # Input that will by used by lexer
    lexer = little_duckLexer(input_stream)  # Converts input text into tokens

    # Attach custom error listener to the lexer
    lexer_error_listener = SyntaxErrorListener()  # Create instance of error listener
    lexer.removeErrorListeners()  # Remove default listener
    lexer.addErrorListener(lexer_error_listener)  # Add the new listener

    token_stream = CommonTokenStream(lexer)  # Wraps lexer, to be consumed by parser
    parser = little_duckParser(token_stream)  # Instance of parser

    # Attach custom error listener to the parser
    parser_error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_error_listener)

    # Attempt to parse the input
    tree = parser.programa()  # 'programa' (initial symbol of grammar) method is called

    # Collect syntax errors from both lexer and parser
    syntax_errors = (
        lexer_error_listener.syntax_errors + parser_error_listener.syntax_errors
    )

    # Check for syntax errors
    if syntax_errors:  # If we have errors
        raise Exception(
            "\n".join(syntax_errors)
        )  # Raises exception with all errors concatenated

    return tree  # return tree of syntactic analysis


# Test functions


def test_variable_declarations():
    """Test parsing of variable declarations."""
    input_text = """
    programa test;
    vars {
        x: entero;
        y, z: flotante;
    }
    inicio {
    escribe("Variables declared successfully");
    }
    fin
    """
    try:
        tree = parse_input(input_text)
        assert tree is not None, "Parsing failed: tree is None"
    except Exception as e:
        assert False, f"Parsing failed with exception: {e}"


def test_assignment_statements():
    """Test parsing of assignment statements."""
    input_text = """
    programa test;
    vars {
        x, y: entero;
    }
    inicio {
        x = 10;
        y = x + 5;
        escribe("Variables assigned successfully");
    }
    fin
    """
    try:
        tree = parse_input(input_text)
        assert tree is not None, "Parsing failed: tree is None"
    except Exception as e:
        assert False, f"Parsing failed with exception: {e}"


def test_arithmetic_expressions():
    """Test parsing of arithmetic expressions."""
    input_text = """
    programa test;
    vars {
        x, y, z: entero;
    }
    inicio {
        z = x + y * 2;
        z = (x + y) * 2;
    }
    fin
    """
    try:
        tree = parse_input(input_text)
        assert tree is not None, "Parsing failed: tree is None"
    except Exception as e:
        assert False, f"Parsing failed with exception: {e}"


def test_conditional_statements():
    """Test parsing of conditional statements with and without 'sino'."""
    input_text = """
    programa test;
    vars {
        x, y: entero;
    }
    inicio {
        si (x > y) haz {
            escribe(x);
        } sino haz {
            escribe(y);
        }
        si (x == y) haz {
            escribe("x is equal to y");
        }
    }
    fin
    """
    try:
        tree = parse_input(input_text)
        assert tree is not None, "Parsing failed: tree is None"
    except Exception as e:
        assert False, f"Parsing failed with exception: {e}"


def test_loop_statements():
    """Test parsing of loop statements."""
    input_text = """
    programa test;
    vars {
        x: entero;
    }
    inicio {
        mientras (x < 10) haz {
            x = x + 1;
        }
    }
    fin
    """
    try:
        tree = parse_input(input_text)
        assert tree is not None, "Parsing failed: tree is None"
    except Exception as e:
        assert False, f"Parsing failed with exception: {e}"


def test_function_calls():
    """Test parsing of function calls without 'retorno' in functions."""
    input_text = """
    programa test;
    vars {
        z: entero;
    }
    func suma(a: entero, b: entero) {
        x = a + b;
        escribe(x);
    }
    inicio {
        suma(5, 10);
    }
    fin
    """
    try:
        tree = parse_input(input_text)
        assert tree is not None, "Parsing failed: tree is None"
    except Exception as e:
        assert False, f"Parsing failed with exception: {e}"


def test_full_program():
    """Test parsing of a comprehensive program combining multiple constructs."""
    input_text = """
    programa test;
    vars {
        x, y: entero;
        z: flotante;
    }
    func suma(a: entero, b: entero) {
        x = a + b;
        escribe(x);
    }
    inicio {
        x = 10;
        y = 20;
        suma(x, y);
        z = x * 1.5;
        si (z > 50) haz {
            escribe("z es mayor que 50");
        } sino haz {
            escribe("z es menor o igual a 50");
        }
        mientras (x < y) haz {
            x = x + 1;
        }
    }
    fin
    """
    try:
        tree = parse_input(input_text)
        assert tree is not None, "Parsing failed: tree is None"
    except Exception as e:
        assert False, f"Parsing failed with exception: {e}"


def test_syntax_error_missing_semicolon():
    """Test parsing with a missing semicolon to ensure syntax errors are caught."""
    input_text = """
    programa test;
    vars {
        x: entero
    }
    inicio {
        x = 10
    }
    fin
    """
    try:
        tree = parse_input(input_text)
        assert (
            False
        ), "Parsing succeeded but was expected to fail due to missing semicolons."
    except Exception as e:
        error_message = str(e)
        assert (
            "missing ';'" in error_message or "mismatched input" in error_message
        ), f"Unexpected error message: {e}"


def test_invalid_identifier():
    """Test parsing with an invalid identifier to check lexer errors."""
    input_text = """
    programa test;
    vars {
        1x: entero;
    }
    inicio {
    }
    fin
    """
    try:
        tree = parse_input(input_text)
        assert (
            False
        ), "Parsing succeeded but was expected to fail due to invalid identifier."
    except Exception as e:
        error_message = str(e)
        assert (
            "token recognition error" in error_message
            or "extraneous input" in error_message
        ), f"Unexpected error message: {e}"


def test_unexpected_token():
    """Test parsing with an unexpected token to ensure error handling."""
    input_text = """
    programa test;
    vars {
        x: entero;
    }
    inicio {
        x = @10;
    }
    fin
    """
    try:
        tree = parse_input(input_text)
        assert (
            False
        ), "Parsing succeeded but was expected to fail due to unexpected token."
    except Exception as e:
        error_message = str(e)
        assert (
            "token recognition error" in error_message
            or "no viable alternative" in error_message
        ), f"Unexpected error message: {e}"


if __name__ == "__main__":
    # List of test functions to run
    tests = [
        test_variable_declarations,
        test_assignment_statements,
        test_arithmetic_expressions,
        test_conditional_statements,
        test_loop_statements,
        test_function_calls,
        test_full_program,
        test_syntax_error_missing_semicolon,
        test_invalid_identifier,
        test_unexpected_token,
    ]

    # Run each test function and report the result
    for test in tests:
        try:
            test()
            print(f"{test.__name__}: PASSED")
        except AssertionError as e:
            print(f"{test.__name__}: FAILED")
            print(f"AssertionError: {e}")
        except Exception as e:
            print(f"{test.__name__}: FAILED with exception")
            print(f"Exception: {e}")
