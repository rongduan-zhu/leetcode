class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [[] for i in xrange(len(nums) + 1)]
        freq = {}
        output = []

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for num, freq in freq.items():
            bucket[freq].extend([num])

        i = len(bucket) - 1
        while len(output) < k and i > -1:
            output.extend(bucket[i])
            i -= 1

        return output[:k]
