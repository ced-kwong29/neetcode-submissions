class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f'{len(s)}#{s}' for s in strs])

    def decode(self, s: str) -> List[str]:
        strs = []

        ndx, end = 0, len(s)

        while ndx < end:
            endNdx = ndx
            while s[endNdx] != "#":
                endNdx += 1

            strLength = int(s[ndx:endNdx])

            endNdx += 1
            ndx = endNdx

            endNdx += strLength

            # for _ in range(strLength):
            #     endNdx += 1
            
            strs.append(s[ndx:endNdx])

            ndx = endNdx
            
        return strs