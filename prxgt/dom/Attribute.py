__author__ = 'Alex Gusev <alex@flancer64.com>'


class Attribute:
    """In-memory model for one attribute"""
    name = None
    type = None

    def __repr__(self):
        return "[" + self.name + "@" + self.type + "]"