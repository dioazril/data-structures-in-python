class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # Create new Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # Create new Node
        # add Node to end
        pass

    def prepend(self, value):
        # Create new Node
        # add Node to beginning
        pass

    def insert(self, index, value):
        # Create new Node
        # insert Node
        pass


my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
