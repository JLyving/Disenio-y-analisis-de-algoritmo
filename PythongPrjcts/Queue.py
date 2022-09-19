from Node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.end = None
        self.size = 0

    def insertfin(self, e):
        new_node = Node(e)
        if self.first == None:
            self.first = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node
        self.size += 1

    def removeini(self):
        if self.first == None:
            return None
        e = self.first.elem
        self.first = self.first.next
        self.size -= 1
        return print(e)

    def tamanio(self):
        return print(self.size)

    def esvacia(self):
        return print(self.size == 0)

    def primero(self):
        if self.first == None:
            return None
        else:
            return print(self.first.elem)
