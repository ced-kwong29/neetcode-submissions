class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = Counter(t), defaultdict(int)
        need, have = len(countT), 0

        res = 0, 0
        minLength = float("inf")

        left = 0
        for right in range(len(s)):
            window[s[right]] += 1

            if countT.get(s[right]) and countT[s[right]] == window[s[right]]:
                have += 1

            while have == need:
                currLength = right - left + 1
                if currLength < minLength:
                    minLength = currLength
                    res = left, right

                if countT.get(s[left]) and countT[s[left]] == window[s[left]]:
                    have -= 1
                
                window[s[left]] -= 1
                left += 1

        return s[res[0]:res[1] + 1] if minLength < float("inf") else ""