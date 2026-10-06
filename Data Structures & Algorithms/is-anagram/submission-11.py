class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lengthS = len(s)
        if lengthS != len(t):
            return False

        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))

        for ndx in range(lengthS):
            if sortedS[ndx] != sortedT[ndx]:
                return False
        
        return True