import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # some how when the code is ran on submit server, heapify [1, 2] turns into [2]...
        return heapq.nsmallest(k, heapq.merge(*matrix))[-1]

        minheap = map(lambda (index, val): MatrixCell(0, index, val), enumerate(matrix[0][:]))
        heapq.heapify(minheap)

        for i in xrange(k - 1):
            min_val = heapq.heappop(minheap)
            if min_val.x == len(matrix) - 1:
                continue
            heapq.heappush(minheap, MatrixCell(min_val.x + 1, min_val.y, matrix[min_val.x + 1][min_val.y]))

        ans = heapq.heappop(minheap).val
        return ans

class MatrixCell(object):
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def __eq__(self, other):
        if type(other) is type(self):
            return self.x == other.x and \
                self.y == other.y and \
                self.val == other.val

        return False
