class Stack:
    """(LIFO) queuing policy implemented using python list."""

    def __init__(self):
        self.list = []

    def push(self, item):
        """Push 'item' onto the stack."""
        self.list.append(item)

    def pop(self):
        """Pop the most recently pushed item from the stack."""
        return self.list.pop()

    def top(self):
        """Return the last element."""
        return self.list[-1]

    def is_empty(self):
        """Returns true if the stack is empty."""
        return len(self.list) == 0


def depth_first_search(graph, start):
    stack = Stack()
    stack.push(start)
    path = []

    while not stack.is_empty():
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.push(neighbor)

    return path


def main():
    adjacency_matrix = {
        1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [6],
        5: [6],
        6: [7],
        7: []
    }
    dfs_path = depth_first_search(adjacency_matrix, 1)
    print(dfs_path)


if __name__ == '__main__':
    main()
