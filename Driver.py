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

    input_file = argv[1]
    input_stream = FileStream(input_file)

    lexer = little_duckLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = little_duckParser(stream)
    tree = parser.programa()

    # Initialize the custom listener with traversal printing enabled
    listener = LittleDuckCustomListener(print_traversal=False)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Retrieve the quadruples and virtual memory
    quadruples = listener.quadruple_manager.quadruples
    virtual_memory = listener.virtual_memory
    function_table = listener.function_table

    # Initialize and run the virtual machine
    vm = VirtualMachine(quadruples, virtual_memory, function_table, print_traversal=False)
    vm.run()

if __name__ == '__main__':
    main(sys.argv)