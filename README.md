# Project Title: Programming Paradigm Project Task

## Introduction

This work contains my work of EBNF Grammar and Parser for the project Tiny. The parser has been implement with ANTLR4 (https://github.com/antlr/antlr4/blob/master/doc/python-target.md) library and with [Python 3.11.2]. However, I have implement a main.py page that  contain all classes and use external textfile to check the first task (Valid/Invalid).

## Project Components:
There are several items of this project for EBNF Grammar and also to implement the parser:
- EBNF grammar TinyGrammar.PDF (for the first task!)
- Parser: implement the tokens and lexer and parser:
    - main.py
    - ANTLR4 sources:
        - TinyGrammar.interp
        - TinyGrammar.tokens
        - TinyGrammarListener.py
        - TinyGrammarParser.py
        - TinyGrammarLexer.interp
        - TinyGrammarLexer.py
        - TinyGrammarLexer.tokens
        - antlr-4.13.0-complete.jar
        - TinyGrammar.g4
    - Tiny_sample_code.txt (is where to write a test code to check      valid or invalid)
    - CustomErrorListener.py
- Static Type System: 
    - ASTGenerator.py
    - Interpreter.py

# Prerequisites:
- Python 3.8 minimum
- Install ANTLR4 for Python3 **(((VERY IMPORTANT!!!)))**
```bash
pip install antlr4-python3-runtime
```

# How to run the code: 
There is 2 ways to run the code:

### 1.  Using the CMD from Local Project File:

 - Please find the (./Tiny_sample_code.txt) to write the code for testing and save it
 - Open the Command Line from project folder <path_to_file> like: ..\ProgParadigms_Ismail_Mayouf:

```
py main.py
```

### 2. Docker: There are two ways for this:
   
  #### 2.1 Build a docker on local file: using below commands

- Open a command line from the folder:

+ build a docker image[I did already!]:

```
docker build -t tiny-interpreter .
```

+ run docker image
```
docker run -it tiny-interpreter
```

For further testing, Please find the <./Tiny_sample_code.txt> to add and adjust the testing code [save it] and repeat the same above commands (build & run)

  #### 2.2 Find the repo on docker-hub:

- The registry URL [https://hub.docker.com/]
- My username: ismail23
- the image name and tag: <ismail23/tiny-interpreter:latest>


### Evaluation
You can use  <./Tiny_sample_code.txt> for checking the expected ouput and by doing using either running from folder or docker as explained above.

### Explain my work & DEsign decision: 

After creating the EBNF grammar {EBNF grammar TinyGrammar.PDF} . I have created another TinyGrammar.g4 that is compitable to ANTLR4, after this step I have created a (CustomErrorListener.py) which a custom to define a error listener for ANTLR framework and overrides all error-handling, this is important for main.py. 

Furthermore, the main.py contains if all dependencies of ANTLR4 and Custom Error Listener and External Tiny_simple_code for testing.

For the second Task I have tried to create ASTGenerator and Symbol_table.py for building a static system but It doesn't detect the Integer Overflows.

## Task 1

### 1.1 The EBNF grammar is presented in the PDF file, and below are description for some symbols used on it:

 * <> :: non-terminal 
 * () :: for a list of alternatives to be picked
 * {} :: for a series of zero or more occurrences
 * [] :: for an optional sequence; pick one or none
 * `` :: Terminal

 I have used a <character> for letters. And I added <localdections> to use local <something>.

## 1.2 Parser: 

To test the parser, please find the  ./Tiny_sample_code.txt to insert the testing code, then you can use both ways explain before to execute the code. Expected Outputs : Input program is valid OR Input code is Invalid.

Note: You can generate the parser again if needed using below command: 
```
antlr4 TinyGrammar.g4
```

## Task 2

- I have created a ASTGenerator for static system to detect integer overflow. 
- I have written an Interpreter methods that travers and evaluate nodes of the AST generated from ASTGenerator.py to pass it to main.py
- I have extended main.py code to detect and present the expected output for BufferOverflows [but Unfortunality is didn't detect any of overflows].
