from random import randint

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums[:]

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # or
        # return random.shuffle(self.reset())
        shuffled = self.reset()

        for i in range(len(self.nums) - 1, -1, -1):
            random_element = randint(0, i)

            temp = shuffled[i]
            shuffled[i] = shuffled[random_element]
            shuffled[random_element] = temp

        return shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
