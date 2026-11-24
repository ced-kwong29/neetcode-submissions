class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dialPad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        combos = []
        end = len(digits)
        def generate(ndx, combo):
            if ndx == end:
                if combo:
                    combos.append(combo)
                return

            for char in dialPad[digits[ndx]]:
                generate(ndx + 1, combo + char)
                
        generate(0, "")
        return combos