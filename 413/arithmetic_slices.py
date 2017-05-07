class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0

        count = []

        if A[2] - A[1] == A[1] - A[0]:
            count.append(1)
        else:
            count.append(0)

        for i in range(3, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                count.append(count[i - 3] + 1)
            else:
                count.append(0)

        return sum(count)
