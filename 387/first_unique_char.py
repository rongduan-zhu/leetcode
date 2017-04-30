class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        oc = OrderedCounter()

        for i, c in enumerate(s):
            oc.insert(c, i)

        return oc.find_first_unique()

class OrderedCounter(object):
    def __init__(self):
        self.counter = {}
        self.elements = []

    def insert(self, element, i):
        if element in self.counter:
            self.counter[element][0] += 1
        else:
            self.elements.append(element)
            self.counter[element] = [1, i]

    def find_first_unique(self):
        for i, element in enumerate(self.elements):
            if self.counter[element][0] == 1:
                return self.counter[element][1]

        return -1
