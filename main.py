from antlr4 import InputStream, CommonTokenStream
from TinyGrammarLexer import TinyGrammarLexer
from TinyGrammarParser import TinyGrammarParser
from CustomErrorListener import CustomErrorListener

def validate_code(input_code):
    input_stream = InputStream(input_code)
    lexer = TinyGrammarLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = TinyGrammarParser(tokens)

    # Attach the custom error listener to the parser
    parser.removeErrorListeners()
    custom_error_listener = CustomErrorListener()
    parser.addErrorListener(custom_error_listener)

    try:
        tree = parser.program()  # Use the appropriate starting rule
        return True  # The program is valid
    except ValueError as e:
        return False  # The program is invalid

if __name__ == '__main__':
    input_code = """
int main () {
    int x;
    char y;
    x = 10;
    y = 'A';
    x = x + y;  // Error: Adding int and char
    return 0;
}


    """

    is_valid = validate_code(input_code)
    if is_valid:
        print("Input program is valid.")
    else:
        print("Input program is invalid.")
