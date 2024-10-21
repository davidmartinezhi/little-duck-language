"""
This script is a driver for parsing Little Duck language using ANTLR4.
It takes an input file as a command-line argument, tokenizes it with a lexer, parses it using the Little Duck parser, and prints the parse tree.
"""

import sys
from antlr4 import *  # Importing ANTLR4 runtime library
from generated.little_duckLexer import (
    little_duckLexer,
)  # Importing the generated lexer for Little Duck language
from generated.little_duckParser import (
    little_duckParser,
)  # Importing the generated parser for Little Duck language


def main(argv):
    """
    Main function that handles the input stream, tokenizes it, parses it, and prints the parse tree.

    Args:
        argv (list): List of command-line arguments. The first argument (argv[1]) should be the path to the input file.
    """

    # Load the input file provided as a command-line argument and create an input stream
    input_stream = FileStream(argv[1])

    # Initialize the lexer with the input stream (breaks the input into tokens)
    lexer = little_duckLexer(input_stream)  # Converts input text into tokens

    # Create a stream of tokens from the lexer output
    stream = CommonTokenStream(
        lexer
    )  # Wraps the lexer output into a token stream for the parser

    # Initialize the parser with the token stream (uses the tokens to create a parse tree)
    parser = little_duckParser(stream)  # Instance of parser

    # Start parsing the input according to the grammar rule 'programa' (the entry point of the grammar)
    tree = parser.programa()  # 'programa' (initial symbol of grammar) method is called

    # Print the parse tree in string format
    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    # Call the main function with the command-line arguments
    main(sys.argv)  # python3 Driver.py test_program.txt
