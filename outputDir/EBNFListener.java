// Generated from EBNF.g4 by ANTLR 4.13.0
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
	 * Enter a parse tree produced by {@link EBNFParser#declarations}.
	 * @param ctx the parse tree
	 */
	void enterDeclarations(EBNFParser.DeclarationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#declarations}.
	 * @param ctx the parse tree
	 */
	void exitDeclarations(EBNFParser.DeclarationsContext ctx);
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
	 * Enter a parse tree produced by {@link EBNFParser#statements}.
	 * @param ctx the parse tree
	 */
	void enterStatements(EBNFParser.StatementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#statements}.
	 * @param ctx the parse tree
	 */
	void exitStatements(EBNFParser.StatementsContext ctx);
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
	 * Enter a parse tree produced by {@link EBNFParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void enterIf_statement(EBNFParser.If_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void exitIf_statement(EBNFParser.If_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#while_loop}.
	 * @param ctx the parse tree
	 */
	void enterWhile_loop(EBNFParser.While_loopContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#while_loop}.
	 * @param ctx the parse tree
	 */
	void exitWhile_loop(EBNFParser.While_loopContext ctx);
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
	 * Enter a parse tree produced by {@link EBNFParser#identifier}.
	 * @param ctx the parse tree
	 */
	void enterIdentifier(EBNFParser.IdentifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#identifier}.
	 * @param ctx the parse tree
	 */
	void exitIdentifier(EBNFParser.IdentifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link EBNFParser#constant}.
	 * @param ctx the parse tree
	 */
	void enterConstant(EBNFParser.ConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link EBNFParser#constant}.
	 * @param ctx the parse tree
	 */
	void exitConstant(EBNFParser.ConstantContext ctx);
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
}