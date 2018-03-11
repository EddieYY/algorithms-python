
# binary search tree

class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insr(root, node):
    if root is None:
        root=node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insr(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insr(root.r_child, node)
def print_binaryTree(root):
    if root is None:
        return
    print_binaryTree(root.l_child)
    print(root.data)
    print_binaryTree(root.r_child)



r=Node(304)
binary_insr(r, Node(4))
binary_insr(r, Node(11111))
binary_insr(r, Node(33))
print_binaryTree(r)
