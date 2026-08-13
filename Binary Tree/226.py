#226
#翻转二叉树
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root : return
        tmp = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(tmp)
        return root

#递归还蛮简单
#暂存一边节点 用定义函数翻转 暂存节点给另一半
#注意root.left = self.invertTree(tmp)这步里面是tmp