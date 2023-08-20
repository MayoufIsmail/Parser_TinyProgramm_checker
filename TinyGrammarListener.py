# Generated from TinyGrammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .TinyGrammarParser import TinyGrammarParser
else:
    from TinyGrammarParser import TinyGrammarParser

# This class defines a complete listener for a parse tree produced by TinyGrammarParser.
class TinyGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by TinyGrammarParser#program.
    def enterProgram(self, ctx:TinyGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#program.
    def exitProgram(self, ctx:TinyGrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#declarationList.
    def enterDeclarationList(self, ctx:TinyGrammarParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#declarationList.
    def exitDeclarationList(self, ctx:TinyGrammarParser.DeclarationListContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#declaration.
    def enterDeclaration(self, ctx:TinyGrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#declaration.
    def exitDeclaration(self, ctx:TinyGrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:TinyGrammarParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:TinyGrammarParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#dataType.
    def enterDataType(self, ctx:TinyGrammarParser.DataTypeContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#dataType.
    def exitDataType(self, ctx:TinyGrammarParser.DataTypeContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#identifierList.
    def enterIdentifierList(self, ctx:TinyGrammarParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#identifierList.
    def exitIdentifierList(self, ctx:TinyGrammarParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:TinyGrammarParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:TinyGrammarParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#parameterList.
    def enterParameterList(self, ctx:TinyGrammarParser.ParameterListContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#parameterList.
    def exitParameterList(self, ctx:TinyGrammarParser.ParameterListContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#parameter.
    def enterParameter(self, ctx:TinyGrammarParser.ParameterContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#parameter.
    def exitParameter(self, ctx:TinyGrammarParser.ParameterContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#compoundStmt.
    def enterCompoundStmt(self, ctx:TinyGrammarParser.CompoundStmtContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#compoundStmt.
    def exitCompoundStmt(self, ctx:TinyGrammarParser.CompoundStmtContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#localDeclarations.
    def enterLocalDeclarations(self, ctx:TinyGrammarParser.LocalDeclarationsContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#localDeclarations.
    def exitLocalDeclarations(self, ctx:TinyGrammarParser.LocalDeclarationsContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#statementList.
    def enterStatementList(self, ctx:TinyGrammarParser.StatementListContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#statementList.
    def exitStatementList(self, ctx:TinyGrammarParser.StatementListContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#statement.
    def enterStatement(self, ctx:TinyGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#statement.
    def exitStatement(self, ctx:TinyGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#expressionStmt.
    def enterExpressionStmt(self, ctx:TinyGrammarParser.ExpressionStmtContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#expressionStmt.
    def exitExpressionStmt(self, ctx:TinyGrammarParser.ExpressionStmtContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#selectionStmt.
    def enterSelectionStmt(self, ctx:TinyGrammarParser.SelectionStmtContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#selectionStmt.
    def exitSelectionStmt(self, ctx:TinyGrammarParser.SelectionStmtContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#iterationStmt.
    def enterIterationStmt(self, ctx:TinyGrammarParser.IterationStmtContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#iterationStmt.
    def exitIterationStmt(self, ctx:TinyGrammarParser.IterationStmtContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#returnStmt.
    def enterReturnStmt(self, ctx:TinyGrammarParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#returnStmt.
    def exitReturnStmt(self, ctx:TinyGrammarParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#expression.
    def enterExpression(self, ctx:TinyGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#expression.
    def exitExpression(self, ctx:TinyGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#variable.
    def enterVariable(self, ctx:TinyGrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#variable.
    def exitVariable(self, ctx:TinyGrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#simpleExpression.
    def enterSimpleExpression(self, ctx:TinyGrammarParser.SimpleExpressionContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#simpleExpression.
    def exitSimpleExpression(self, ctx:TinyGrammarParser.SimpleExpressionContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:TinyGrammarParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:TinyGrammarParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#term.
    def enterTerm(self, ctx:TinyGrammarParser.TermContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#term.
    def exitTerm(self, ctx:TinyGrammarParser.TermContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#factor.
    def enterFactor(self, ctx:TinyGrammarParser.FactorContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#factor.
    def exitFactor(self, ctx:TinyGrammarParser.FactorContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#call.
    def enterCall(self, ctx:TinyGrammarParser.CallContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#call.
    def exitCall(self, ctx:TinyGrammarParser.CallContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#args.
    def enterArgs(self, ctx:TinyGrammarParser.ArgsContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#args.
    def exitArgs(self, ctx:TinyGrammarParser.ArgsContext):
        pass


    # Enter a parse tree produced by TinyGrammarParser#relationalOperator.
    def enterRelationalOperator(self, ctx:TinyGrammarParser.RelationalOperatorContext):
        pass

    # Exit a parse tree produced by TinyGrammarParser#relationalOperator.
    def exitRelationalOperator(self, ctx:TinyGrammarParser.RelationalOperatorContext):
        pass



del TinyGrammarParser