# Little Duck Language Compiler

![Python](https://img.shields.io/badge/Python-3.13-blue)
![ANTLR4](https://img.shields.io/badge/ANTLR4-4.9.2-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen)

**Little Duck** is a simple programming language designed to reinforce basic concepts of lexical, syntactic and semantic analysis. This project implements a compiler using `ANTLR4` and Python 3.13, covering lexical, syntactic and semantic analysis phases.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [Contributions](#contributions)
- [License](#license)

## Description

The **Little Duck** compiler processes code written in the Little Duck language and analyzes it in two main phases:

1. **Lexical Analysis:** Identifies valid tokens such as keywords, identifiers, operators, and numbers.
2. **Syntactic Analysis:** Ensures that the structure of the code follows the grammar rules.

This project is part of an academic exercise aimed at learning how compilers function at a fundamental level, using ANTLR4 to generate the lexer and parser and Python 3.13 to manage the compilation process.

## Requirements

- Python 3.13
- ANTLR4 4.9.2

## Installation

First, clone this repository to your local machine:

```bash
git clone https://github.com/your_user/little_duck_language_compiler.git
cd little_duck_language_compiler
