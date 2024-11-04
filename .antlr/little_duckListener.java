// Generated from /Users/gerardomartinez/Desktop/9no/little_duck/little_duck.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link little_duckParser}.
 */
public interface little_duckListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link little_duckParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(little_duckParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(little_duckParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#vars}.
	 * @param ctx the parse tree
	 */
	void enterVars(little_duckParser.VarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#vars}.
	 * @param ctx the parse tree
	 */
	void exitVars(little_duckParser.VarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#var_decl_list}.
	 * @param ctx the parse tree
	 */
	void enterVar_decl_list(little_duckParser.Var_decl_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#var_decl_list}.
	 * @param ctx the parse tree
	 */
	void exitVar_decl_list(little_duckParser.Var_decl_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#var_decl}.
	 * @param ctx the parse tree
	 */
	void enterVar_decl(little_duckParser.Var_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#var_decl}.
	 * @param ctx the parse tree
	 */
	void exitVar_decl(little_duckParser.Var_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#id_list}.
	 * @param ctx the parse tree
	 */
	void enterId_list(little_duckParser.Id_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#id_list}.
	 * @param ctx the parse tree
	 */
	void exitId_list(little_duckParser.Id_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(little_duckParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(little_duckParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#funcs}.
	 * @param ctx the parse tree
	 */
	void enterFuncs(little_duckParser.FuncsContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#funcs}.
	 * @param ctx the parse tree
	 */
	void exitFuncs(little_duckParser.FuncsContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#func_decl}.
	 * @param ctx the parse tree
	 */
	void enterFunc_decl(little_duckParser.Func_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#func_decl}.
	 * @param ctx the parse tree
	 */
	void exitFunc_decl(little_duckParser.Func_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#param_list}.
	 * @param ctx the parse tree
	 */
	void enterParam_list(little_duckParser.Param_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#param_list}.
	 * @param ctx the parse tree
	 */
	void exitParam_list(little_duckParser.Param_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(little_duckParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(little_duckParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#cuerpo}.
	 * @param ctx the parse tree
	 */
	void enterCuerpo(little_duckParser.CuerpoContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#cuerpo}.
	 * @param ctx the parse tree
	 */
	void exitCuerpo(little_duckParser.CuerpoContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#estatuto}.
	 * @param ctx the parse tree
	 */
	void enterEstatuto(little_duckParser.EstatutoContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#estatuto}.
	 * @param ctx the parse tree
	 */
	void exitEstatuto(little_duckParser.EstatutoContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#asigna}.
	 * @param ctx the parse tree
	 */
	void enterAsigna(little_duckParser.AsignaContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#asigna}.
	 * @param ctx the parse tree
	 */
	void exitAsigna(little_duckParser.AsignaContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#imprime}.
	 * @param ctx the parse tree
	 */
	void enterImprime(little_duckParser.ImprimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#imprime}.
	 * @param ctx the parse tree
	 */
	void exitImprime(little_duckParser.ImprimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#print_list}.
	 * @param ctx the parse tree
	 */
	void enterPrint_list(little_duckParser.Print_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#print_list}.
	 * @param ctx the parse tree
	 */
	void exitPrint_list(little_duckParser.Print_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#print_item}.
	 * @param ctx the parse tree
	 */
	void enterPrint_item(little_duckParser.Print_itemContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#print_item}.
	 * @param ctx the parse tree
	 */
	void exitPrint_item(little_duckParser.Print_itemContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#ciclo}.
	 * @param ctx the parse tree
	 */
	void enterCiclo(little_duckParser.CicloContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#ciclo}.
	 * @param ctx the parse tree
	 */
	void exitCiclo(little_duckParser.CicloContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#condicion}.
	 * @param ctx the parse tree
	 */
	void enterCondicion(little_duckParser.CondicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#condicion}.
	 * @param ctx the parse tree
	 */
	void exitCondicion(little_duckParser.CondicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#condicion_else}.
	 * @param ctx the parse tree
	 */
	void enterCondicion_else(little_duckParser.Condicion_elseContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#condicion_else}.
	 * @param ctx the parse tree
	 */
	void exitCondicion_else(little_duckParser.Condicion_elseContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#llamada}.
	 * @param ctx the parse tree
	 */
	void enterLlamada(little_duckParser.LlamadaContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#llamada}.
	 * @param ctx the parse tree
	 */
	void exitLlamada(little_duckParser.LlamadaContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#arg_list}.
	 * @param ctx the parse tree
	 */
	void enterArg_list(little_duckParser.Arg_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#arg_list}.
	 * @param ctx the parse tree
	 */
	void exitArg_list(little_duckParser.Arg_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(little_duckParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(little_duckParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#op_comparacion}.
	 * @param ctx the parse tree
	 */
	void enterOp_comparacion(little_duckParser.Op_comparacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#op_comparacion}.
	 * @param ctx the parse tree
	 */
	void exitOp_comparacion(little_duckParser.Op_comparacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(little_duckParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(little_duckParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(little_duckParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(little_duckParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(little_duckParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(little_duckParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link little_duckParser#cte}.
	 * @param ctx the parse tree
	 */
	void enterCte(little_duckParser.CteContext ctx);
	/**
	 * Exit a parse tree produced by {@link little_duckParser#cte}.
	 * @param ctx the parse tree
	 */
	void exitCte(little_duckParser.CteContext ctx);
}