"""
This script is a driver for parsing the Little Duck language using ANTLR4.
It takes an input file as a command-line argument, tokenizes it with a lexer,
parses it using the Little Duck parser, and performs semantic analysis using a custom listener.
After parsing, it retrieves the generated quadruples and virtual memory,
and runs the virtual machine to execute the program.
"""

import sys
from antlr4 import *
from generated.little_duckLexer import little_duckLexer  # Generated lexer for Little Duck language
from generated.little_duckParser import little_duckParser  # Generated parser for Little Duck language
from src.custom_listener import LittleDuckCustomListener  # Importing the custom listener for semantic analysis
from semantics.virtual_machine import VirtualMachine  # Importing the VirtualMachine class


def main(argv):
    """
    Main function that handles the input stream, tokenizes it, parses it,
    performs semantic analysis using the custom listener, and runs the virtual machine.

    Args:
        argv (list): List of command-line arguments.
                     The first argument (argv[1]) should be the path to the input file.
    """
    if len(argv) < 2:
        print("Usage: python3 driver.py <input_file>")
        sys.exit(1)

    # Load the input file provided as a command-line argument and create an input stream
    input_file = argv[1]
    input_stream = FileStream(input_file)

    # Initialize the lexer with the input stream (breaks the input into tokens)
    lexer = little_duckLexer(input_stream)  # Converts input text into tokens

    # Create a stream of tokens from the lexer output
    token_stream = CommonTokenStream(lexer)  # Wraps the lexer output into a token stream for the parser

    # Initialize the parser with the token stream (uses the tokens to create a parse tree)
    parser = little_duckParser(token_stream)  # Instance of the parser

    # Add error handling (optional)
    parser.removeErrorListeners()
    parser.addErrorListener(DiagnosticErrorListener())

    # Start parsing the input according to the grammar rule 'programa' (the entry point of the grammar)
    tree = parser.programa()  # 'programa' is the initial symbol of the grammar

    # Initialize the custom listener for semantic analysis
    listener = LittleDuckCustomListener(print_traversal=False)  # Set print_traversal to True to print the traversal

    # Walk the parse tree with the custom listener to perform semantic actions
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # After parsing and semantic analysis, retrieve the quadruples and virtual memory
    quadruples = listener.quadruple_manager.quadruples
    virtual_memory = listener.virtual_memory

    # Print the generated quadruples
    # print("\nGenerated Quadruples:")
    # for idx, quad in enumerate(quadruples):
    #     print(f"{idx}: {quad}")

    # # Print the memory state before execution
    # print("\nMemory State Before Execution:")
    # virtual_memory.print_memory()
    # print("\nRunning program:")
    # Initialize and run the virtual machine
    vm = VirtualMachine(quadruples, virtual_memory)
    vm.run()



if __name__ == "__main__":
    # Call the main function with the command-line arguments
    main(sys.argv)  # Usage: python3 driver.py test_program.ld
