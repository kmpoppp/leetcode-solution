class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a,k,r = head,head,head
        while r.next != None:
            if n>0:
                n-=1
            else:
                k = k.next
            r = r.next
        if n>0:
            return a.next
        k.next = k.next.next
        return a

## Question Link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1505113625/
## Time Complexity : O(n)
## Space Complexity : O(1)
            
        