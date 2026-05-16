class Solution:
    def checkTriplet(self, nums: List[List[int]], newTriplet: List[int]) -> bool:
        return any(
            item[0] == newTriplet[0] and
            item[1] == newTriplet[1] and
            item[2] == newTriplet[2]
            for item in nums
        )


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        # nj + nk = -ni
        sorted_nums = sorted(nums)
        n = len(nums)
        for i in range(len(sorted_nums) - 2):
            ni = sorted_nums[i]
            l = i+1
            r = n-1

            while l < r:
                if sorted_nums[l] + sorted_nums[r] + ni == 0:
                    newTriplet = [ni,sorted_nums[l] , sorted_nums[r]]
                    hasTriplet = self.checkTriplet(result,newTriplet)
                    # on verifie si le triplet existe deja
                    if not hasTriplet:
                        result.append(newTriplet)
                    l +=1
                    r -=1
                elif sorted_nums[l] + sorted_nums[r] + ni > 0:
                    r -=1
                else:
                    l +=1
        return result
        



        