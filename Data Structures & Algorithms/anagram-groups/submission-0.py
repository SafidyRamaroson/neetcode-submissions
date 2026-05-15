class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # On verifie qu'on a une seul element dans la liste et la retourner
        if len(strs) == 1:
            return [strs]
        # on cree une array qui groupe les anagrams
        # on va sorted chaque string dans le tableau
        # on fait une iteration et on cherche tous les index de l'element

        grouped_anagrams = []
        sorted_strs = [sorted(i) for i in strs]
        seen = []

        for target in sorted_strs:
            if target not in seen:
                seen.append(target)
                indices = [i for i, x in enumerate(sorted_strs) if x == target]
                grouped_anagrams.append([strs[x] for x in indices])
        
        return grouped_anagrams
