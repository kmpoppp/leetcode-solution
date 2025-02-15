class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k): ##reverse Group for k nodes
            prev, curr = None, head
            while k > 0 and curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k -= 1
            return prev,curr ## return new head and the rest that dont reverse
        length = 0
        node = head
        while node: ##count the length
            node = node.next
            length += 1
        ROUND = length // k ## mod for find the round
        temp = head
        oi, temp = reverse(temp, k) ##reverse 1st round
        prev_tail = head 
        for _ in range(ROUND - 1): ##reverse for the rest round
            new_head, temp = reverse(temp, k)
            prev_tail.next = new_head
            prev_tail = prev_tail.next
            for _ in range(k - 1):
                prev_tail = prev_tail.next
        prev_tail.next = temp
        return oi 
## Question Link : https://leetcode.com/problems/reverse-nodes-in-k-group/description/
## Time Complexity : O(n)
## Space Complexity : O(1)