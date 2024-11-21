"""
This script is a driver for parsing the Little Duck language using ANTLR4.
It takes an input file as a command-line argument, tokenizes it with a lexer,
parses it using the Little Duck parser, and performs semantic analysis using a custom listener.
After parsing, it retrieves the generated quadruples and virtual memory,
and runs the virtual machine to execute the program.
"""

import sys
from antlr4 import *
from generated.little_duckLexer import (
    little_duckLexer,
)  # Generated lexer for Little Duck language
from generated.little_duckParser import (
    little_duckParser,
)  # Generated parser for Little Duck language
from src.custom_listener import (
    LittleDuckCustomListener,
)  # Importing the custom listener for semantic analysis
from src.custom_error_listener import (
    LittleDuckErrorListener,
)  # Importing the custom error listener
from semantics.virtual_machine import (
    VirtualMachine,
)  # Importing the VirtualMachine class



def main(argv):
    if len(argv) != 2:
        print("Usage: python3 Driver.py <input_file>")
        return

    # Load the input file provided as a command-line argument and create an input stream
    input_file = argv[1]
    input_stream = FileStream(input_file)

    # Initialize the lexer with the input stream (breaks the input into tokens)
    lexer = little_duckLexer(input_stream)

    # Create a stream of tokens from the lexer output
    stream = CommonTokenStream(lexer)

    # Initialize the parser with the token stream (uses the tokens to create a parse tree)
    parser = little_duckParser(stream)

    # Remove default error listeners
    parser.removeErrorListeners()

    # Add the custom error listener
    error_listener = LittleDuckErrorListener()
    parser.addErrorListener(error_listener)

    # Start parsing the input according to the grammar rule 'programa' (the entry point of the grammar)
    tree = parser.programa()

    # Initialize the custom listener with traversal printing enabled
    listener = LittleDuckCustomListener(print_traversal=False)

    # Walk the parse tree with the custom listener to perform semantic actions
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Retrieve the quadruples, virtual memory and function table
    quadruples = listener.quadruple_manager.quadruples
    virtual_memory = listener.virtual_memory
    function_table = listener.function_table

    # Initialize and run the virtual machine
    vm = VirtualMachine(quadruples, virtual_memory, function_table, print_traversal=False)
    vm.run()

if __name__ == '__main__':
    main(sys.argv)