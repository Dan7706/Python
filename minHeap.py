#https://github.com/Dan7706
#Implementing min heap data strucure using python list in wrapper class.



class MinHeap:
    def __init__(self, items=None):
        super().__init__()
        if items is None:
            items = []
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self._floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self._floatUp(len(self.heap) - 1)

    def peek(self):
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self._swap(1, len(self.heap) - 1)
            min_value = self.heap.pop()
            self._bubbleDown(1)
        elif len(self.heap) == 2:
            min_value = self.heap.pop()
        else:
            return False
        return min_value

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] < self.heap[parent]:
            self._swap(index, parent)
            self._floatUp(parent)

    def _bubbleDown(self, index):
        left_node = index * 2
        right_node = index * 2 + 1
        smallest_value = index
        if len(self.heap) > left_node and self.heap[smallest_value] > self.heap[left_node]:
            smallest = left
        if len(self.heap) > right_node and self.heap[smallest_value] > self.heap[right_node]:
            smallest_value = right_node
        if smallest_value != index:
            self._swap(index, smallest_value)
            self._bubbleDown(smallest_value)

    def __str__(self):
        return str(self.heap)



