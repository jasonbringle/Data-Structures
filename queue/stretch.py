from stack import Stack

class StackQueue:
    def __init__(self):
        self.size = 0
        self.storage_en = Stack()
        self.storage_de = Stack()

    def __len__(self):
        return self.size
        
    def enqueue(self, value):
        self.storage_en.push(value)

    def dequeue(self):
        if len(self.storage_en) == 0:
            return None
        else:
            while len(self.storage_en) > 0:
                latest = self.storage_en.push()
                self.storage_de.pop(latest)
            return self.storage_de.pop()
        self.size -=1


stackQueue = StackQueue()

stackQueue.enqueue(23)

print(stackQueue.size)