# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def __init__(self):
#         self.root = [4, 2, 7, 1, 3, 6, 9]
#
#     def inverted(self):
#         new_node = TreeNode()
#         if self.root is None:
#             self.root = new_node
#         temp = new_node
#         while True:
#             if new_node.val == temp.val:
#                 return False
#             if new_node.val > temp.val:
#                 if temp.left is None:
#                     temp.left = new_node
#             else:
#                 if temp.right is None:
#                     temp.right = new_node
#                     return True
#                 temp = temp.right
#
#
