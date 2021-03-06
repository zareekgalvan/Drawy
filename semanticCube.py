"""
------------------------------------------------------------
Cubo semantico DRAWY

Cesar Armando Galvan Valles	A00814038
Angel David Gonzalez Galvan	A01137638

Correr en terminal:
$	python drawylex.py
$	python drawyparser.py test/test1.txt

*cambiar el filename a otros archivos de prueba
------------------------------------------------------------
"""

# Cubo semantico que define las operaciones que pueden realizarse y el valor de retorno que generan
semanticCube = {
	"int" : {
		"int" : {
			"+" : "int",
			"-" : "int",
			"*" : "int",
			"/" : "int",
			"%" : "int",
			"=" : "int",
			"==" : "bool",
			"<>" : "bool",
			">" : "bool",
			"<" : "bool",
			">=" : "bool",
			"<=" : "bool",
			"&&" : "ERROR",
			"||" : "ERROR"
		},
		"double" : {
			"+" : "double",
			"-" : "double",
			"*" : "double",
			"/" : "double",
			"%" : "double",
			"=" : "double",
			"==" : "bool",
			"<>" : "bool",
			">" : "bool",
			"<" : "bool",
			">=" : "bool",
			"<=" : "bool",
			"&&" : "",
			"||" : ""
		},
		"bool" : {
			"+" : "ERROR",
			"-" : "ERROR",
			"*" : "ERROR",
			"/" : "ERROR",
			"%" : "ERROR",
			"=" : "ERROR",
			"==" : "ERROR",
			"<>" : "ERROR",
			">" : "ERROR",
			"<" : "ERROR",
			">=" : "ERROR",
			"<=" : "ERROR",
			"&&" : "ERROR",
			"||" : "ERROR"
		}
	},
	"double" : {
		"int" : {
			"+" : "double",
			"-" : "double",
			"*" : "double",
			"/" : "double",
			"%" : "double",
			"=" : "double",
			"==" : "bool",
			"<>" : "bool",
			">" : "bool",
			"<" : "bool",
			">=" : "bool",
			"<=" : "bool",
			"&&" : "ERROR",
			"||" : "ERROR"
		},
		"double" : {
			"+" : "double",
			"-" : "double",
			"*" : "double",
			"/" : "double",
			"%" : "double",
			"=" : "double",
			"==" : "bool",
			"<>" : "bool",
			">" : "bool",
			"<" : "bool",
			">=" : "bool",
			"<=" : "bool",
			"&&" : "ERROR",
			"||" : "ERROR"
		},
		"bool" : {
			"+" : "ERROR",
			"-" : "ERROR",
			"*" : "ERROR",
			"/" : "ERROR",
			"%" : "ERROR",
			"=" : "ERROR",
			"==" : "ERROR",
			"<>" : "ERROR",
			">" : "ERROR",
			"<" : "ERROR",
			">=" : "ERROR",
			"<=" : "ERROR",
			"&&" : "ERROR",
			"||" : "ERROR"
		}
	},
	"bool" : {
		"int" : {
			"+" : "ERROR",
			"-" : "ERROR",
			"*" : "ERROR",
			"/" : "ERROR",
			"%" : "ERROR",
			"=" : "ERROR",
			"==" : "ERROR",
			"<>" : "ERROR",
			">" : "ERROR",
			"<" : "ERROR",
			">=" : "ERROR",
			"<=" : "ERROR",
			"&&" : "ERROR",
			"||" : "ERROR"
		},
		"double" : {
			"+" : "ERROR",
			"-" : "ERROR",
			"*" : "ERROR",
			"/" : "ERROR",
			"%" : "ERROR",
			"=" : "ERROR",
			"==" : "ERROR",
			"<>" : "ERROR",
			">" : "ERROR",
			"<" : "ERROR",
			">=" : "ERROR",
			"<=" : "ERROR",
			"&&" : "ERROR",
			"||" : "ERROR"
		},
		"bool" : {
			"+" : "ERROR",
			"-" : "ERROR",
			"*" : "ERROR",
			"/" : "ERROR",
			"%" : "ERROR",
			"=" : "ERROR",
			"==" : "bool",
			"<>" : "bool",
			">" : "ERROR",
			"<" : "ERROR",
			">=" : "ERROR",
			"<=" : "ERROR",
			"&&" : "bool",
			"||" : "bool"
		}
	}
}

def getTypeSC(op1, op2, oper):
	return semanticCube[op1][op2][oper]

# Probar que este declarado correctamente el cubo semantico

def printSemanticCube():
	for key in semanticCube:
		for  key2 in semanticCube[key]:
			print semanticCube[key][key2]
