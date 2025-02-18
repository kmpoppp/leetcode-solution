def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        ROWS , COLS = len(nums),len(nums[0])
        bottom,top = 0 , ROWS-1
        row = -1
        while bottom<=top:
            m = (top+bottom)//2
            if nums[m][0] <= target <= nums[m][-1]:
                row = m
                break
            elif nums[m][0] > target:
                top = m-1
            else:
                bottom = m+1
        if row == -1:
            return False
        l,r = 0,COLS-1
        while l<=r:
            m = (l+r)//2
            if nums[row][m] == target:
                return True
            if nums[row][m] > target:
                r = m-1
            else:
                l = m+1
        
        return False
    
## Question Link : https://leetcode.com/problems/search-a-2d-matrix/submissions/1515270400/
## Time Complexity : O(log (m*n))
## Space Complexity : O(1)