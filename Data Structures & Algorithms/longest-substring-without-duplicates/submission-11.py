class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        maxLong = 0

        if n == 0:
            return 0 
        elif n == 1:
            return 1
        elif n == 2:
            if s[0] != s[1]:
                return 2
            else:
                return 1
        else:
            for i in range(n-1):
                l = s[i]
                for j in range(i+1, n):
                    valJ = s[j]
                    if valJ not in l:
                        l +=valJ
                    else:
                        break
                print(l)
                maxLong = max(len(l),maxLong)
            return maxLong
                


        