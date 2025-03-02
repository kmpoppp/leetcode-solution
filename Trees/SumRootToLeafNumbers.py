class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        temp = []
        def dfs(root, t):
            if not root:
                return
            if not root.left and not root.right:
                temp.append(t + str(root.val))
                return
            t = t + str(root.val)
            dfs(root.left, t)
            dfs(root.right, t)
        dfs(root, '')
        ans = 0
        for t in temp:
            ans += int(t)
        return ans

##Question Link : https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
##Time Complexity : O(n)
##Space Complexity : O(n)