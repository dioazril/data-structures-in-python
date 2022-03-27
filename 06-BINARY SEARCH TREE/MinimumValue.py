class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.counter = 1
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        contain = value
        while temp is not None:
            if contain < temp.value:
                temp = temp.left
            elif contain > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value(self, current_node):
        while current_node.left is not None:
            self.counter += 1
            current_node = current_node.left
        print(self.counter)
        # return current_node.value


binary_search_tree = BinarySearchTree()
binary_search_tree.insert(3)
binary_search_tree.insert(9)
binary_search_tree.insert(20)
# print(binary_search_tree.contains(18))
# print(binary_search_tree.contains(11))
print(binary_search_tree.min_value(binary_search_tree.root))
print(binary_search_tree.min_value(binary_search_tree.root.right))
