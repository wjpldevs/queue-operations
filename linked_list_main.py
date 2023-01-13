from node import Node

class NodeTest():

    @property
    def first(self) -> Node:
        return self.first

    @first.setter
    def first(self, value):
        self.first = value

    @property
    def aux1(self) -> Node:
        return self.aux1

    @aux1.setter
    def aux1(self, value):
        self.aux1 = value

    @property
    def aux2(self) -> Node:
        return self.aux2

    @aux2.setter
    def aux2(self, value):
        self.aux2 = value

    @property
    def quantity(self) -> int:
        return self.quantity

    @quantity.setter
    def quantity(self, value):
        self.quantity = value
    
    def __init__(self) -> None:
        self.first: Node = None
        self.aux1: Node = None
        self.aux2: Node = None
        self.quantity = 0

    def is_empty(self) -> None:
        if self.fist == None:
            print("List is empty")
        else:
            print("List contains some data")

    def loop(self) -> None:
        aux = self.first

        while (aux != None):
            print(f"{aux.data}")
            aux = aux.link

    def insert_start(self, data):
        new = Node(data)

        new.link = self.first
        self.first = new

        self.quantity = self.quantity + 1

    def insert_end(self, data):
        aux = self.first

        while aux.link != None:
            aux = aux.link

        new = Node(data)
        new.link = None
        aux.link = new

        self.quantity = self.quantity + 1

    


    