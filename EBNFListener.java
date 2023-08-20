// Generated from .\EBNF.g4 by ANTLR 4.13.0
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link EBNFParser}.
 */
public interface EBNFListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link EBNFParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(EBNFParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(EBNFParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#declarationList}.
	 * @param ctx the parse tree
	 */
	void enterDeclarationList(EBNFParser.DeclarationListContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#declarationList}.
	 * @param ctx the parse tree
	 */
	void exitDeclarationList(EBNFParser.DeclarationListContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(EBNFParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(EBNFParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#functionList}.
	 * @param ctx the parse tree
	 */
	void enterFunctionList(EBNFParser.FunctionListContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#functionList}.
	 * @param ctx the parse tree
	 */
	void exitFunctionList(EBNFParser.FunctionListContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(EBNFParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(EBNFParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void enterParameterList(EBNFParser.ParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void exitParameterList(EBNFParser.ParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(EBNFParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(EBNFParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(EBNFParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(EBNFParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#statementList}.
	 * @param ctx the parse tree
	 */
	void enterStatementList(EBNFParser.StatementListContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#statementList}.
	 * @param ctx the parse tree
	 */
	void exitStatementList(EBNFParser.StatementListContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(EBNFParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(EBNFParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(EBNFParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(EBNFParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(EBNFParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(EBNFParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void enterWhileLoop(EBNFParser.WhileLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void exitWhileLoop(EBNFParser.WhileLoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(EBNFParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(EBNFParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(EBNFParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(EBNFParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(EBNFParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(EBNFParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(EBNFParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(EBNFParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(EBNFParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(EBNFParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(EBNFParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(EBNFParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(EBNFParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(EBNFParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(EBNFParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(EBNFParser.IdentifierContext ctx);
}