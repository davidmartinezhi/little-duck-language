grammar little_duck;

/* Parser Rules */
programa
    : PROGRAMA ID SEMI vars funcs INICIO cuerpo FIN
    ;

vars
    : VARS LBRACE var_decl_list RBRACE
    |   /* empty */
    ;

var_decl_list
    : var_decl+
    ;

var_decl
    : id_list COLON tipo SEMI
    ;

id_list
    : ID (COMMA ID)*
    ;

tipo
    : ENTERO
    | FLOTANTE
    ;

funcs
    : func_decl funcs
    |   /* empty */
    ;

func_decl
    : FUNC ID LPAREN param_list RPAREN cuerpo
    ;

param_list
    : param (COMMA param)*
    |   /* empty */
    ;

param
    : ID COLON tipo
    ;

cuerpo
    : LBRACE estatuto+ RBRACE
    ;

estatuto
    : asigna
    | imprime
    | ciclo
    | condicion
    | llamada
    ;

asigna
    : ID ASSIGN expresion SEMI
    ;

imprime
    : ESCRIBE LPAREN print_list RPAREN SEMI
    ;

print_list
    : print_item (COMMA print_item)*
    ;

print_item
    : expresion
    | STRING_LITERAL
    ;

ciclo
    : MIENTRAS LPAREN expresion RPAREN HAZ cuerpo
    ;

condicion
    : SI LPAREN expresion RPAREN HAZ cuerpo condicion_else
    ;

condicion_else
    : SINO HAZ cuerpo
    |   /* empty */
    ;

llamada
    : ID LPAREN arg_list RPAREN SEMI
    ;

arg_list
    : expresion (COMMA expresion)*
    |   /* empty */
    ;

expresion
    : exp (op_comparacion exp)?
    ;

op_comparacion
    : GT
    | LT
    | NEQ
    | EQ
    ;

exp
    : termino ((PLUS | MINUS) termino)*
    ;

termino
    : factor ((MULT | DIV) factor)*
    ;

factor
    : LPAREN expresion RPAREN
    | ID
    | cte
    ;

cte
    : CTE_FLOT
    | CTE_ENT
    ;

/* Lexer Rules */
PROGRAMA   : 'programa';
VARS       : 'vars';
INICIO     : 'inicio';
FIN        : 'fin';
ENTERO     : 'entero';
FLOTANTE   : 'flotante';
ESCRIBE    : 'escribe';
MIENTRAS   : 'mientras';
HAZ        : 'haz';
SI         : 'si';
SINO       : 'sino';
FUNC       : 'func';

ASSIGN     : '=';
SEMI       : ';';
COLON      : ':';
COMMA      : ',';
LPAREN     : '(';
RPAREN     : ')';
LBRACE     : '{';
RBRACE     : '}';
PLUS       : '+';
MINUS      : '-';
MULT       : '*';
DIV        : '/';
GT         : '>';
LT         : '<';
NEQ        : '!=';
EQ         : '==';

ID
    : [a-zA-Z][a-zA-Z0-9_]*
    ;

CTE_ENT
    : [0-9]+
    ;

CTE_FLOT
    : [0-9]+ '.' [0-9]+
    ;

STRING_LITERAL
    : '"' ~["\r\n]* '"'
    ;

/* Whitespace and Comments */
WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '//' ~[\r\n]* -> skip
    ;