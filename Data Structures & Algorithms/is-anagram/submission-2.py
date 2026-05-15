class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # la taille des strings ne sont pas le meme
        if len(s) != len(t):
            return False
        else:
            # On utilise set() pour eviter la duplication
            ss = set(s)

            # On itere sur le set et on compte le nombre de caractere
            for car in s:
                if s.count(car) != t.count(car):
                    return False

            return True