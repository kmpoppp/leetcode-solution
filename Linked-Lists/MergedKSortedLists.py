# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = []
        for L in lists:
            temp = L
            while temp:
                heapq.heappush(k, temp.val)
                temp = temp.next
        curr = ListNode()
        dummy = curr
        for i in range(len(k)):
            curr.next = ListNode(heapq.heappop(k))
            curr = curr.next   
        return dummy.next
    
## Question Link : https://leetcode.com/problems/merge-k-sorted-lists/description/
## Time Complexity : O(nlogn)
## Space Complexity : O(n)