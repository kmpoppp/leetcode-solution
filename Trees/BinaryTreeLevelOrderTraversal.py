class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque()
        q.append(root)
        while q:
            ans.append([])
            for _ in range(len(q)):
                node = q.popleft()
                ans[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
    
##Question Link : https://leetcode.com/problems/binary-tree-level-order-traversal/
##Time Complexity : O(n)
##Space Complexity : O(n)