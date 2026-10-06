# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(array, start, mid, end):
            left = array[start:mid + 1]
            right = array[mid + 1:end + 1]

            l, lEnd = 0, len(left)
            r, rEnd = 0, len(right)
            ndx = start

            while l < lEnd and r < rEnd:
                if left[l].key <= right[r].key:
                    array[ndx] = left[l]
                    l += 1
                else:
                    array[ndx] = right[r]
                    r += 1
                ndx += 1

            while l < lEnd:
                array[ndx] = left[l]
                l += 1
                ndx += 1

            while r < rEnd:
                array[ndx] = right[r]
                r += 1
                ndx += 1


        def sort(array, start, end):
            if end - start <= 0:
                return array

            mid = (start + end) // 2
            sort(array, start, mid)
            sort(array, mid + 1, end)

            merge(array, start, mid, end)

            return array

        return sort(pairs, 0, len(pairs) - 1)
