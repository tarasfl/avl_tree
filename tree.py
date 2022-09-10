class Node:

    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key
        self.height = 1


class Tree:

    def __init__(self):
        self.root = None

    def delete(self, key, node):
        if node is not None:
            if key < node.key:
                self.delete(key, node.left)
            elif key > node.key:
                self.delete(key, node.right)
            else:
                if node.left is None:
                    buffer = node.right
                    root = None
                    return buffer

                elif node.right is None:
                    buffer = node.left
                    root = None
                    return buffer

                buffer = tree.get_most_left(node.right)
                node.key = buffer.key
                self.delete(buffer.key, node.right)

            node.height = 1 + max(self.get_height(node.left),
                                  self.get_most_left(node.right))

            balance = self.get_balance(node)

            if balance > 1 and self.get_balance(node.left) >= 0:
                return self.rotate_right(node)

            if balance < -1 and self.get_balance(node.right) <= 0:
                return self.rotate_left(node)

                # Case 3 - Left Right
            if balance > 1 and self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

                # Case 4 - Right Left
            if balance < -1 and self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

            return node

    def get_most_left(self, node):
        if node is None or node.left is None:
            return node

        return self.get_most_left(node.left)

    @staticmethod
    def get_height(node):
        if node is None:
            return 0
        return node.height

    @staticmethod
    def get_balance(node):
        if node is None:
            return 0
        return Tree.get_height(node.left) - Tree.get_height(node.right)

    @staticmethod
    def rotate_left(node):

        if node.right is not None:
            new_parent = node.right
            node.right = new_parent.left
            new_parent.left = node
            return new_parent

    @staticmethod
    def rotate_right(node):

        if node.left is not None:
            new_parent = node.left
            node.left = new_parent.right
            new_parent.right = node
            return new_parent


if __name__ == '__main__':
    tree = Tree()
    node10 = tree.root = Node(10)
    node8 = tree.root.left = Node(8)

    tree.delete(10, tree.root)

    print(tree.root.left.key)
