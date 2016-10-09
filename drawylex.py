"""
Analizador lexico DRAWY

César Armando Galván Valles		A00814038
Ángel David Gonzalez Galván		A011

"""

import ply.lex as lex

# Lista de palabras reservadas

reserved = {
	'int' : 'INT'
	'double' : 'DOUBLE'
	'bool' : 'BOOL'
	'intList' : 'INTLIST'
	'doubleList' : 'DOUBLELIST'
	'void' : 'VOID'
	'if' : 'IF'
	'else' : 'ELSE'
	'while' : 'WHILE'
	'read' : 'READ'
	'write' : 'WRITE'
	'true' : 'TRUE'
	'false' : 'FALSE'
	'main' : 'MAIN'
	'drawCirle' : 'DRAWCIRCLE'
	'drawSquare' : 'DRAWSQUARE'
	'drawRectangle' : 'DRAWRECTANGLE'
	'drawLine' : 'DRAWLINE'
	'drawArc' : 'DRAWARC'
	'moveFigure' : 'MOVEFIGURE'
	'rotateFigure' : 'ROTATEFIGURE'
	'changeThickness' : 'CHANGETHICKNESS'
	'changeColor' : 'CHANGECOLOR'
	'scaleUp' : 'SCALEUP'
	'scaleDown' : 'SCALEDOWN'
	'erase' : 'ERASE'
	'append' : 'APPEND'
	'prepend' : 'PREPEND'
	'addAt' : 'ADDAT'
	'removeFirst' : 'REMOVEFIRST'
	'removeLast' : 'REMOVELAST'
	'removeAt' : 'REMOVEAT'
	'thin' : 'THIN'
	'medium' : 'MEDIUM'
	'thick' : 'THICK'
	'red' : 'RED'
	'blue' : 'BLUE'
	'green' : 'GREEN'
	'yellow' : 'YELLOW'
	'black' : 'BLACK'
	'purple' : 'PURPLE'
	'orange' : 'ORANGE'
	'func' : 'FUNC'
	'return' : 'RETURN'
}

# Lista de tokens

tokens = ['PLUS', 'MINUS', 'MULTIPLICATION', 'DIVISION', 'MOD', 'EQUALS', 
			'EQUALEQUALS', 'DIFFERENT', 'GREATER', 'FEWER', 
			'GREATEROREQUAL', 'FEWEROREQUAL', 'AND', 'OR', 'LPAR', 'RPAR', 
			'LBRACKET', 'RBRACKET', 'COMMA', 'SEMICOLON', 'CTEINT', 
			'CTEDOUBLE', 'CTESTRING'] + list(reserved.values())

# Expresiones regulares

t_ignore = '\t'
t_CTEINT = r'-?[0-9]+'
t_CTEDOUBLE = r'-?[0-9]+\.[0-9]+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'/'
t_MOD = r'%'
t_COMMA = r','
t_SEMICOLON = r';'
t_EQUALS = r'='
t_EQUALSEQUALS = r'=='
t_DIFFERENT = r'<>'
t_GREATER = r'>'
t_FEWER = r'<'
t_GREATEROREQUAL = r'>='
t_FEWEROREQUAL = r'<='
t_AND = r'&&'
t_OR = r'||'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRACKET = r'{'
t_RBRACKET = r'}'

# Expresion regular para los IDs

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = reserved.get(t.value, 'ID')
	return t

# Expresion regular para las constantes tipo string

def t_CTESTRING(t):  
  r'\".*\"'
  return t

# Identificar saltos de linea y llevar conteo de la linea actual

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Manejo de errores de lexico

def t_error(t):
	print("Error de lexico %s" % t.value[0])
	exit(-1)
	t.lexer.skip(1)

# Comentarios estilo C++

def t_comment(t):
    r'//.*\n'
    t.lexer.lineno += 1
    return t

# Crear el analizador de lexico

lexer = lex.lex()