# A Tree is a data structure where data is arranged in a hierarchical structure.
# The topmost node is called the root.A tree normally has one root.
# A node directly above another node is its parent. A node directly below another node is its child.
# A node having no children is called a leaf node.
# Edge

# The connection between two nodes is called an edge.

# A
# |
# B

# The line between A and B is an edge.
# shibling - having same parent node is called sibling.

# depth - The depth of a node is the number of edges from the root to the node Depth: Root se kisi node tak kitne edges hain.
# height - The height of a node is the number of edges on the longest path from the node to a leaf.Height: Kisi node se neeche deepest leaf tak kitne edges hain.

# Binary Tree: A tree in which each node can have at most two children is called a binary tree.

# importand tree traversals are:
# 1. Inorder Traversal (Left, Root, Right)
# 2. Preorder Traversal (Root, Left, Right)
# 3. Postorder Traversal (Left, Right, Root)
# 4. Level Order Traversal (Breadth First Traversal)

#create class of a TreeNode of a Binary Tree.# 2. Preorder Traversal (Root, Left, Right)


# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# rootNode = TreeNode(1)
# rootNode.left = TreeNode(2)
# rootNode.right = TreeNode(3)

# def preorderTraversal(root):
#     if root is None:
#         return
#     print(root.data)
#     preorderTraversal(root.left)
#     preorderTraversal(root.right)
# preorderTraversal(rootNode)

# 1. Inorder Traversal (Left, Root, Right)

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# rootNode = TreeNode(1)
# rootNode.left = TreeNode(2)
# rootNode.right = TreeNode(3)

# def inorderTraversal(root):
#     if root is None:
#         return
#     inorderTraversal(root.left)
#     print(root.data)
#     inorderTraversal(root.right)
# inorderTraversal(rootNode)

# 3. Postorder Traversal (Left, Right, Root)
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# rootNode = TreeNode(1)
# rootNode.left = TreeNode(2)
# rootNode.right = TreeNode(3)

# def postorderTraversal(root):
#     if root is None:
#         return
#     postorderTraversal(root.left)
#     postorderTraversal(root.right)
#     print(root.data)
# postorderTraversal(rootNode)

# Count nodes in a Binary tree. Root is given as parameter.

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# rootNode = TreeNode(1)
# rootNode.left = TreeNode(2)
# rootNode.right = TreeNode(3)

# def countNodes(root):
#     if root is None:
#         return 0
#     return 1 + countNodes(root.left) + countNodes(root.right)
# print(countNodes(rootNode))

# WAP to find sum of all of the nodes of a binary tree, havnig root as the paramter. 

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# rootNode = TreeNode(1)
# rootNode.left = TreeNode(2)
# rootNode.right = TreeNode(3)


# def sumOfNodes(root):
#     if root is None:
#         return 0
#     return root.data + sumOfNodes(root.left) + sumOfNodes(root.right)

# print(sumOfNodes(rootNode))

# find maximum value in a binary tree.

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# rootNode = TreeNode(1)
# rootNode.left = TreeNode(2)
# rootNode.right = TreeNode(3)

# def findMax(root):
#     if root is None:
#         return float('-inf')
#     left_max = findMax(root.left)
#     right_max = findMax(root.right)
#     return max(root.data, left_max, right_max)

# print(findMax(rootNode))
