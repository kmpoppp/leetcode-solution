class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            temp = -float('inf')
            for _ in range(len(q)):
                node = q.popleft()
                if node.val > temp:
                    temp = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(temp)
        return ans

##Question Link : https://leetcode.com/problems/find-largest-value-in-each-tree-row/
##Time Complexity : O(n)
##Space Complexity : O(h)