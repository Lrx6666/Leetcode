#104 二叉树的最大深度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root : return 0
        return max(self.maxDepth(root.left) , self.maxDepth(root.right)) + 1


#递归
#最简单的方法是返回左右子树中较大的再+1