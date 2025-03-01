class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if not root.left and not root.right:## if leaves
                if target == root.val:
                    return None
            return root
        return dfs(root)
    
##Question Link : https://leetcode.com/problems/delete-leaves-with-a-given-value/
##Time Complexity : O(n)
##Space Complexity : O(h)