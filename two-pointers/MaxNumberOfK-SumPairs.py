class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        l,r = 0,n-1
        while l<r:
            if nums[l]+nums[r] == k:
                count+=1
                l+=1
                r-=1
            elif nums[l]+nums[r] < k:
                l+=1
            else:
                r-=1
        return count
            
## Question Link : https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=problem-list-v2&envId=two-pointers
## Time Complexity : O(nlogn)
## Space Complexity : O(1)