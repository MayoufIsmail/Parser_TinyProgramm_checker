import ply.lex as lex
import ply.yacc as yacc
from ast_nodes import ProgramNode, FunctionNode

# List of token names
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'EXPONENT',
    'ASSIGN',
    'EQ',
    'NEQ',
    'LT',
    'LTE',
    'GT',
    'GTE',
    'AND',
    'OR',
    'NOT',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'SEMICOLON',
    'COMMA',
    'COLON',
    'DOT',
    'STRING_LITERAL',
    'COMMENT',
    'NEWLINE',
    'IF',
    'ELSE',
    'WHILE',
    'FOR',
    'FUNCTION',
    'RETURN',
    'INT',
    'FLOAT',
    'CHAR',
    'BOOL',
    'BOOLEAN',
    'MAIN',
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_EXPONENT = r'\*\*'
t_ASSIGN = r'='
t_EQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','
t_COLON = r':'
t_DOT = r'\.'
t_STRING_LITERAL = r'\"([^\\\n]|(\\.))*?\"'
t_COMMENT = r'//.*'
t_NEWLINE = r'\n'


# A regular expression rule with some action code
def t_main_function(t):
    'main_function : INT_MAIN'

def t_identifier(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT_LITERAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_CHAR_LITERAL(t):
    r'\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]  # Remove single quotes
    return t


def t_INT_LITERAL(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


# Ignored characters (whitespace and tabs)
t_ignore = ' \t'


# Define a rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Reserved words
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'function': 'FUNCTION',
    'return': 'RETURN',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'bool': 'BOOL',
    'true': 'BOOLEAN',
    'false': 'BOOLEAN',
}

# Build the lexer
lexer = lex.lex()


# Parsing rules...
def p_program(p):
    '''program : functions INT_MAIN function_body
               | INT_MAIN function_body'''
    if len(p) == 4:
        p[0] = ProgramNode(p.lineno(1), p[1], p[3])
    elif len(p) == 3:
        p[0] = ProgramNode(p.lineno(1), [], p[2])


def p_functions(p):
    '''functions : functions function
                 | empty'''
    if p[1] is None:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]


def p_function(p):
    '''function : type IDENTIFIER LPAREN parameters RPAREN function_body'''
    p[0] = FunctionNode(p.lineno(1), p[1], p[2], p[4], p[6])


def p_parameters(p):
    '''parameters : multiple_parameters
                  | single_parameter
                  | empty'''
    if p[1] is None:
        p[0] = []
    else:
        p[0] = p[1]


def p_multiple_parameters(p):
    '''multiple_parameters : multiple_parameters COMMA single_parameter
                          | single_parameter'''
    p[0] = p[1] + [p[3]] if len(p) == 4 else [p[1]]


def p_single_parameter(p):
    '''single_parameter : type IDENTIFIER'''
    # Create a ParameterNode object and store it in p[0]
    p[0] = ParameterNode(p.lineno(1), p[1], p[2])

# Define other parsing rules similarly

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | LPAREN expression RPAREN
                  | NUMBER'''
    pass


def p_statement(p):
    '''statement : SEMICOLON
                 | block
                 | assignment
                 | if
                 | while'''
    p[0] = [p[1]] if p.slice[1].type != 'SEMICOLON' else None


# Define other parsing rules similarly

def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()


# Tokenization
lexer.input('sample_program.txt')
for token in lexer:
    print(token)

# Sample input expression...
sample_expression = "3 + 4 * (2 - 1)"

# Parse the sample expression...
expression_result = parser.parse(sample_expression)
print("Expression parsing completed successfully. Result:", expression_result)

with open('sample_program.txt', 'r') as file:
    sample_program = file.read()

parsed_result = parser.parse(sample_program)
print("Parsing completed successfully!")
# Parse the sample program...
program_result = parser.parse(sample_program)
print("Program parsing completed successfully.")
