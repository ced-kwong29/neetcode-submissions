class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = Counter(t), defaultdict(int)
        have, need = 0, len(countT)

        res, resLength = (-1, -1), float("inf")
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            if window[s[right]] == countT.get(s[right], -1):
                have += 1

            while have == need:
                currLength = right - left + 1
                if currLength < resLength:
                    resLength = currLength
                    res = (left, right)
                
                window[s[left]] -= 1
                if window[s[left]] < countT.get(s[left], -1):
                    have -= 1
                    
                left += 1

        return s[res[0]:res[1] + 1] if resLength != float("inf") else ""
            