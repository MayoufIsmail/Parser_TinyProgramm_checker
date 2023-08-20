grammar TinyGrammar;

program: declarationList;

declarationList: declaration declarationList | ;

declaration: variableDeclaration
            | functionDeclaration;

variableDeclaration: dataType identifierList ';' ;

dataType: 'int' | 'float' | 'char' | 'bool';

identifierList: IDENTIFIER (',' IDENTIFIER)*;

functionDeclaration: dataType IDENTIFIER '(' parameterList ')' compoundStmt;

parameterList: parameter (',' parameter)* | ;

parameter: dataType IDENTIFIER;

compoundStmt: '{' localDeclarations statementList '}';

localDeclarations: localDeclarations variableDeclaration | ;

statementList: statementList statement | ;

statement: expressionStmt
         | compoundStmt
         | selectionStmt
         | iterationStmt
         | returnStmt;

expressionStmt: expression ';' ;

selectionStmt: 'if' '(' expression ')' statement ('else' statement)?;

iterationStmt: 'while' '(' expression ')' statement;

returnStmt: 'return' expression? ';';

expression: variable '=' expression
          | simpleExpression;

variable: IDENTIFIER
        | IDENTIFIER '[' additiveExpression ']';

simpleExpression: additiveExpression (relationalOperator additiveExpression)?;

additiveExpression: additiveExpression '+' term
                  | additiveExpression '-' term
                  | term;

term: term '*' factor
    | term '/' factor
    | term '%' factor
    | factor;

factor: '(' expression ')'
      | variable
      | call
      | NUMBER
      | BOOLEAN
      | CHAR_LITERAL
      | 'true'
      | 'false';

call: IDENTIFIER '(' args ')';

args: expression (',' expression)* | ;

relationalOperator: '<' | '>' | '<=' | '>=' | '==' | '!=';

IDENTIFIER: [a-zA-Z][a-zA-Z0-9]*;
NUMBER: '0' | [1-9][0-9]*;
BOOLEAN: 'true' | 'false';
CHAR_LITERAL: '\'' . '\'';
WS: [ \t\r\n]+ -> skip;
