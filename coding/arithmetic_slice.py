class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        k = 0
        for i in range(2, len(A)):
            if (A[i] - A[i-1]) == (A[i-1] - A[i-2]):
                k += 1
                count += k
            else:
                k = 0
                
        return count
