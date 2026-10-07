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

# WAP to find height of a binary tree. Height of a binary tree is the number of edges on the longest path from the root to a leaf node.
# class TreeNode:
#   def __init__(self, data):
#     self.value=data
#     self.left=None
#     self.right=None

# root =TreeNode(1)
# root.left=TreeNode(2)
# root.left.left=TreeNode(3)

# def nodeHeight(node):
#     if node is None:
#         return -1
#     return 1 + max(nodeHeight(node.left), nodeHeight(node.right))
# print(nodeHeight(root))

# WAP for Level order traversal.
# from collections import deque
# class TreeNode:
#     def __init__(self, data):
#         self.value = data
#         self.left = None
#         self.right = None

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.right = TreeNode(4)

# def lot(root):
#     q = deque([root])
#     ans = []
#     while q:
#         firstElement = q.popleft()
#         ans.append(firstElement.value)
#         if firstElement.left is not None:
#             q.append(firstElement.left)
#         if firstElement.right is not None:
#             q.append(firstElement.right)
#     return ans
# print(lot(root))

# Find maximum depth of a binary tree.

# class TreeNode:
#   def __init__(self, data):
#     self.value=data
#     self.left=None
#     self.right=None
# root =TreeNode(1)
# root.left=TreeNode(2)
# root.left.left=TreeNode(3)

# def maxDepth(root):
#   if root is None:
#     return 0
#   left=maxDepth(root.left)
#   right=maxDepth(root.right)
#   return 1+max(left,right)
# print(maxDepth(root))

# Count leaf nodes in a binary tree.

# leaf node is a node which has no children.

# class TreeNode:
#   def __init__(self, data):
#     self.value=data
#     self.left=None
#     self.right=None
# root =TreeNode(1)
# root.left=TreeNode(2)
# root.left.left=TreeNode(3)
# root.right=TreeNode(4)

# def countLeafNodes(root):
#   if root is None:
#     return 0
#   if root.left is None and root.right is None:
#     return 1
#   return countLeafNodes(root.left)+countLeafNodes(root.right)
# print(countLeafNodes(root))

# Diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# **Diameter of a Binary Tree = tree ke kisi bhi 2 nodes ke beech ka longest path (number of edges).**

# Example:

# ```text
#         1
#        / \
#       2   3
#      / \
#     4   5
# ```

# Longest path:

# ```text
# 4 → 2 → 1 → 3
# ```

# So:

# ```text
# Diameter = 3 edges
# ```

# **Easy difference:**

# * **Depth** → Root → Node
# * **Height** → Node → Deepest Leaf
# * **Diameter** → Any Node → Any Node, **longest path**

# class TreeNode:
#     def __init__(self, data):
#         self.value = data
#         self.left = None
#         self.right = None


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)

# diameter = float('-inf')
# def height(root):
#     global diameter
#     if root is None:
#         return -1
#     leftH = height(root.left)
#     rightH = height(root.right)
#     diameter = max(diameter, leftH + rightH + 2)
#     return 1 + max(leftH, rightH)
# height(root)
# print("Diameter:", diameter)

# WAP to print left view of a binary tree.

# class TreeNode:
#     def __init__(self, data):
#         self.value = data
#         self.left = None
#         self.right = None
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

# def leftView(root):
#     if root is None:
#         return []
#     result = []
#     queue = [root]
#     while queue:
#         level_size = len(queue)
#         for i in range(level_size):
#             node = queue.pop(0)
#             if i == 0:
#                 result.append(node.value)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#     return result
# print(leftView(root))

# WAP to print right view of a binary tree using DFS.

class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


def rightView(root):
    result = []

    def dfs(node, depth):
        if node is None:
            return
        if depth == len(result):
            result.append(node.value)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(rightView(root))

# WAP to find the lowest common ancestor (LCA) of two nodes in a binary tree.

def lowestCommonAncestor(root, p, q):
    if root is None or root is p or root is q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left is not None and right is not None:
        return root
    return left if left is not None else right


p = root.left.left
q = root.left.right
lca = lowestCommonAncestor(root, p, q)
print("LCA:", lca.value if lca is not None else None)

# Binary Search Tree (BST) is a binary tree in which for each node, the value of all the nodes in the left subtree is less than the value of the node, and the value of all the nodes in the right subtree is greater than the value of the node.

# why Binary Search Tree is used?
# Binary Search Tree (BST) is used for efficient searching, insertion, and deletion of elements.

# WAP to search a data in binary search tree

# class TreeNode:
#     def __init__(self, data):
#         self.value = data
#         self.left = None
#         self.right = None

# def searchBST(root, target):
#     if root is None or root.value == target:
#         return root
#     if target < root.value:
#         return searchBST(root.left, target)
#     return searchBST(root.right, target)

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(7)

# # Search for a value in the BST
# target = 5
# result = searchBST(root, target)
# if result:
#     print(f"Value {target} found in the BST.")
# else:
#     print(f"Value {target} not found in the BST.")

# WAP to search a data in binary search tree (iterative search)

# class TreeNode:
#     def __init__(self, data):
#         self.value = data
#         self.left = None
#         self.right = None

# def searchBSTIterative(root, target):
#     current = root
#     while current:
#         if target == current.value:
#             return current
#         elif target < current.value:
#             current = current.left
#         else:
#             current = current.right
#     return None
# target = 5
# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(7)

# result = searchBSTIterative(root, target)
# if result:
#     print(f"Value {target} found in the BST.")
# else:
#     print(f"Value {target} not found in the BST.")

# WAP to insert a value in a BST.

# class TreeNode:

#   def __init__(self, data):
#     self.value = data
#     self.left=None
#     self.right=None

# def insertNewNode(root, newValue):
#   if root is None:
#     return TreeNode(newValue)
#   if newValue>root.value:
#     root.right=insertNewNode(root.right, newValue)
#   elif newValue<root.value:
#     root.left=insertNewNode(root.left, newValue)
#   return root

# Inorder traversal for BST  
# Inorder = Left → Root → Right (LNR)

# class TreeNode:
#     def __init__(self, data):
#         self.value = data
#         self.left = None
#         self.right = None


# # Create BST
# root = TreeNode(4)

# root.left = TreeNode(2)
# root.right = TreeNode(6)

# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)

# root.right.left = TreeNode(5)
# root.right.right = TreeNode(7)


# # Inorder Traversal: Left → Root → Right
# def inorder(root):
#     if root is None:
#         return []

#     return inorder(root.left) + [root.value] + inorder(root.right)


# # Print result
# print(inorder(root))

# WAP to find minimum and maximum in a BST 

# class TreeNode:
#   def __init__(self, data):
#     self.value = data
#     self.left=None
#     self.right=None

# def findMin(root):
#   current = root
#   while current.left is not None:
#     current = current.left
#   return current.value

# def findMax(root):
#   current = root
#   while current.right is not None:
#     current = current.right
#   return current.value


# root = TreeNode(4)
# root.left = TreeNode(2) 
# root.right = TreeNode(6)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)

# print("Minimum value in the BST:", findMin(root))  
# print("Maximum value in the BST:", findMax(root)) #

# Delete a Node from a BST. with all case with explanation.

# class TreeNode:
#   def __init__(self, data):
#     self.value = data
#     self.left=None
#     self.right=None

# def findMinNode(node):
#   current = node
#   while current.left is not None:
#     current = current.left
#   return current



# def deleteTargetNode(root, target):
#   if root is None:
#     return root
#   if target < root.value:
#     root.left = deleteTargetNode(root.left, target)
#   elif target > root.value:
#     root.right = deleteTargetNode(root.right, target)
#   else:
#     # Node with only one child or no child
#     if root.left is None:
#       return root.right
#     elif root.right is None:
#       return root.left

#     # Node with two children: Get the inorder successor (smallest in the right subtree)
#     temp = findMinNode(root.right)
#     root.value = temp.value
#     root.right = deleteTargetNode(root.right, temp.value)

#   return root


# WAP to find LCA OF 2 nodes p and q 

class TreeNode:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

