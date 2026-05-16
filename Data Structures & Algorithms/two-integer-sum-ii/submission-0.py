class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(0, len(numbers)-1):
            rest = target - numbers[i]
            if rest in numbers[i+1:]:
               index_rest = numbers.index(rest)
               return [i + 1, index_rest + 1]