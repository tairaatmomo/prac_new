class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def clear(self):
        self.elements.clear()

    def top(self):
        if self.is_empty():
            return None
        return self.elements[-1]
    
    def min(self):
        return min(self.elements)
    
    def max(self):
        return max(self.elements)
