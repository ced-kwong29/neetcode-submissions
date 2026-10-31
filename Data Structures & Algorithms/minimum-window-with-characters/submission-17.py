class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, minLength = (0, 0), float("inf")

        countT, freq = Counter(t), defaultdict(int)
        need, have = len(countT), 0

        left = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            if countT.get(s[right]) and countT[s[right]] == freq[s[right]]:
                have += 1

            while have == need:
                currLength = right - left + 1
                if currLength < minLength:
                    res = left, right
                    minLength = currLength
                
                if countT.get(s[left]) and countT[s[left]] == freq[s[left]]:
                    have -= 1
                freq[s[left]] -= 1
                left += 1

        return s[res[0]:res[1] + 1] if minLength != float("inf") else ""