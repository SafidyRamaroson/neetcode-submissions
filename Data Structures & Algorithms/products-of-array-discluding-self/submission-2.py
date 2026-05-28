class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            m = 1
            for j in range(len(nums)):
                if i != j:
                    m *= nums[j]
            res.append(m)

        return res
"""
nums = [1,2,4,6]
P[0] = p[1] * p[2] * p[3]
P[1] = p[0] * p[2] * p[3]
P[2] = p[0] * p[1] * p[3]
P[3] = p[0] * p[1] * p[2]

"""

        

