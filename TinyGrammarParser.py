# Generated from TinyGrammar.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,235,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        1,1,1,1,1,1,1,3,1,59,8,1,1,2,1,2,3,2,63,8,2,1,3,1,3,1,3,1,3,1,4,
        1,4,1,5,1,5,1,5,5,5,74,8,5,10,5,12,5,77,9,5,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,7,1,7,1,7,5,7,89,8,7,10,7,12,7,92,9,7,1,7,3,7,95,8,7,1,
        8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,108,8,10,10,10,
        12,10,111,9,10,1,11,1,11,1,11,5,11,116,8,11,10,11,12,11,119,9,11,
        1,12,1,12,1,12,1,12,1,12,3,12,126,8,12,1,13,1,13,1,13,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,3,14,138,8,14,1,15,1,15,1,15,1,15,1,15,
        1,15,1,16,1,16,3,16,148,8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        3,17,157,8,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,165,8,18,1,19,1,
        19,1,19,1,19,3,19,171,8,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,5,20,182,8,20,10,20,12,20,185,9,20,1,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,5,21,199,8,21,10,21,12,21,
        202,9,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        3,22,215,8,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,5,24,225,8,
        24,10,24,12,24,228,9,24,1,24,3,24,231,8,24,1,25,1,25,1,25,0,4,20,
        22,40,42,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,0,2,1,0,2,5,1,0,25,30,238,0,52,1,0,0,0,2,58,
        1,0,0,0,4,62,1,0,0,0,6,64,1,0,0,0,8,68,1,0,0,0,10,70,1,0,0,0,12,
        78,1,0,0,0,14,94,1,0,0,0,16,96,1,0,0,0,18,99,1,0,0,0,20,104,1,0,
        0,0,22,112,1,0,0,0,24,125,1,0,0,0,26,127,1,0,0,0,28,130,1,0,0,0,
        30,139,1,0,0,0,32,145,1,0,0,0,34,156,1,0,0,0,36,164,1,0,0,0,38,166,
        1,0,0,0,40,172,1,0,0,0,42,186,1,0,0,0,44,214,1,0,0,0,46,216,1,0,
        0,0,48,230,1,0,0,0,50,232,1,0,0,0,52,53,3,2,1,0,53,1,1,0,0,0,54,
        55,3,4,2,0,55,56,3,2,1,0,56,59,1,0,0,0,57,59,1,0,0,0,58,54,1,0,0,
        0,58,57,1,0,0,0,59,3,1,0,0,0,60,63,3,6,3,0,61,63,3,12,6,0,62,60,
        1,0,0,0,62,61,1,0,0,0,63,5,1,0,0,0,64,65,3,8,4,0,65,66,3,10,5,0,
        66,67,5,1,0,0,67,7,1,0,0,0,68,69,7,0,0,0,69,9,1,0,0,0,70,75,5,31,
        0,0,71,72,5,6,0,0,72,74,5,31,0,0,73,71,1,0,0,0,74,77,1,0,0,0,75,
        73,1,0,0,0,75,76,1,0,0,0,76,11,1,0,0,0,77,75,1,0,0,0,78,79,3,8,4,
        0,79,80,5,31,0,0,80,81,5,7,0,0,81,82,3,14,7,0,82,83,5,8,0,0,83,84,
        3,18,9,0,84,13,1,0,0,0,85,90,3,16,8,0,86,87,5,6,0,0,87,89,3,16,8,
        0,88,86,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,95,
        1,0,0,0,92,90,1,0,0,0,93,95,1,0,0,0,94,85,1,0,0,0,94,93,1,0,0,0,
        95,15,1,0,0,0,96,97,3,8,4,0,97,98,5,31,0,0,98,17,1,0,0,0,99,100,
        5,9,0,0,100,101,3,20,10,0,101,102,3,22,11,0,102,103,5,10,0,0,103,
        19,1,0,0,0,104,109,6,10,-1,0,105,106,10,2,0,0,106,108,3,6,3,0,107,
        105,1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,
        21,1,0,0,0,111,109,1,0,0,0,112,117,6,11,-1,0,113,114,10,2,0,0,114,
        116,3,24,12,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,
        118,1,0,0,0,118,23,1,0,0,0,119,117,1,0,0,0,120,126,3,26,13,0,121,
        126,3,18,9,0,122,126,3,28,14,0,123,126,3,30,15,0,124,126,3,32,16,
        0,125,120,1,0,0,0,125,121,1,0,0,0,125,122,1,0,0,0,125,123,1,0,0,
        0,125,124,1,0,0,0,126,25,1,0,0,0,127,128,3,34,17,0,128,129,5,1,0,
        0,129,27,1,0,0,0,130,131,5,11,0,0,131,132,5,7,0,0,132,133,3,34,17,
        0,133,134,5,8,0,0,134,137,3,24,12,0,135,136,5,12,0,0,136,138,3,24,
        12,0,137,135,1,0,0,0,137,138,1,0,0,0,138,29,1,0,0,0,139,140,5,13,
        0,0,140,141,5,7,0,0,141,142,3,34,17,0,142,143,5,8,0,0,143,144,3,
        24,12,0,144,31,1,0,0,0,145,147,5,14,0,0,146,148,3,34,17,0,147,146,
        1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,150,5,1,0,0,150,33,1,
        0,0,0,151,152,3,36,18,0,152,153,5,15,0,0,153,154,3,34,17,0,154,157,
        1,0,0,0,155,157,3,38,19,0,156,151,1,0,0,0,156,155,1,0,0,0,157,35,
        1,0,0,0,158,165,5,31,0,0,159,160,5,31,0,0,160,161,5,16,0,0,161,162,
        3,40,20,0,162,163,5,17,0,0,163,165,1,0,0,0,164,158,1,0,0,0,164,159,
        1,0,0,0,165,37,1,0,0,0,166,170,3,40,20,0,167,168,3,50,25,0,168,169,
        3,40,20,0,169,171,1,0,0,0,170,167,1,0,0,0,170,171,1,0,0,0,171,39,
        1,0,0,0,172,173,6,20,-1,0,173,174,3,42,21,0,174,183,1,0,0,0,175,
        176,10,3,0,0,176,177,5,18,0,0,177,182,3,42,21,0,178,179,10,2,0,0,
        179,180,5,19,0,0,180,182,3,42,21,0,181,175,1,0,0,0,181,178,1,0,0,
        0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,0,0,184,41,1,0,0,0,
        185,183,1,0,0,0,186,187,6,21,-1,0,187,188,3,44,22,0,188,200,1,0,
        0,0,189,190,10,4,0,0,190,191,5,20,0,0,191,199,3,44,22,0,192,193,
        10,3,0,0,193,194,5,21,0,0,194,199,3,44,22,0,195,196,10,2,0,0,196,
        197,5,22,0,0,197,199,3,44,22,0,198,189,1,0,0,0,198,192,1,0,0,0,198,
        195,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,0,201,
        43,1,0,0,0,202,200,1,0,0,0,203,204,5,7,0,0,204,205,3,34,17,0,205,
        206,5,8,0,0,206,215,1,0,0,0,207,215,3,36,18,0,208,215,3,46,23,0,
        209,215,5,32,0,0,210,215,5,33,0,0,211,215,5,34,0,0,212,215,5,23,
        0,0,213,215,5,24,0,0,214,203,1,0,0,0,214,207,1,0,0,0,214,208,1,0,
        0,0,214,209,1,0,0,0,214,210,1,0,0,0,214,211,1,0,0,0,214,212,1,0,
        0,0,214,213,1,0,0,0,215,45,1,0,0,0,216,217,5,31,0,0,217,218,5,7,
        0,0,218,219,3,48,24,0,219,220,5,8,0,0,220,47,1,0,0,0,221,226,3,34,
        17,0,222,223,5,6,0,0,223,225,3,34,17,0,224,222,1,0,0,0,225,228,1,
        0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,227,231,1,0,0,0,228,226,1,
        0,0,0,229,231,1,0,0,0,230,221,1,0,0,0,230,229,1,0,0,0,231,49,1,0,
        0,0,232,233,7,1,0,0,233,51,1,0,0,0,20,58,62,75,90,94,109,117,125,
        137,147,156,164,170,181,183,198,200,214,226,230
    ]

class TinyGrammarParser ( Parser ):

    grammarFileName = "TinyGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'int'", "'float'", "'char'", "'bool'", 
                     "','", "'('", "')'", "'{'", "'}'", "'if'", "'else'", 
                     "'while'", "'return'", "'='", "'['", "']'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'true'", "'false'", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "NUMBER", "BOOLEAN", "CHAR_LITERAL", "WS" ]

    RULE_program = 0
    RULE_declarationList = 1
    RULE_declaration = 2
    RULE_variableDeclaration = 3
    RULE_dataType = 4
    RULE_identifierList = 5
    RULE_functionDeclaration = 6
    RULE_parameterList = 7
    RULE_parameter = 8
    RULE_compoundStmt = 9
    RULE_localDeclarations = 10
    RULE_statementList = 11
    RULE_statement = 12
    RULE_expressionStmt = 13
    RULE_selectionStmt = 14
    RULE_iterationStmt = 15
    RULE_returnStmt = 16
    RULE_expression = 17
    RULE_variable = 18
    RULE_simpleExpression = 19
    RULE_additiveExpression = 20
    RULE_term = 21
    RULE_factor = 22
    RULE_call = 23
    RULE_args = 24
    RULE_relationalOperator = 25

    ruleNames =  [ "program", "declarationList", "declaration", "variableDeclaration", 
                   "dataType", "identifierList", "functionDeclaration", 
                   "parameterList", "parameter", "compoundStmt", "localDeclarations", 
                   "statementList", "statement", "expressionStmt", "selectionStmt", 
                   "iterationStmt", "returnStmt", "expression", "variable", 
                   "simpleExpression", "additiveExpression", "term", "factor", 
                   "call", "args", "relationalOperator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    IDENTIFIER=31
    NUMBER=32
    BOOLEAN=33
    CHAR_LITERAL=34
    WS=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationList(self):
            return self.getTypedRuleContext(TinyGrammarParser.DeclarationListContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = TinyGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.declarationList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(TinyGrammarParser.DeclarationContext,0)


        def declarationList(self):
            return self.getTypedRuleContext(TinyGrammarParser.DeclarationListContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_declarationList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationList" ):
                listener.enterDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationList" ):
                listener.exitDeclarationList(self)




    def declarationList(self):

        localctx = TinyGrammarParser.DeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarationList)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.declaration()
                self.state = 55
                self.declarationList()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(TinyGrammarParser.VariableDeclarationContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(TinyGrammarParser.FunctionDeclarationContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = TinyGrammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.variableDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.functionDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self):
            return self.getTypedRuleContext(TinyGrammarParser.DataTypeContext,0)


        def identifierList(self):
            return self.getTypedRuleContext(TinyGrammarParser.IdentifierListContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = TinyGrammarParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.dataType()
            self.state = 65
            self.identifierList()
            self.state = 66
            self.match(TinyGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)




    def dataType(self):

        localctx = TinyGrammarParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(TinyGrammarParser.IDENTIFIER)
            else:
                return self.getToken(TinyGrammarParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return TinyGrammarParser.RULE_identifierList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierList" ):
                listener.enterIdentifierList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierList" ):
                listener.exitIdentifierList(self)




    def identifierList(self):

        localctx = TinyGrammarParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(TinyGrammarParser.IDENTIFIER)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 71
                self.match(TinyGrammarParser.T__5)
                self.state = 72
                self.match(TinyGrammarParser.IDENTIFIER)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self):
            return self.getTypedRuleContext(TinyGrammarParser.DataTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(TinyGrammarParser.IDENTIFIER, 0)

        def parameterList(self):
            return self.getTypedRuleContext(TinyGrammarParser.ParameterListContext,0)


        def compoundStmt(self):
            return self.getTypedRuleContext(TinyGrammarParser.CompoundStmtContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = TinyGrammarParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.dataType()
            self.state = 79
            self.match(TinyGrammarParser.IDENTIFIER)
            self.state = 80
            self.match(TinyGrammarParser.T__6)
            self.state = 81
            self.parameterList()
            self.state = 82
            self.match(TinyGrammarParser.T__7)
            self.state = 83
            self.compoundStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyGrammarParser.ParameterContext)
            else:
                return self.getTypedRuleContext(TinyGrammarParser.ParameterContext,i)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = TinyGrammarParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.parameter()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 86
                    self.match(TinyGrammarParser.T__5)
                    self.state = 87
                    self.parameter()
                    self.state = 92
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self):
            return self.getTypedRuleContext(TinyGrammarParser.DataTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(TinyGrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TinyGrammarParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = TinyGrammarParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.dataType()
            self.state = 97
            self.match(TinyGrammarParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def localDeclarations(self):
            return self.getTypedRuleContext(TinyGrammarParser.LocalDeclarationsContext,0)


        def statementList(self):
            return self.getTypedRuleContext(TinyGrammarParser.StatementListContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_compoundStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStmt" ):
                listener.enterCompoundStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStmt" ):
                listener.exitCompoundStmt(self)




    def compoundStmt(self):

        localctx = TinyGrammarParser.CompoundStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_compoundStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(TinyGrammarParser.T__8)
            self.state = 100
            self.localDeclarations(0)
            self.state = 101
            self.statementList(0)
            self.state = 102
            self.match(TinyGrammarParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalDeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def localDeclarations(self):
            return self.getTypedRuleContext(TinyGrammarParser.LocalDeclarationsContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(TinyGrammarParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_localDeclarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocalDeclarations" ):
                listener.enterLocalDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocalDeclarations" ):
                listener.exitLocalDeclarations(self)



    def localDeclarations(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TinyGrammarParser.LocalDeclarationsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_localDeclarations, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 109
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TinyGrammarParser.LocalDeclarationsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_localDeclarations)
                    self.state = 105
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 106
                    self.variableDeclaration() 
                self.state = 111
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(TinyGrammarParser.StatementListContext,0)


        def statement(self):
            return self.getTypedRuleContext(TinyGrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)



    def statementList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TinyGrammarParser.StatementListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_statementList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self._ctx.stop = self._input.LT(-1)
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TinyGrammarParser.StatementListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statementList)
                    self.state = 113
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 114
                    self.statement() 
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionStmt(self):
            return self.getTypedRuleContext(TinyGrammarParser.ExpressionStmtContext,0)


        def compoundStmt(self):
            return self.getTypedRuleContext(TinyGrammarParser.CompoundStmtContext,0)


        def selectionStmt(self):
            return self.getTypedRuleContext(TinyGrammarParser.SelectionStmtContext,0)


        def iterationStmt(self):
            return self.getTypedRuleContext(TinyGrammarParser.IterationStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(TinyGrammarParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = TinyGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 23, 24, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.expressionStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.compoundStmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.selectionStmt()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.iterationStmt()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.returnStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TinyGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_expressionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStmt" ):
                listener.enterExpressionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStmt" ):
                listener.exitExpressionStmt(self)




    def expressionStmt(self):

        localctx = TinyGrammarParser.ExpressionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expressionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.expression()
            self.state = 128
            self.match(TinyGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TinyGrammarParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(TinyGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_selectionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionStmt" ):
                listener.enterSelectionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionStmt" ):
                listener.exitSelectionStmt(self)




    def selectionStmt(self):

        localctx = TinyGrammarParser.SelectionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_selectionStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(TinyGrammarParser.T__10)
            self.state = 131
            self.match(TinyGrammarParser.T__6)
            self.state = 132
            self.expression()
            self.state = 133
            self.match(TinyGrammarParser.T__7)
            self.state = 134
            self.statement()
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 135
                self.match(TinyGrammarParser.T__11)
                self.state = 136
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterationStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TinyGrammarParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(TinyGrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_iterationStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterationStmt" ):
                listener.enterIterationStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterationStmt" ):
                listener.exitIterationStmt(self)




    def iterationStmt(self):

        localctx = TinyGrammarParser.IterationStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_iterationStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(TinyGrammarParser.T__12)
            self.state = 140
            self.match(TinyGrammarParser.T__6)
            self.state = 141
            self.expression()
            self.state = 142
            self.match(TinyGrammarParser.T__7)
            self.state = 143
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TinyGrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)




    def returnStmt(self):

        localctx = TinyGrammarParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(TinyGrammarParser.T__13)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32237420672) != 0):
                self.state = 146
                self.expression()


            self.state = 149
            self.match(TinyGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(TinyGrammarParser.VariableContext,0)


        def expression(self):
            return self.getTypedRuleContext(TinyGrammarParser.ExpressionContext,0)


        def simpleExpression(self):
            return self.getTypedRuleContext(TinyGrammarParser.SimpleExpressionContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = TinyGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.variable()
                self.state = 152
                self.match(TinyGrammarParser.T__14)
                self.state = 153
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.simpleExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TinyGrammarParser.IDENTIFIER, 0)

        def additiveExpression(self):
            return self.getTypedRuleContext(TinyGrammarParser.AdditiveExpressionContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = TinyGrammarParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_variable)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(TinyGrammarParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(TinyGrammarParser.IDENTIFIER)
                self.state = 160
                self.match(TinyGrammarParser.T__15)
                self.state = 161
                self.additiveExpression(0)
                self.state = 162
                self.match(TinyGrammarParser.T__16)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyGrammarParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(TinyGrammarParser.AdditiveExpressionContext,i)


        def relationalOperator(self):
            return self.getTypedRuleContext(TinyGrammarParser.RelationalOperatorContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_simpleExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleExpression" ):
                listener.enterSimpleExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleExpression" ):
                listener.exitSimpleExpression(self)




    def simpleExpression(self):

        localctx = TinyGrammarParser.SimpleExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_simpleExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.additiveExpression(0)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0):
                self.state = 167
                self.relationalOperator()
                self.state = 168
                self.additiveExpression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(TinyGrammarParser.TermContext,0)


        def additiveExpression(self):
            return self.getTypedRuleContext(TinyGrammarParser.AdditiveExpressionContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)



    def additiveExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TinyGrammarParser.AdditiveExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_additiveExpression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 181
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = TinyGrammarParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 175
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 176
                        self.match(TinyGrammarParser.T__17)
                        self.state = 177
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = TinyGrammarParser.AdditiveExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpression)
                        self.state = 178
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 179
                        self.match(TinyGrammarParser.T__18)
                        self.state = 180
                        self.term(0)
                        pass

             
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(TinyGrammarParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(TinyGrammarParser.TermContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TinyGrammarParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 198
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = TinyGrammarParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 189
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 190
                        self.match(TinyGrammarParser.T__19)
                        self.state = 191
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = TinyGrammarParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 192
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 193
                        self.match(TinyGrammarParser.T__20)
                        self.state = 194
                        self.factor()
                        pass

                    elif la_ == 3:
                        localctx = TinyGrammarParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 195
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 196
                        self.match(TinyGrammarParser.T__21)
                        self.state = 197
                        self.factor()
                        pass

             
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TinyGrammarParser.ExpressionContext,0)


        def variable(self):
            return self.getTypedRuleContext(TinyGrammarParser.VariableContext,0)


        def call(self):
            return self.getTypedRuleContext(TinyGrammarParser.CallContext,0)


        def NUMBER(self):
            return self.getToken(TinyGrammarParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(TinyGrammarParser.BOOLEAN, 0)

        def CHAR_LITERAL(self):
            return self.getToken(TinyGrammarParser.CHAR_LITERAL, 0)

        def getRuleIndex(self):
            return TinyGrammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = TinyGrammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_factor)
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(TinyGrammarParser.T__6)
                self.state = 204
                self.expression()
                self.state = 205
                self.match(TinyGrammarParser.T__7)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.match(TinyGrammarParser.NUMBER)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.match(TinyGrammarParser.BOOLEAN)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 211
                self.match(TinyGrammarParser.CHAR_LITERAL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 212
                self.match(TinyGrammarParser.T__22)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 213
                self.match(TinyGrammarParser.T__23)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TinyGrammarParser.IDENTIFIER, 0)

        def args(self):
            return self.getTypedRuleContext(TinyGrammarParser.ArgsContext,0)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = TinyGrammarParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(TinyGrammarParser.IDENTIFIER)
            self.state = 217
            self.match(TinyGrammarParser.T__6)
            self.state = 218
            self.args()
            self.state = 219
            self.match(TinyGrammarParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(TinyGrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = TinyGrammarParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 23, 24, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.expression()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 222
                    self.match(TinyGrammarParser.T__5)
                    self.state = 223
                    self.expression()
                    self.state = 228
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TinyGrammarParser.RULE_relationalOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalOperator" ):
                listener.enterRelationalOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalOperator" ):
                listener.exitRelationalOperator(self)




    def relationalOperator(self):

        localctx = TinyGrammarParser.RelationalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_relationalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2113929216) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.localDeclarations_sempred
        self._predicates[11] = self.statementList_sempred
        self._predicates[20] = self.additiveExpression_sempred
        self._predicates[21] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def localDeclarations_sempred(self, localctx:LocalDeclarationsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def statementList_sempred(self, localctx:StatementListContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def additiveExpression_sempred(self, localctx:AdditiveExpressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




