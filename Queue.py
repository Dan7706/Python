class Queue:
    def __init__(self):
        self.queue = list()


    def isEmpty(self):
        return len(self.queue) == 0


    def enqueue(self, item):
        self.queue.insert(0,item)


    def dequeue(self):
        return self.queue.pop()


    def size(self):
        return len(self.queue)
