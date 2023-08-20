from lark import Lark, Transformer, v_args

# Define the EBNF grammar for Tiny
grammar = """
    Tiny ::= "int main()" "{" declarations statements "}"
          | "int sum()" "{" declarations statements "}"
          | "int" "(" identifier ")" "{" declarations statements "}"

    declarations ::= "{" declaration "}"

    declaration ::= type identifier ("," identifier)* ";"

    type ::= "int" | "float" | "char" | "bool"

    identifier: /[a-zA-Z][a-zA-Z0-9]*/

    statements ::= "{" statement "}"

    statement ::= assignment
              | if_statement
              | while_loop

    assignment ::= identifier "=" expression ";"

    if_statement ::= "if" "(" expression ")" "{" statements "}" [ "else" "{" statements "}" ]

    while_loop ::= "while" "(" expression ")" "{" statements "}"

    expression ::= term ( add_op term )*

    term ::= factor ( mul_op factor )*

    factor ::= identifier
           | constant
           | "(" expression ")"

    add_op ::= "+" | "-"

    mul_op ::= "*" | "/"

    constant ::= integer
             | float_num
             | char_literal
             | bool_literal

    integer: /[0-9]+/

    float_num: /[0-9]+\.[0-9]+/

    char_literal: /'.'/ 

    bool_literal ::= "true" | "false"
"""



# Create a Lark parser using the provided grammar
parser = Lark(grammar, start='Tiny', parser='earley')

@v_args(inline=True)
class TinyTransformer(Transformer):
    def __init__(self):
        self.variables = set()

    def declarations(self, *args):
        for declaration in args:
            self.variables.update(declaration)

    def declaration(self, type_, *identifiers):
        return identifiers

    def identifier(self, name):
        return name.value

    # Add other transformation methods for different grammar rules here


# Function to validate a program using the parser and transformer
def validate_program(program):
    try:
        tree = parser.parse(program)
        transformer = TinyTransformer()
        transformer.transform(tree)
        return True, None
    except Exception as e:
        return False, str(e)


# Test programs
valid_program = """
int main() {
    int x, y;
    x = 10;
    y = x + 5;
}
"""

invalid_program = """
int sum() {
    int x, y;
    x = 10;
    y = x + ;
}
"""

# Test the validation function
valid, error_msg = validate_program(valid_program)
if valid:
    print("Valid program.")
else:
    print("Invalid program:", error_msg)

valid, error_msg = validate_program(invalid_program)
if valid:
    print("Valid program.")
else:
    print("Invalid program:", error_msg)
