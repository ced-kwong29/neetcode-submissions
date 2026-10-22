class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = Counter(t), defaultdict(int)
        need, total = len(countT), 0

        end = len(s)
        res, minLength = (0, end - 1), end

        left = 0
        for right in range(end):
            window[s[right]] += 1

            if window[s[right]] == countT.get(s[right], 0):
                total += 1

            while total == need:
                currLength = right - left
                if currLength < minLength:
                    minLength = currLength
                    res = (left, right)

                window[s[left]] -= 1
                if window[s[left]] < countT.get(s[left], 0):
                    total -= 1
                
                left += 1
        
        return s[res[0]:res[1] + 1] if minLength < end else ""
