def printPila(pila):
	print "-------------------"
	while not pila.isEmpty():
		print pila.peek()
		pila.pop()
	print "-------------------"