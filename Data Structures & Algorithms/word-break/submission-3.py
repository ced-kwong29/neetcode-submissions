class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        end = len(s)
        dp = [False] * (end + 1)
        dp[end] = True

        for i in range(end - 1, -1, -1):
            for word in wordDict:
                wLen = len(word)
                if wLen == len(s[i:i + wLen]) and s[i:i + wLen] == word:
                    dp[i] = dp[i + wLen]
                if dp[i]:
                    break
        return dp[0]