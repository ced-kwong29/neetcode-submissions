class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{str(len(s))}#{s}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        end = len(s)
        while i < end:
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded_str.append(s[i:j])
            i = j

        return decoded_str
