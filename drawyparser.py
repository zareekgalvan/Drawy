"""



"""

import ply.yacc as yacc
import sys


# Importar token del lexer
from drawylex import tokens

# Funcion que encapsula todo el codigo, funcion principal del lenguaje
def p_program(p):
	'''program : vars func main'''
	p[0] = "PROGRAM COMPILED"

# Funcion que define la declaracion de variables
def p_vars(p):
	'''vars : var_type ID SEMICOLON more_vars'''

# Funcion complementaria de declaracion de variables
def p_more_vars(p):
	'''more_vars : vars 
			|'''

# Funcion de tipos de variables
def p_var_type(p):
	'''var_type : INT
			| DOUBLE
			| BOOL
			| INTLIST
			| DOUBLELIST'''

# Funcion para declaracion de funciones
def p_func(p):
	'''func : FUNC func_type ID LPAR pars RPAR func_block'''

# Funcion para declarar el tipo de funcion
def p_func_type(p):
	'''func_type : INT 
			| DOUBLE
			| BOOL
			| VOID'''

# Funcion para la declaracion de parametros dentro de una funcion
def p_pars(p):
	'''pars : pars_comp 
			|'''

# Funcion para declarar al menos un parametro
def p_pars_comp(p):
	'''pars_comp : var_type ID more_pars'''

# Funcion para declarar mas parametros adicionales
def p_more_pars(p):
	'''more_pars : COMMA pars_comp more_pars
			|'''

# Funcion del bloque dentro de una funcion
def p_func_block(p):
	'''func_block : LBRACKET more_vars more_statements RETURN ID SEMICOLON RBRACKET'''

# Funcion
def p_more_statements(p):
	'''more_statements : statement
			|'''

# Funcion
def p_statement(p):
	'''statement : statement_comp more_statements'''

# Funcion
def p_statement_comp(p):
	'''statement_comp : assignation
			| condition
			| cycle
			| read
			| write
			| function'''

# Funcion
def p_assignation(p):
	'''assignation : ID EQUALS expression SEMICOLON'''

# Funcion
def p_condition(p):
	'''condition : IF LPAR expression RPAR block condition_comp'''

# Funcion
def p_condition_comp(p):
	'''condition_comp : ELSE block
			|'''

# Funcion 
def p_cycle(p):
	'''cycle : WHILE LPAR expression RPAR block'''

# Funcion
def p_read(p):
	'''read : READ LPAR var_cte RPAR SEMICOLON'''

# Funcion
def p_write(p):
	'''write : WRITE LPAR var_comp RPAR SEMICOLON'''

# Funcion
def p_var_comp(p):
	'''var_comp : function
			| var_cte'''

# Funcion
def p_function(p):
	'''function : ID LPAR var_comp var_more RPAR SEMICOLON'''

# Funcion
def p_var_more(p):
	'''var_more : COMMA var_comp var_more
			|'''

# Funcion
def p_expression(p):
	'''expression : comp expression_comp'''

# Funcion
def p_expression_comp(p):
	'''expression_comp : andor comp
			|'''

# Funcion
def p_andor(p):
	'''andor : AND
			| OR'''

# Funcion
def p_comp(p):
	'''comp : exp exp_comp'''

# Funcion
def p_exp_comp(p):
	'''exp_comp : comparator exp
			|'''

# Funcion
def p_comparator(p):
	'''comparator : GREATER
			| FEWER
			| GREATEROREQUAL
			| FEWEROREQUAL
			| DIFFERENT
			| EQUALEQUALS'''

# Funcion
def p_exp(p):
	'''exp : term more_term'''

# Funcion
def p_more_term(p):
	'''more_term : operator exp
			|'''

# Funcion
def p_operator(p):
	'''operator : PLUS
			| MINUS'''

# Funcion
def p_term(p):
	'''term : factor more_factor'''

# Funcion
def p_more_factor(p):
	'''more_factor : multiplier term
			|'''

# Funcion
def p_multiplier(p):
	'''multiplier : MULTIPLICATION
			| DIVISION'''

# Funcion
def p_factor(p):
	'''factor : LPAR exp RPAR
			| var_cte'''

# Funcion
def p_var_cte(p):
	'''var_cte : CTEINT
			| CTEDOUBLE
			| ID'''

# Funcion
def p_block(p):
	'''block : LBRACKET more_statements RBRACKET'''

# Funcion
def p_main(p):
	'''main : MAIN block'''










