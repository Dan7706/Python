class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self):
        return ('(' + str(self.data) + ')')



class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def find(self, data):
        this_node = self.root
        while this_node is not None:
            if this_node.data == data:
                return data
            else:
                this_node = this_node.next
        return None

    def remove(self, data):
        this_node = self.root
        prev_node = None
        while this_node is not None:
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next = this_node.next
                else:
                    self.root = this_node.next
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next
        return False

    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node, end="->")
            this_node = this_node.next
        print(None)


ll = LinkedList()
ll.add(33)
ll.add(44)
ll.add(55)
ll.print_list()
print("Found: ", ll.find(44))
print("Removed: ",ll.remove(44))
print("Found: ", ll.find(44))
ll.print_list()
