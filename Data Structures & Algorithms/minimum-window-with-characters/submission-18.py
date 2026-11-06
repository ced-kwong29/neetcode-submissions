class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = (0, 0)
        minLength = float("inf")

        countT, freq = Counter(t), defaultdict(int)
        need, have = len(countT), 0

        left = 0
        for right in range(len(s)):
            char = s[right]
            freq[char] += 1

            if countT.get(char) and countT[char] == freq[char]:
                have += 1

            while have == need:
                currLength = right - left + 1
                if currLength < minLength:
                    minLength = currLength
                    res = (left, right)

                if countT.get(s[left]) and countT[s[left]] == freq[s[left]]:
                    have -= 1

                freq[s[left]] -= 1
                left += 1


        return s[res[0]:res[1] + 1] if minLength != float("inf") else ""