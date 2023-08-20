from antlr4.error.ErrorListener import ErrorListener


class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ValueError(f"Syntax error at line {line}, column {column}: {msg}")
