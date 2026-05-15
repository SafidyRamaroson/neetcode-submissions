class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        grouped = {}
        setted_nums = sorted(list(dict.fromkeys(nums)))

        if len(nums) == 0:
            return 0
        else:
            for i in range(len(setted_nums)):
                if len(grouped) == 0:
                    grouped["0"] = [setted_nums[i]]
                else:
                    last_key = list(grouped)[-1]
                    if grouped[last_key][-1] + 1 == setted_nums[i]:
                        grouped[last_key].append(setted_nums[i])
                    else:
                        grouped[str(int(last_key) + 1)] = [setted_nums[i]]
            sorted_group_by_value = dict(sorted(grouped.items(), key = lambda item: len(item[1]), reverse= True))
            first_key = list(sorted_group_by_value)[0]
            return len(sorted_group_by_value[first_key])
                






            

            
            


        