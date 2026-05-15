class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        set_nums = set(nums)
        freq = {}

        for n in set_nums:
            # on recherche la frequence de chaque nombre sous forme de dict
            freq[str(n)] = nums.count(n)

        # On trie la dict par ordre decroissante
        sorted_freq = dict(sorted(freq.items(),key = lambda x:x[1], reverse = True))

        # On prend les keys du sorted_freq cad les elements
        els = [k for k,v in sorted_freq.items()]

        # On prend le K premier
        result = [ int(els[i]) for i in range(0,k)]

        return result


        