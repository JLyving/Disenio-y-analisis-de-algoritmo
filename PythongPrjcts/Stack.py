from Node import Node


class Stack:
    def __init__(self):
        self.end = None
        self.size = 0

    def Push(self, e):
        new_node = Node(e)
        if self.end == None:
            self.end = new_node
        else:
            new_node.next = self.end
            self.end = new_node
        self.size += 1

    def Pop(self):
        if self.end == None:
            return None
        e = self.end.elem
        self.end = self.end.next
        self.size -= 1
        return print(e)

    def esvacia(self):
        return print(self.size == 0)

    def tamanio(self):
        return print(self.size)

    def ultimo(self):
        if self.end == None:
            return None
        else:
            return print(self.end.elem)
