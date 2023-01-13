from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:

    # constructor
    def __init__(self) -> None:
        self.data: str = ""
        self.link: Node = None

    # overloaded constructor
    def __init__(self, data:str) -> None:
        self.data = data
        self.link = None
    
    # properties

    # getter
    @property
    def data(self) -> str:
        return self.data

    # setter
    @data.setter
    def data(self, value):
        self.data = value

    # getter
    @property
    def link(self) -> Node:
        return self.link

    # setter
    @link.setter
    def link(self, value):
        self.link = value

