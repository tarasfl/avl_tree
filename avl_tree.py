class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, node, key):

        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        self.balance_tree(node)

        self.root = node
        return node

    def delete(self, node, key):

        if not node:
            return node

        elif key < node.key:
            node.left = self.delete(node.left, key)

        elif key > node.key:
            node.right = self.delete(node.right, key)

        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.get_most_left(node.right)
            node.key = temp.key
            node.right = self.delete(node.right,
                                     temp.val)

        if node is None:
            return node

        self.balance_tree(node)
        return node

    def balance_tree(self, node):
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

    def rotate_left(self, node):

        new_parent = node.right
        left_child = new_parent.left

        new_parent.left = node
        node.right = left_child

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        new_parent.height = 1 + max(self.get_height(new_parent.left),
                           self.get_height(new_parent.right))

        return new_parent

    def rotate_right(self, node):
        new_parent = node.left
        right_child = new_parent.right

        new_parent.right = node
        node.left = right_child

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        new_parent.height = 1 + max(self.get_height(new_parent.left),
                           self.get_height(new_parent.right))

        return new_parent

    def get_height(self, node):
        if not node:
            return 0

        return node.height

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left) - self.get_height(node.right)

    def get_most_left(self, node):
        if node is None or node.left is None:
            return node

        return self.get_most_left(node.left)

    def print_tree(self, node):

        if not node:
            return

        print(node.key)
        self.print_tree(node.left)
        self.print_tree(node.right)

