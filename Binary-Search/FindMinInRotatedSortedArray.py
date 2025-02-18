class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l <r:
            m = (l+r)//2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = m+1
        return nums[l]
    
## Question Link : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
## Time Complexity : O(logn)
## Space Complxeity : O(1)