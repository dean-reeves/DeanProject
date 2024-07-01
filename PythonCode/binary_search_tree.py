# binary_search_tree.py
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

if __name__ == "__main__":
    root = TreeNode(50)
    keys = [30, 20, 40, 70, 60, 80]
    for key in keys:
        root = insert(root, key)
    inorder_traversal(root)
