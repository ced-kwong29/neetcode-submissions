class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

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
            
            strs.append(s[ndx:endNdx])

            ndx = endNdx
            
        return strs