// Generated from .\TinyGrammar.g4 by ANTLR 4.13.0
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TinyGrammarParser}.
 */
public interface TinyGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(TinyGrammarParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(TinyGrammarParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#declarationList}.
	 * @param ctx the parse tree
	 */
	void enterDeclarationList(TinyGrammarParser.DeclarationListContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#declarationList}.
	 * @param ctx the parse tree
	 */
	void exitDeclarationList(TinyGrammarParser.DeclarationListContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(TinyGrammarParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(TinyGrammarParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#functionList}.
	 * @param ctx the parse tree
	 */
	void enterFunctionList(TinyGrammarParser.FunctionListContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#functionList}.
	 * @param ctx the parse tree
	 */
	void exitFunctionList(TinyGrammarParser.FunctionListContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(TinyGrammarParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(TinyGrammarParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void enterParameterList(TinyGrammarParser.ParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void exitParameterList(TinyGrammarParser.ParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(TinyGrammarParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(TinyGrammarParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(TinyGrammarParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(TinyGrammarParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#statementList}.
	 * @param ctx the parse tree
	 */
	void enterStatementList(TinyGrammarParser.StatementListContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#statementList}.
	 * @param ctx the parse tree
	 */
	void exitStatementList(TinyGrammarParser.StatementListContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(TinyGrammarParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(TinyGrammarParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(TinyGrammarParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(TinyGrammarParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(TinyGrammarParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(TinyGrammarParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void enterWhileLoop(TinyGrammarParser.WhileLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void exitWhileLoop(TinyGrammarParser.WhileLoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(TinyGrammarParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(TinyGrammarParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(TinyGrammarParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(TinyGrammarParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(TinyGrammarParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(TinyGrammarParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(TinyGrammarParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(TinyGrammarParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(TinyGrammarParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(TinyGrammarParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(TinyGrammarParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(TinyGrammarParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(TinyGrammarParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(TinyGrammarParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link TinyGrammarParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(TinyGrammarParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link TinyGrammarParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(TinyGrammarParser.IdentifierContext ctx);
}