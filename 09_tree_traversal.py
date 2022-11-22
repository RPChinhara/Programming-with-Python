# Design a class that accommodates all the Tree traversal types (Inorder, Preorder, Postorder)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.val, end=" ")
            self.inOrder(root.right)

    def preOrder(self, root):
        if root:
            print(root.val, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.val, end=" ")


root = Node(1)
root.left = Node(2)  # type: ignore
root.right = Node(3)  # type: ignore
root.left.left = Node(4)  # type: ignore
root.left.right = Node(5)  # type: ignore

print("InOrder Traversal: ")
root.inOrder(root)
print("\n")

print("PreOrder Traversal: ")
root.preOrder(root)
print("\n")

print("PostOrder Traversal: ")
root.postOrder(root)
print("\n")