from Queue import Queue
from Stack import Stack

cola1 = Queue()
pila1 = Stack()

cola1.esvacia()
cola1.insertfin(6)
cola1.insertfin(5)
cola1.insertfin(4)
cola1.esvacia()
cola1.tamanio()
cola1.primero()
cola1.removeini()
cola1.esvacia()
cola1.tamanio()
cola1.primero()

print("-----------------")

pila1.esvacia()
pila1.Push(10)
pila1.Push(11)
pila1.Push(12)
pila1.esvacia()
pila1.tamanio()
pila1.ultimo()
pila1.Pop()
pila1.esvacia()
pila1.tamanio()
pila1.ultimo()
