// Generated from /Users/gerardomartinez/Desktop/9no/little_duck/little_duck.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class little_duckParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROGRAMA=1, VARS=2, INICIO=3, FIN=4, ENTERO=5, FLOTANTE=6, ESCRIBE=7, 
		MIENTRAS=8, HAZ=9, SI=10, SINO=11, FUNC=12, ASSIGN=13, SEMI=14, COLON=15, 
		COMMA=16, LPAREN=17, RPAREN=18, LBRACE=19, RBRACE=20, PLUS=21, MINUS=22, 
		MULT=23, DIV=24, GT=25, LT=26, NEQ=27, EQ=28, ID=29, CTE_ENT=30, CTE_FLOT=31, 
		STRING_LITERAL=32, WS=33, COMMENT=34;
	public static final int
		RULE_programa = 0, RULE_inicio = 1, RULE_vars = 2, RULE_var_decl_list = 3, 
		RULE_var_decl = 4, RULE_id_list = 5, RULE_tipo = 6, RULE_funcs = 7, RULE_func_decl = 8, 
		RULE_cuerpo_func = 9, RULE_param_list = 10, RULE_param = 11, RULE_cuerpo = 12, 
		RULE_estatuto = 13, RULE_asigna = 14, RULE_imprime = 15, RULE_print_list = 16, 
		RULE_print_item = 17, RULE_ciclo = 18, RULE_condicion = 19, RULE_condicion_else = 20, 
		RULE_llamada = 21, RULE_arg_list = 22, RULE_expresion = 23, RULE_op_comparacion = 24, 
		RULE_exp = 25, RULE_termino = 26, RULE_factor = 27, RULE_cte = 28;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "inicio", "vars", "var_decl_list", "var_decl", "id_list", 
			"tipo", "funcs", "func_decl", "cuerpo_func", "param_list", "param", "cuerpo", 
			"estatuto", "asigna", "imprime", "print_list", "print_item", "ciclo", 
			"condicion", "condicion_else", "llamada", "arg_list", "expresion", "op_comparacion", 
			"exp", "termino", "factor", "cte"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'programa'", "'vars'", "'inicio'", "'fin'", "'entero'", "'flotante'", 
			"'escribe'", "'mientras'", "'haz'", "'si'", "'sino'", "'func'", "'='", 
			"';'", "':'", "','", "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", 
			"'/'", "'>'", "'<'", "'!='", "'=='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAMA", "VARS", "INICIO", "FIN", "ENTERO", "FLOTANTE", "ESCRIBE", 
			"MIENTRAS", "HAZ", "SI", "SINO", "FUNC", "ASSIGN", "SEMI", "COLON", "COMMA", 
			"LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", "MULT", "DIV", 
			"GT", "LT", "NEQ", "EQ", "ID", "CTE_ENT", "CTE_FLOT", "STRING_LITERAL", 
			"WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "little_duck.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public little_duckParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode PROGRAMA() { return getToken(little_duckParser.PROGRAMA, 0); }
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public TerminalNode SEMI() { return getToken(little_duckParser.SEMI, 0); }
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public FuncsContext funcs() {
			return getRuleContext(FuncsContext.class,0);
		}
		public InicioContext inicio() {
			return getRuleContext(InicioContext.class,0);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(PROGRAMA);
			setState(59);
			match(ID);
			setState(60);
			match(SEMI);
			setState(61);
			vars();
			setState(62);
			funcs();
			setState(63);
			inicio();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InicioContext extends ParserRuleContext {
		public TerminalNode INICIO() { return getToken(little_duckParser.INICIO, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public TerminalNode FIN() { return getToken(little_duckParser.FIN, 0); }
		public InicioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inicio; }
	}

	public final InicioContext inicio() throws RecognitionException {
		InicioContext _localctx = new InicioContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_inicio);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			match(INICIO);
			setState(66);
			cuerpo();
			setState(67);
			match(FIN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarsContext extends ParserRuleContext {
		public TerminalNode VARS() { return getToken(little_duckParser.VARS, 0); }
		public TerminalNode LBRACE() { return getToken(little_duckParser.LBRACE, 0); }
		public Var_decl_listContext var_decl_list() {
			return getRuleContext(Var_decl_listContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(little_duckParser.RBRACE, 0); }
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vars);
		try {
			setState(75);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VARS:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				match(VARS);
				setState(70);
				match(LBRACE);
				setState(71);
				var_decl_list();
				setState(72);
				match(RBRACE);
				}
				break;
			case INICIO:
			case ESCRIBE:
			case MIENTRAS:
			case SI:
			case FUNC:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_decl_listContext extends ParserRuleContext {
		public List<Var_declContext> var_decl() {
			return getRuleContexts(Var_declContext.class);
		}
		public Var_declContext var_decl(int i) {
			return getRuleContext(Var_declContext.class,i);
		}
		public Var_decl_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl_list; }
	}

	public final Var_decl_listContext var_decl_list() throws RecognitionException {
		Var_decl_listContext _localctx = new Var_decl_listContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_var_decl_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(77);
				var_decl();
				}
				}
				setState(80); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_declContext extends ParserRuleContext {
		public Id_listContext id_list() {
			return getRuleContext(Id_listContext.class,0);
		}
		public TerminalNode COLON() { return getToken(little_duckParser.COLON, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(little_duckParser.SEMI, 0); }
		public Var_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl; }
	}

	public final Var_declContext var_decl() throws RecognitionException {
		Var_declContext _localctx = new Var_declContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_var_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			id_list();
			setState(83);
			match(COLON);
			setState(84);
			tipo();
			setState(85);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Id_listContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(little_duckParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(little_duckParser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(little_duckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(little_duckParser.COMMA, i);
		}
		public Id_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_list; }
	}

	public final Id_listContext id_list() throws RecognitionException {
		Id_listContext _localctx = new Id_listContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_id_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			match(ID);
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(88);
				match(COMMA);
				setState(89);
				match(ID);
				}
				}
				setState(94);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode ENTERO() { return getToken(little_duckParser.ENTERO, 0); }
		public TerminalNode FLOTANTE() { return getToken(little_duckParser.FLOTANTE, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			_la = _input.LA(1);
			if ( !(_la==ENTERO || _la==FLOTANTE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncsContext extends ParserRuleContext {
		public Func_declContext func_decl() {
			return getRuleContext(Func_declContext.class,0);
		}
		public FuncsContext funcs() {
			return getRuleContext(FuncsContext.class,0);
		}
		public FuncsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs; }
	}

	public final FuncsContext funcs() throws RecognitionException {
		FuncsContext _localctx = new FuncsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_funcs);
		try {
			setState(101);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FUNC:
				enterOuterAlt(_localctx, 1);
				{
				setState(97);
				func_decl();
				setState(98);
				funcs();
				}
				break;
			case INICIO:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Func_declContext extends ParserRuleContext {
		public TerminalNode FUNC() { return getToken(little_duckParser.FUNC, 0); }
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(little_duckParser.LPAREN, 0); }
		public Param_listContext param_list() {
			return getRuleContext(Param_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(little_duckParser.RPAREN, 0); }
		public Cuerpo_funcContext cuerpo_func() {
			return getRuleContext(Cuerpo_funcContext.class,0);
		}
		public Func_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_decl; }
	}

	public final Func_declContext func_decl() throws RecognitionException {
		Func_declContext _localctx = new Func_declContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_func_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(FUNC);
			setState(104);
			match(ID);
			setState(105);
			match(LPAREN);
			setState(106);
			param_list();
			setState(107);
			match(RPAREN);
			setState(108);
			cuerpo_func();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Cuerpo_funcContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(little_duckParser.LBRACE, 0); }
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(little_duckParser.RBRACE, 0); }
		public List<EstatutoContext> estatuto() {
			return getRuleContexts(EstatutoContext.class);
		}
		public EstatutoContext estatuto(int i) {
			return getRuleContext(EstatutoContext.class,i);
		}
		public Cuerpo_funcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cuerpo_func; }
	}

	public final Cuerpo_funcContext cuerpo_func() throws RecognitionException {
		Cuerpo_funcContext _localctx = new Cuerpo_funcContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_cuerpo_func);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			match(LBRACE);
			setState(111);
			vars();
			setState(113); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(112);
				estatuto();
				}
				}
				setState(115); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 536872320L) != 0) );
			setState(117);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Param_listContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(little_duckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(little_duckParser.COMMA, i);
		}
		public Param_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_list; }
	}

	public final Param_listContext param_list() throws RecognitionException {
		Param_listContext _localctx = new Param_listContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_param_list);
		int _la;
		try {
			setState(128);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(119);
				param();
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(120);
					match(COMMA);
					setState(121);
					param();
					}
					}
					setState(126);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case RPAREN:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public TerminalNode COLON() { return getToken(little_duckParser.COLON, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			match(ID);
			setState(131);
			match(COLON);
			setState(132);
			tipo();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CuerpoContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(little_duckParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(little_duckParser.RBRACE, 0); }
		public List<EstatutoContext> estatuto() {
			return getRuleContexts(EstatutoContext.class);
		}
		public EstatutoContext estatuto(int i) {
			return getRuleContext(EstatutoContext.class,i);
		}
		public CuerpoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cuerpo; }
	}

	public final CuerpoContext cuerpo() throws RecognitionException {
		CuerpoContext _localctx = new CuerpoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_cuerpo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(LBRACE);
			setState(136); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(135);
				estatuto();
				}
				}
				setState(138); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 536872320L) != 0) );
			setState(140);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EstatutoContext extends ParserRuleContext {
		public AsignaContext asigna() {
			return getRuleContext(AsignaContext.class,0);
		}
		public ImprimeContext imprime() {
			return getRuleContext(ImprimeContext.class,0);
		}
		public CicloContext ciclo() {
			return getRuleContext(CicloContext.class,0);
		}
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public LlamadaContext llamada() {
			return getRuleContext(LlamadaContext.class,0);
		}
		public EstatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estatuto; }
	}

	public final EstatutoContext estatuto() throws RecognitionException {
		EstatutoContext _localctx = new EstatutoContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_estatuto);
		try {
			setState(147);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(142);
				asigna();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(143);
				imprime();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(144);
				ciclo();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(145);
				condicion();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(146);
				llamada();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(little_duckParser.ASSIGN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(little_duckParser.SEMI, 0); }
		public AsignaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asigna; }
	}

	public final AsignaContext asigna() throws RecognitionException {
		AsignaContext _localctx = new AsignaContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_asigna);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			match(ID);
			setState(150);
			match(ASSIGN);
			setState(151);
			expresion();
			setState(152);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImprimeContext extends ParserRuleContext {
		public TerminalNode ESCRIBE() { return getToken(little_duckParser.ESCRIBE, 0); }
		public TerminalNode LPAREN() { return getToken(little_duckParser.LPAREN, 0); }
		public Print_listContext print_list() {
			return getRuleContext(Print_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(little_duckParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(little_duckParser.SEMI, 0); }
		public ImprimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_imprime; }
	}

	public final ImprimeContext imprime() throws RecognitionException {
		ImprimeContext _localctx = new ImprimeContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_imprime);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			match(ESCRIBE);
			setState(155);
			match(LPAREN);
			setState(156);
			print_list();
			setState(157);
			match(RPAREN);
			setState(158);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Print_listContext extends ParserRuleContext {
		public List<Print_itemContext> print_item() {
			return getRuleContexts(Print_itemContext.class);
		}
		public Print_itemContext print_item(int i) {
			return getRuleContext(Print_itemContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(little_duckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(little_duckParser.COMMA, i);
		}
		public Print_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_list; }
	}

	public final Print_listContext print_list() throws RecognitionException {
		Print_listContext _localctx = new Print_listContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_print_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			print_item();
			setState(165);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(161);
				match(COMMA);
				setState(162);
				print_item();
				}
				}
				setState(167);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Print_itemContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode STRING_LITERAL() { return getToken(little_duckParser.STRING_LITERAL, 0); }
		public Print_itemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_item; }
	}

	public final Print_itemContext print_item() throws RecognitionException {
		Print_itemContext _localctx = new Print_itemContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_print_item);
		try {
			setState(170);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
			case ID:
			case CTE_ENT:
			case CTE_FLOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(168);
				expresion();
				}
				break;
			case STRING_LITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(169);
				match(STRING_LITERAL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CicloContext extends ParserRuleContext {
		public TerminalNode MIENTRAS() { return getToken(little_duckParser.MIENTRAS, 0); }
		public TerminalNode LPAREN() { return getToken(little_duckParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(little_duckParser.RPAREN, 0); }
		public TerminalNode HAZ() { return getToken(little_duckParser.HAZ, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public CicloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ciclo; }
	}

	public final CicloContext ciclo() throws RecognitionException {
		CicloContext _localctx = new CicloContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_ciclo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(MIENTRAS);
			setState(173);
			match(LPAREN);
			setState(174);
			expresion();
			setState(175);
			match(RPAREN);
			setState(176);
			match(HAZ);
			setState(177);
			cuerpo();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionContext extends ParserRuleContext {
		public TerminalNode SI() { return getToken(little_duckParser.SI, 0); }
		public TerminalNode LPAREN() { return getToken(little_duckParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(little_duckParser.RPAREN, 0); }
		public TerminalNode HAZ() { return getToken(little_duckParser.HAZ, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public Condicion_elseContext condicion_else() {
			return getRuleContext(Condicion_elseContext.class,0);
		}
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_condicion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			match(SI);
			setState(180);
			match(LPAREN);
			setState(181);
			expresion();
			setState(182);
			match(RPAREN);
			setState(183);
			match(HAZ);
			setState(184);
			cuerpo();
			setState(185);
			condicion_else();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Condicion_elseContext extends ParserRuleContext {
		public TerminalNode SINO() { return getToken(little_duckParser.SINO, 0); }
		public TerminalNode HAZ() { return getToken(little_duckParser.HAZ, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public Condicion_elseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion_else; }
	}

	public final Condicion_elseContext condicion_else() throws RecognitionException {
		Condicion_elseContext _localctx = new Condicion_elseContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_condicion_else);
		try {
			setState(191);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SINO:
				enterOuterAlt(_localctx, 1);
				{
				setState(187);
				match(SINO);
				setState(188);
				match(HAZ);
				setState(189);
				cuerpo();
				}
				break;
			case ESCRIBE:
			case MIENTRAS:
			case SI:
			case RBRACE:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LlamadaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(little_duckParser.LPAREN, 0); }
		public Arg_listContext arg_list() {
			return getRuleContext(Arg_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(little_duckParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(little_duckParser.SEMI, 0); }
		public LlamadaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_llamada; }
	}

	public final LlamadaContext llamada() throws RecognitionException {
		LlamadaContext _localctx = new LlamadaContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_llamada);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			match(ID);
			setState(194);
			match(LPAREN);
			setState(195);
			arg_list();
			setState(196);
			match(RPAREN);
			setState(197);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Arg_listContext extends ParserRuleContext {
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(little_duckParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(little_duckParser.COMMA, i);
		}
		public Arg_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg_list; }
	}

	public final Arg_listContext arg_list() throws RecognitionException {
		Arg_listContext _localctx = new Arg_listContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_arg_list);
		int _la;
		try {
			setState(208);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
			case ID:
			case CTE_ENT:
			case CTE_FLOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(199);
				expresion();
				setState(204);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(200);
					match(COMMA);
					setState(201);
					expresion();
					}
					}
					setState(206);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case RPAREN:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public Op_comparacionContext op_comparacion() {
			return getRuleContext(Op_comparacionContext.class,0);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			exp();
			setState(214);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 503316480L) != 0)) {
				{
				setState(211);
				op_comparacion();
				setState(212);
				exp();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Op_comparacionContext extends ParserRuleContext {
		public TerminalNode GT() { return getToken(little_duckParser.GT, 0); }
		public TerminalNode LT() { return getToken(little_duckParser.LT, 0); }
		public TerminalNode NEQ() { return getToken(little_duckParser.NEQ, 0); }
		public TerminalNode EQ() { return getToken(little_duckParser.EQ, 0); }
		public Op_comparacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_comparacion; }
	}

	public final Op_comparacionContext op_comparacion() throws RecognitionException {
		Op_comparacionContext _localctx = new Op_comparacionContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_op_comparacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 503316480L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public List<TerminoContext> termino() {
			return getRuleContexts(TerminoContext.class);
		}
		public TerminoContext termino(int i) {
			return getRuleContext(TerminoContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(little_duckParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(little_duckParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(little_duckParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(little_duckParser.MINUS, i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			termino();
			setState(223);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(219);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(220);
				termino();
				}
				}
				setState(225);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> MULT() { return getTokens(little_duckParser.MULT); }
		public TerminalNode MULT(int i) {
			return getToken(little_duckParser.MULT, i);
		}
		public List<TerminalNode> DIV() { return getTokens(little_duckParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(little_duckParser.DIV, i);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			factor();
			setState(231);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==MULT || _la==DIV) {
				{
				{
				setState(227);
				_la = _input.LA(1);
				if ( !(_la==MULT || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(228);
				factor();
				}
				}
				setState(233);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode LPAREN() { return getToken(little_duckParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(little_duckParser.RPAREN, 0); }
		public TerminalNode ID() { return getToken(little_duckParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_factor);
		try {
			setState(240);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(234);
				match(LPAREN);
				setState(235);
				expresion();
				setState(236);
				match(RPAREN);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(238);
				match(ID);
				}
				break;
			case CTE_ENT:
			case CTE_FLOT:
				enterOuterAlt(_localctx, 3);
				{
				setState(239);
				cte();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CteContext extends ParserRuleContext {
		public TerminalNode CTE_FLOT() { return getToken(little_duckParser.CTE_FLOT, 0); }
		public TerminalNode CTE_ENT() { return getToken(little_duckParser.CTE_ENT, 0); }
		public CteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cte; }
	}

	public final CteContext cte() throws RecognitionException {
		CteContext _localctx = new CteContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			_la = _input.LA(1);
			if ( !(_la==CTE_ENT || _la==CTE_FLOT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\"\u00f5\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0003\u0002L\b\u0002\u0001\u0003\u0004\u0003O\b\u0003\u000b"+
		"\u0003\f\u0003P\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0005\u0005[\b\u0005\n\u0005"+
		"\f\u0005^\t\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0003\u0007f\b\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0004\tr\b\t\u000b"+
		"\t\f\ts\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0005\n{\b\n\n\n\f\n~"+
		"\t\n\u0001\n\u0003\n\u0081\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0004\f\u0089\b\f\u000b\f\f\f\u008a\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u0094\b\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0005\u0010\u00a4\b\u0010\n\u0010\f\u0010\u00a7\t\u0010\u0001"+
		"\u0011\u0001\u0011\u0003\u0011\u00ab\b\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u00c0"+
		"\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0005\u0016\u00cb\b\u0016\n"+
		"\u0016\f\u0016\u00ce\t\u0016\u0001\u0016\u0003\u0016\u00d1\b\u0016\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0003\u0017\u00d7\b\u0017\u0001"+
		"\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0005\u0019\u00de"+
		"\b\u0019\n\u0019\f\u0019\u00e1\t\u0019\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0005\u001a\u00e6\b\u001a\n\u001a\f\u001a\u00e9\t\u001a\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0003\u001b\u00f1"+
		"\b\u001b\u0001\u001c\u0001\u001c\u0001\u001c\u0000\u0000\u001d\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e"+
		" \"$&(*,.02468\u0000\u0005\u0001\u0000\u0005\u0006\u0001\u0000\u0019\u001c"+
		"\u0001\u0000\u0015\u0016\u0001\u0000\u0017\u0018\u0001\u0000\u001e\u001f"+
		"\u00ed\u0000:\u0001\u0000\u0000\u0000\u0002A\u0001\u0000\u0000\u0000\u0004"+
		"K\u0001\u0000\u0000\u0000\u0006N\u0001\u0000\u0000\u0000\bR\u0001\u0000"+
		"\u0000\u0000\nW\u0001\u0000\u0000\u0000\f_\u0001\u0000\u0000\u0000\u000e"+
		"e\u0001\u0000\u0000\u0000\u0010g\u0001\u0000\u0000\u0000\u0012n\u0001"+
		"\u0000\u0000\u0000\u0014\u0080\u0001\u0000\u0000\u0000\u0016\u0082\u0001"+
		"\u0000\u0000\u0000\u0018\u0086\u0001\u0000\u0000\u0000\u001a\u0093\u0001"+
		"\u0000\u0000\u0000\u001c\u0095\u0001\u0000\u0000\u0000\u001e\u009a\u0001"+
		"\u0000\u0000\u0000 \u00a0\u0001\u0000\u0000\u0000\"\u00aa\u0001\u0000"+
		"\u0000\u0000$\u00ac\u0001\u0000\u0000\u0000&\u00b3\u0001\u0000\u0000\u0000"+
		"(\u00bf\u0001\u0000\u0000\u0000*\u00c1\u0001\u0000\u0000\u0000,\u00d0"+
		"\u0001\u0000\u0000\u0000.\u00d2\u0001\u0000\u0000\u00000\u00d8\u0001\u0000"+
		"\u0000\u00002\u00da\u0001\u0000\u0000\u00004\u00e2\u0001\u0000\u0000\u0000"+
		"6\u00f0\u0001\u0000\u0000\u00008\u00f2\u0001\u0000\u0000\u0000:;\u0005"+
		"\u0001\u0000\u0000;<\u0005\u001d\u0000\u0000<=\u0005\u000e\u0000\u0000"+
		"=>\u0003\u0004\u0002\u0000>?\u0003\u000e\u0007\u0000?@\u0003\u0002\u0001"+
		"\u0000@\u0001\u0001\u0000\u0000\u0000AB\u0005\u0003\u0000\u0000BC\u0003"+
		"\u0018\f\u0000CD\u0005\u0004\u0000\u0000D\u0003\u0001\u0000\u0000\u0000"+
		"EF\u0005\u0002\u0000\u0000FG\u0005\u0013\u0000\u0000GH\u0003\u0006\u0003"+
		"\u0000HI\u0005\u0014\u0000\u0000IL\u0001\u0000\u0000\u0000JL\u0001\u0000"+
		"\u0000\u0000KE\u0001\u0000\u0000\u0000KJ\u0001\u0000\u0000\u0000L\u0005"+
		"\u0001\u0000\u0000\u0000MO\u0003\b\u0004\u0000NM\u0001\u0000\u0000\u0000"+
		"OP\u0001\u0000\u0000\u0000PN\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000"+
		"\u0000Q\u0007\u0001\u0000\u0000\u0000RS\u0003\n\u0005\u0000ST\u0005\u000f"+
		"\u0000\u0000TU\u0003\f\u0006\u0000UV\u0005\u000e\u0000\u0000V\t\u0001"+
		"\u0000\u0000\u0000W\\\u0005\u001d\u0000\u0000XY\u0005\u0010\u0000\u0000"+
		"Y[\u0005\u001d\u0000\u0000ZX\u0001\u0000\u0000\u0000[^\u0001\u0000\u0000"+
		"\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]\u000b\u0001"+
		"\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000_`\u0007\u0000\u0000\u0000"+
		"`\r\u0001\u0000\u0000\u0000ab\u0003\u0010\b\u0000bc\u0003\u000e\u0007"+
		"\u0000cf\u0001\u0000\u0000\u0000df\u0001\u0000\u0000\u0000ea\u0001\u0000"+
		"\u0000\u0000ed\u0001\u0000\u0000\u0000f\u000f\u0001\u0000\u0000\u0000"+
		"gh\u0005\f\u0000\u0000hi\u0005\u001d\u0000\u0000ij\u0005\u0011\u0000\u0000"+
		"jk\u0003\u0014\n\u0000kl\u0005\u0012\u0000\u0000lm\u0003\u0012\t\u0000"+
		"m\u0011\u0001\u0000\u0000\u0000no\u0005\u0013\u0000\u0000oq\u0003\u0004"+
		"\u0002\u0000pr\u0003\u001a\r\u0000qp\u0001\u0000\u0000\u0000rs\u0001\u0000"+
		"\u0000\u0000sq\u0001\u0000\u0000\u0000st\u0001\u0000\u0000\u0000tu\u0001"+
		"\u0000\u0000\u0000uv\u0005\u0014\u0000\u0000v\u0013\u0001\u0000\u0000"+
		"\u0000w|\u0003\u0016\u000b\u0000xy\u0005\u0010\u0000\u0000y{\u0003\u0016"+
		"\u000b\u0000zx\u0001\u0000\u0000\u0000{~\u0001\u0000\u0000\u0000|z\u0001"+
		"\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}\u0081\u0001\u0000\u0000"+
		"\u0000~|\u0001\u0000\u0000\u0000\u007f\u0081\u0001\u0000\u0000\u0000\u0080"+
		"w\u0001\u0000\u0000\u0000\u0080\u007f\u0001\u0000\u0000\u0000\u0081\u0015"+
		"\u0001\u0000\u0000\u0000\u0082\u0083\u0005\u001d\u0000\u0000\u0083\u0084"+
		"\u0005\u000f\u0000\u0000\u0084\u0085\u0003\f\u0006\u0000\u0085\u0017\u0001"+
		"\u0000\u0000\u0000\u0086\u0088\u0005\u0013\u0000\u0000\u0087\u0089\u0003"+
		"\u001a\r\u0000\u0088\u0087\u0001\u0000\u0000\u0000\u0089\u008a\u0001\u0000"+
		"\u0000\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008a\u008b\u0001\u0000"+
		"\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c\u008d\u0005\u0014"+
		"\u0000\u0000\u008d\u0019\u0001\u0000\u0000\u0000\u008e\u0094\u0003\u001c"+
		"\u000e\u0000\u008f\u0094\u0003\u001e\u000f\u0000\u0090\u0094\u0003$\u0012"+
		"\u0000\u0091\u0094\u0003&\u0013\u0000\u0092\u0094\u0003*\u0015\u0000\u0093"+
		"\u008e\u0001\u0000\u0000\u0000\u0093\u008f\u0001\u0000\u0000\u0000\u0093"+
		"\u0090\u0001\u0000\u0000\u0000\u0093\u0091\u0001\u0000\u0000\u0000\u0093"+
		"\u0092\u0001\u0000\u0000\u0000\u0094\u001b\u0001\u0000\u0000\u0000\u0095"+
		"\u0096\u0005\u001d\u0000\u0000\u0096\u0097\u0005\r\u0000\u0000\u0097\u0098"+
		"\u0003.\u0017\u0000\u0098\u0099\u0005\u000e\u0000\u0000\u0099\u001d\u0001"+
		"\u0000\u0000\u0000\u009a\u009b\u0005\u0007\u0000\u0000\u009b\u009c\u0005"+
		"\u0011\u0000\u0000\u009c\u009d\u0003 \u0010\u0000\u009d\u009e\u0005\u0012"+
		"\u0000\u0000\u009e\u009f\u0005\u000e\u0000\u0000\u009f\u001f\u0001\u0000"+
		"\u0000\u0000\u00a0\u00a5\u0003\"\u0011\u0000\u00a1\u00a2\u0005\u0010\u0000"+
		"\u0000\u00a2\u00a4\u0003\"\u0011\u0000\u00a3\u00a1\u0001\u0000\u0000\u0000"+
		"\u00a4\u00a7\u0001\u0000\u0000\u0000\u00a5\u00a3\u0001\u0000\u0000\u0000"+
		"\u00a5\u00a6\u0001\u0000\u0000\u0000\u00a6!\u0001\u0000\u0000\u0000\u00a7"+
		"\u00a5\u0001\u0000\u0000\u0000\u00a8\u00ab\u0003.\u0017\u0000\u00a9\u00ab"+
		"\u0005 \u0000\u0000\u00aa\u00a8\u0001\u0000\u0000\u0000\u00aa\u00a9\u0001"+
		"\u0000\u0000\u0000\u00ab#\u0001\u0000\u0000\u0000\u00ac\u00ad\u0005\b"+
		"\u0000\u0000\u00ad\u00ae\u0005\u0011\u0000\u0000\u00ae\u00af\u0003.\u0017"+
		"\u0000\u00af\u00b0\u0005\u0012\u0000\u0000\u00b0\u00b1\u0005\t\u0000\u0000"+
		"\u00b1\u00b2\u0003\u0018\f\u0000\u00b2%\u0001\u0000\u0000\u0000\u00b3"+
		"\u00b4\u0005\n\u0000\u0000\u00b4\u00b5\u0005\u0011\u0000\u0000\u00b5\u00b6"+
		"\u0003.\u0017\u0000\u00b6\u00b7\u0005\u0012\u0000\u0000\u00b7\u00b8\u0005"+
		"\t\u0000\u0000\u00b8\u00b9\u0003\u0018\f\u0000\u00b9\u00ba\u0003(\u0014"+
		"\u0000\u00ba\'\u0001\u0000\u0000\u0000\u00bb\u00bc\u0005\u000b\u0000\u0000"+
		"\u00bc\u00bd\u0005\t\u0000\u0000\u00bd\u00c0\u0003\u0018\f\u0000\u00be"+
		"\u00c0\u0001\u0000\u0000\u0000\u00bf\u00bb\u0001\u0000\u0000\u0000\u00bf"+
		"\u00be\u0001\u0000\u0000\u0000\u00c0)\u0001\u0000\u0000\u0000\u00c1\u00c2"+
		"\u0005\u001d\u0000\u0000\u00c2\u00c3\u0005\u0011\u0000\u0000\u00c3\u00c4"+
		"\u0003,\u0016\u0000\u00c4\u00c5\u0005\u0012\u0000\u0000\u00c5\u00c6\u0005"+
		"\u000e\u0000\u0000\u00c6+\u0001\u0000\u0000\u0000\u00c7\u00cc\u0003.\u0017"+
		"\u0000\u00c8\u00c9\u0005\u0010\u0000\u0000\u00c9\u00cb\u0003.\u0017\u0000"+
		"\u00ca\u00c8\u0001\u0000\u0000\u0000\u00cb\u00ce\u0001\u0000\u0000\u0000"+
		"\u00cc\u00ca\u0001\u0000\u0000\u0000\u00cc\u00cd\u0001\u0000\u0000\u0000"+
		"\u00cd\u00d1\u0001\u0000\u0000\u0000\u00ce\u00cc\u0001\u0000\u0000\u0000"+
		"\u00cf\u00d1\u0001\u0000\u0000\u0000\u00d0\u00c7\u0001\u0000\u0000\u0000"+
		"\u00d0\u00cf\u0001\u0000\u0000\u0000\u00d1-\u0001\u0000\u0000\u0000\u00d2"+
		"\u00d6\u00032\u0019\u0000\u00d3\u00d4\u00030\u0018\u0000\u00d4\u00d5\u0003"+
		"2\u0019\u0000\u00d5\u00d7\u0001\u0000\u0000\u0000\u00d6\u00d3\u0001\u0000"+
		"\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7/\u0001\u0000\u0000"+
		"\u0000\u00d8\u00d9\u0007\u0001\u0000\u0000\u00d91\u0001\u0000\u0000\u0000"+
		"\u00da\u00df\u00034\u001a\u0000\u00db\u00dc\u0007\u0002\u0000\u0000\u00dc"+
		"\u00de\u00034\u001a\u0000\u00dd\u00db\u0001\u0000\u0000\u0000\u00de\u00e1"+
		"\u0001\u0000\u0000\u0000\u00df\u00dd\u0001\u0000\u0000\u0000\u00df\u00e0"+
		"\u0001\u0000\u0000\u0000\u00e03\u0001\u0000\u0000\u0000\u00e1\u00df\u0001"+
		"\u0000\u0000\u0000\u00e2\u00e7\u00036\u001b\u0000\u00e3\u00e4\u0007\u0003"+
		"\u0000\u0000\u00e4\u00e6\u00036\u001b\u0000\u00e5\u00e3\u0001\u0000\u0000"+
		"\u0000\u00e6\u00e9\u0001\u0000\u0000\u0000\u00e7\u00e5\u0001\u0000\u0000"+
		"\u0000\u00e7\u00e8\u0001\u0000\u0000\u0000\u00e85\u0001\u0000\u0000\u0000"+
		"\u00e9\u00e7\u0001\u0000\u0000\u0000\u00ea\u00eb\u0005\u0011\u0000\u0000"+
		"\u00eb\u00ec\u0003.\u0017\u0000\u00ec\u00ed\u0005\u0012\u0000\u0000\u00ed"+
		"\u00f1\u0001\u0000\u0000\u0000\u00ee\u00f1\u0005\u001d\u0000\u0000\u00ef"+
		"\u00f1\u00038\u001c\u0000\u00f0\u00ea\u0001\u0000\u0000\u0000\u00f0\u00ee"+
		"\u0001\u0000\u0000\u0000\u00f0\u00ef\u0001\u0000\u0000\u0000\u00f17\u0001"+
		"\u0000\u0000\u0000\u00f2\u00f3\u0007\u0004\u0000\u0000\u00f39\u0001\u0000"+
		"\u0000\u0000\u0012KP\\es|\u0080\u008a\u0093\u00a5\u00aa\u00bf\u00cc\u00d0"+
		"\u00d6\u00df\u00e7\u00f0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}