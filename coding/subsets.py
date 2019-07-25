class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subset(dst, src, result):
            if len(src) == 0:
                result.append(dst)
            else:
                subset(dst + [src[0]], src[1:], result)
                subset(dst, src[1:], result)

        result = []
        subset([], nums, result)
        return result
