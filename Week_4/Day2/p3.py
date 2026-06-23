# BST Rule

# In a Binary Search Tree (BST), every node follows this rule:

# Values smaller than the node are stored in its left subtree.
# Values greater than the node are stored in its right subtree.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    if node is None:
        return TreeNode(data)

    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)

    return node

# Inorder Traversal (Print in sorted order)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

# Create BST
values = [8, 3, 10, 1, 6, 14]

root = None
for value in values:
    root = insert(root, value)

# Print BST in sorted order
print("Inorder Traversal:")
inorder(root)