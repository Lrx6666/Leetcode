#94
#二叉树的中序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int] :
        def dfs(node : Optional[TreeNode]) -> None :
            if node is None :
                return
            dfs(node.left) #递归左子树
            ans.append(node.val) #根
            dfs(node.right) #递归右子树

        ans = []
        dfs(root)
        return ans


#三种遍历的遍历顺序

