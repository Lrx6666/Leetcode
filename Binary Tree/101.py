#101
#对称二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(right , left) :
            if not right and not left : return True
            if not right or not left : return False
            if left.val != right.val : return False
            return dfs(left.left, right.right) and \
                   dfs(left.right, right.left)
        return dfs(root.right , root.left)

#递归太好用了
#左右都空 true
#左右有一个是空 false
#左右值不等 false
#往下递归判断 画个图判断深度为2的dfs怎么写
#