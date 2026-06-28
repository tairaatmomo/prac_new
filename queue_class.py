class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        
        return self.items.pop(0)
    
    def front(self):
            if len(self.items) == 0:
                return None
            
            return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def rear(self):
        if len(self.items) == 0:
            return None
        
        return self.items[-1]
