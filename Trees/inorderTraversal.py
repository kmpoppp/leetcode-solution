class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans
    
##Question Link : https://leetcode.com/problems/binary-tree-inorder-traversal/
##Time Complexity : O(n)
##Space Complexity : O(h)