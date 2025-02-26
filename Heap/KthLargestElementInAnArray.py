class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

##Question Link : https://leetcode.com/problems/kth-largest-element-in-an-array/
##Time Complexity :  O(nlogk)
##Space Complexity : O(k)