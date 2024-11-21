# Generated from little_duck.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .little_duckParser import little_duckParser
else:
    from little_duckParser import little_duckParser

# This class defines a complete listener for a parse tree produced by little_duckParser.
class little_duckListener(ParseTreeListener):

    # Enter a parse tree produced by little_duckParser#programa.
    def enterPrograma(self, ctx:little_duckParser.ProgramaContext):
        pass

    # Exit a parse tree produced by little_duckParser#programa.
    def exitPrograma(self, ctx:little_duckParser.ProgramaContext):
        pass


    # Enter a parse tree produced by little_duckParser#inicio.
    def enterInicio(self, ctx:little_duckParser.InicioContext):
        pass

    # Exit a parse tree produced by little_duckParser#inicio.
    def exitInicio(self, ctx:little_duckParser.InicioContext):
        pass


    # Enter a parse tree produced by little_duckParser#vars.
    def enterVars(self, ctx:little_duckParser.VarsContext):
        pass

    # Exit a parse tree produced by little_duckParser#vars.
    def exitVars(self, ctx:little_duckParser.VarsContext):
        pass


    # Enter a parse tree produced by little_duckParser#var_decl_list.
    def enterVar_decl_list(self, ctx:little_duckParser.Var_decl_listContext):
        pass

    # Exit a parse tree produced by little_duckParser#var_decl_list.
    def exitVar_decl_list(self, ctx:little_duckParser.Var_decl_listContext):
        pass


    # Enter a parse tree produced by little_duckParser#var_decl.
    def enterVar_decl(self, ctx:little_duckParser.Var_declContext):
        pass

    # Exit a parse tree produced by little_duckParser#var_decl.
    def exitVar_decl(self, ctx:little_duckParser.Var_declContext):
        pass


    # Enter a parse tree produced by little_duckParser#id_list.
    def enterId_list(self, ctx:little_duckParser.Id_listContext):
        pass

    # Exit a parse tree produced by little_duckParser#id_list.
    def exitId_list(self, ctx:little_duckParser.Id_listContext):
        pass


    # Enter a parse tree produced by little_duckParser#tipo.
    def enterTipo(self, ctx:little_duckParser.TipoContext):
        pass

    # Exit a parse tree produced by little_duckParser#tipo.
    def exitTipo(self, ctx:little_duckParser.TipoContext):
        pass


    # Enter a parse tree produced by little_duckParser#funcs.
    def enterFuncs(self, ctx:little_duckParser.FuncsContext):
        pass

    # Exit a parse tree produced by little_duckParser#funcs.
    def exitFuncs(self, ctx:little_duckParser.FuncsContext):
        pass


    # Enter a parse tree produced by little_duckParser#func_decl.
    def enterFunc_decl(self, ctx:little_duckParser.Func_declContext):
        pass

    # Exit a parse tree produced by little_duckParser#func_decl.
    def exitFunc_decl(self, ctx:little_duckParser.Func_declContext):
        pass


    # Enter a parse tree produced by little_duckParser#cuerpo_func.
    def enterCuerpo_func(self, ctx:little_duckParser.Cuerpo_funcContext):
        pass

    # Exit a parse tree produced by little_duckParser#cuerpo_func.
    def exitCuerpo_func(self, ctx:little_duckParser.Cuerpo_funcContext):
        pass


    # Enter a parse tree produced by little_duckParser#param_list.
    def enterParam_list(self, ctx:little_duckParser.Param_listContext):
        pass

    # Exit a parse tree produced by little_duckParser#param_list.
    def exitParam_list(self, ctx:little_duckParser.Param_listContext):
        pass


    # Enter a parse tree produced by little_duckParser#param.
    def enterParam(self, ctx:little_duckParser.ParamContext):
        pass

    # Exit a parse tree produced by little_duckParser#param.
    def exitParam(self, ctx:little_duckParser.ParamContext):
        pass


    # Enter a parse tree produced by little_duckParser#cuerpo.
    def enterCuerpo(self, ctx:little_duckParser.CuerpoContext):
        pass

    # Exit a parse tree produced by little_duckParser#cuerpo.
    def exitCuerpo(self, ctx:little_duckParser.CuerpoContext):
        pass


    # Enter a parse tree produced by little_duckParser#estatuto.
    def enterEstatuto(self, ctx:little_duckParser.EstatutoContext):
        pass

    # Exit a parse tree produced by little_duckParser#estatuto.
    def exitEstatuto(self, ctx:little_duckParser.EstatutoContext):
        pass


    # Enter a parse tree produced by little_duckParser#asigna.
    def enterAsigna(self, ctx:little_duckParser.AsignaContext):
        pass

    # Exit a parse tree produced by little_duckParser#asigna.
    def exitAsigna(self, ctx:little_duckParser.AsignaContext):
        pass


    # Enter a parse tree produced by little_duckParser#imprime.
    def enterImprime(self, ctx:little_duckParser.ImprimeContext):
        pass

    # Exit a parse tree produced by little_duckParser#imprime.
    def exitImprime(self, ctx:little_duckParser.ImprimeContext):
        pass


    # Enter a parse tree produced by little_duckParser#print_list.
    def enterPrint_list(self, ctx:little_duckParser.Print_listContext):
        pass

    # Exit a parse tree produced by little_duckParser#print_list.
    def exitPrint_list(self, ctx:little_duckParser.Print_listContext):
        pass


    # Enter a parse tree produced by little_duckParser#print_item.
    def enterPrint_item(self, ctx:little_duckParser.Print_itemContext):
        pass

    # Exit a parse tree produced by little_duckParser#print_item.
    def exitPrint_item(self, ctx:little_duckParser.Print_itemContext):
        pass


    # Enter a parse tree produced by little_duckParser#ciclo.
    def enterCiclo(self, ctx:little_duckParser.CicloContext):
        pass

    # Exit a parse tree produced by little_duckParser#ciclo.
    def exitCiclo(self, ctx:little_duckParser.CicloContext):
        pass


    # Enter a parse tree produced by little_duckParser#condicion.
    def enterCondicion(self, ctx:little_duckParser.CondicionContext):
        pass

    # Exit a parse tree produced by little_duckParser#condicion.
    def exitCondicion(self, ctx:little_duckParser.CondicionContext):
        pass


    # Enter a parse tree produced by little_duckParser#condicion_else.
    def enterCondicion_else(self, ctx:little_duckParser.Condicion_elseContext):
        pass

    # Exit a parse tree produced by little_duckParser#condicion_else.
    def exitCondicion_else(self, ctx:little_duckParser.Condicion_elseContext):
        pass


    # Enter a parse tree produced by little_duckParser#llamada.
    def enterLlamada(self, ctx:little_duckParser.LlamadaContext):
        pass

    # Exit a parse tree produced by little_duckParser#llamada.
    def exitLlamada(self, ctx:little_duckParser.LlamadaContext):
        pass


    # Enter a parse tree produced by little_duckParser#arg_list.
    def enterArg_list(self, ctx:little_duckParser.Arg_listContext):
        pass

    # Exit a parse tree produced by little_duckParser#arg_list.
    def exitArg_list(self, ctx:little_duckParser.Arg_listContext):
        pass


    # Enter a parse tree produced by little_duckParser#expresion.
    def enterExpresion(self, ctx:little_duckParser.ExpresionContext):
        pass

    # Exit a parse tree produced by little_duckParser#expresion.
    def exitExpresion(self, ctx:little_duckParser.ExpresionContext):
        pass


    # Enter a parse tree produced by little_duckParser#op_comparacion.
    def enterOp_comparacion(self, ctx:little_duckParser.Op_comparacionContext):
        pass

    # Exit a parse tree produced by little_duckParser#op_comparacion.
    def exitOp_comparacion(self, ctx:little_duckParser.Op_comparacionContext):
        pass


    # Enter a parse tree produced by little_duckParser#exp.
    def enterExp(self, ctx:little_duckParser.ExpContext):
        pass

    # Exit a parse tree produced by little_duckParser#exp.
    def exitExp(self, ctx:little_duckParser.ExpContext):
        pass


    # Enter a parse tree produced by little_duckParser#termino.
    def enterTermino(self, ctx:little_duckParser.TerminoContext):
        pass

    # Exit a parse tree produced by little_duckParser#termino.
    def exitTermino(self, ctx:little_duckParser.TerminoContext):
        pass


    # Enter a parse tree produced by little_duckParser#factor.
    def enterFactor(self, ctx:little_duckParser.FactorContext):
        pass

    # Exit a parse tree produced by little_duckParser#factor.
    def exitFactor(self, ctx:little_duckParser.FactorContext):
        pass


    # Enter a parse tree produced by little_duckParser#cte.
    def enterCte(self, ctx:little_duckParser.CteContext):
        pass

    # Exit a parse tree produced by little_duckParser#cte.
    def exitCte(self, ctx:little_duckParser.CteContext):
        pass



del little_duckParser