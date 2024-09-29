class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if not node.right:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
    
    def inorder_traversal(self, node, elements):
        if node:
            self.inorder_traversal(node.left, elements)
            elements.append(node.data)
            self.inorder_traversal(node.right, elements)
    
    def display(self):
        elements = []
        self.inorder_traversal(self.root, elements)
        return elements

# Test binary tree implementation
binary_tree = BinaryTree()
binary_tree.insert(50)
binary_tree.insert(30)
binary_tree.insert(70)
binary_tree.insert(20)
binary_tree.insert(40)
binary_tree.insert(60)
binary_tree.insert(80)
print("Inorder traversal of the binary tree:", binary_tree.display())  # [20, 30, 40, 50, 60, 70, 80]
