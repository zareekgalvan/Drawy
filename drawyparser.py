"""
------------------------------------------------------------
Analizador sintactico DRAWY

Cesar Armando Galvan Valles	A00814038
Angel David Gonzalez Galvan	A01137638

Correr en terminal:
$	python drawylex.py
$	python drawyparser.py test/test1.txt

*cambiar el filename a otros archivos de prueba
------------------------------------------------------------
"""

import ply.yacc as yacc
import sys
from sets import Set


# Importar token del lexer
from drawylex import tokens
# Directorio de procedimientos
dirProcedures = {}
dirProcedures["global"] = {}
varTableGlobal = {}
varTableGlobal["global"] = {}
ids = set()
global scope 
scope = ['global']
tipo = None


# Funcion que encapsula todo el codigo, funcion principal del lenguaje
def p_program(p):
	'''program : more_vars more_func main'''
	p[0] = "PROGRAM COMPILED"

# Funcion que define la declaracion de variables
def p_vars(p):
	'''vars : var_type to_actual_type ID to_var_table SEMICOLON vars
			|'''
# Funcion
def p_to_ids_set(p):
	'''to_ids_set :'''


#
def p_to_actual_type(p):
	'''to_actual_type :'''
	#print p[-1]
	global tipo
	tipo = p[-1]
	#print actualtype

# Funcion para agregar al directorio de funciones la variable y su tipo
def p_to_var_table(p):
	'''to_var_table :'''
	#print p[-1]
	varid = p[-1]
	print varid
	if varid not in varTableGlobal['global']:
		ids.add(varid)
		varTableGlobal[scope[len(scope)-1]][varid]  = tipo
	else:
		print('Variable "%s" already registered' % (varid))
		sys.exit() 
	#print dirProcedures[scope[len(scope)-1]]

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
	p[0] = p[1]

# Funcion para declaracion de funciones
def p_func(p):
	'''func : FUNC func_type ID procedure_name LPAR pars RPAR func_block more_func'''

# Funcion para declarar el tipo de funcion
def p_func_type(p):
	'''func_type : INT 
			| DOUBLE
			| BOOL
			| VOID'''

# Funcion para insertar en el directorio de funciones el nombre de la funcion
def p_procedure_name(p):
	'''procedure_name :'''
	funcname = p[-1]
	scope.append(p[-1])
	ids.add(p[-1])
	print scope[len(scope)-1]
	varTableGlobal[funcname] = {}

# Funcion para la declaracion de parametros dentro de una funcion
def p_pars(p):
	'''pars : pars_comp 
			|'''

# Funcion para declarar al menos un parametro
def p_pars_comp(p):
	'''pars_comp : var_type ID to_var_table more_pars'''

# Funcion para declarar mas parametros adicionales
def p_more_pars(p):
	'''more_pars : COMMA pars_comp 
			|'''

# Funcion del bloque dentro de una funcion
def p_func_block(p):
	'''func_block : LBRACKET more_vars more_statements RETURN var_cte SEMICOLON RBRACKET
			|'''

def p_more_func(p):
	'''more_func : func
			|'''

# Funcion para mas estatutos o ninguno
def p_more_statements(p):
	'''more_statements : statement
			|'''

# Funcion de estatutos
def p_statement(p):
	'''statement : statement_comp more_statements'''

# Funcion complementaria de estatutos
def p_statement_comp(p):
	'''statement_comp : assignation
			| condition
			| cycle
			| read
			| write
			| function'''

# Funcion de asignacion de un valor a una variable
def p_assignation(p):
	'''assignation : ID EQUALS expression SEMICOLON'''

# Funcion de condicion, if else
def p_condition(p):
	'''condition : IF LPAR expression RPAR block condition_comp'''

# Funcion complementaria de condicion
def p_condition_comp(p):
	'''condition_comp : ELSE block
			|'''

# Funcion de ciclo, where
def p_cycle(p):
	'''cycle : WHILE LPAR expression RPAR block'''

# Funcion de lectura de una variable
def p_read(p):
	'''read : READ LPAR var_cte RPAR SEMICOLON'''

# Funcion  de escritura de una argumento
def p_write(p):
	'''write : WRITE LPAR var_comp RPAR SEMICOLON'''

# Funcion
def p_var_comp(p):
	'''var_comp : function_call
			| var_cte'''

# Funcion
def p_function(p):
	'''function : ID LPAR func_params RPAR SEMICOLON'''

# Funcion
def p_func_params(p):
	'''func_params : var_comp var_more
			|'''

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
			| ID
			| cte_bool
			| function_call'''

# Funcion
def p_cte_bool(p):
	'''cte_bool : TRUE
			| FALSE'''

# Funcion
def p_block(p):
	'''block : LBRACKET more_statements RBRACKET'''

# Funcion
def p_main(p):
	'''main : MAIN procedure_name main_block'''

# Funcion
def p_main_block(p):
	'''main_block : LBRACKET more_vars more_statements RBRACKET'''

# Funcion para la llamada de una funcion
def p_function_call(p):
	'''function_call : ID LPAR func_params RPAR'''

# Funcion de error de sintaxis
def p_error(p):
    print('Syntax error in token %s with value \"%s\" in line %s' % (p.type, p.value, p.lineno))
    sys.exit()


# Construir el parser
drawyparser = yacc.yacc()


# Programa Main
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		file = sys.argv[1]
		# Abre el archivo, almacena su informacion y lo cierra
		try:
			f = open(file,'r')
			data = f.read()
			# print data
			f.close()
			# Parsear el contenido
			
			if (drawyparser.parse(data, tracking=True) == 'PROGRAM COMPILED'):
				print varTableGlobal
				print ids
				print "Valid syntax"
				
		except EOFError:
	   		print(EOFError)
	else:
		print('File missing')





