class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        q = deque()
        q.append(root)
        ans = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if i == 0:
                    ans = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans

##Question Link : https://leetcode.com/problems/find-bottom-left-tree-value/?envType=problem-list-v2&envId=depth-first-search
##Time Complexity : O(n)
##Space Complexity : O(n)