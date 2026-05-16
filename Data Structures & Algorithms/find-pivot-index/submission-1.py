class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lSum = 0
        rSum = 0

        for currPivot in range(len(nums)):
            if currPivot == 0 :
                rSum = sum(nums[currPivot+1:])
                if lSum == rSum:
                    return currPivot
            else:
                lSum = sum(nums[:currPivot])
                rSum = sum(nums[currPivot+1:])
                if lSum == rSum:
                    return currPivot
        return -1

