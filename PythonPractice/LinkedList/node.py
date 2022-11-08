

class Node:

    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        self.value = value

    @property
    def next(self):
        return next

    @next.setter
    def next(self, next_node):
        self.next = next_node
