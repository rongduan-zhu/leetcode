class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        available_mutations = {}

        for mutation in bank:
            available_mutations[mutation] = True

        if end not in available_mutations:
            return -1

        available_mutations[end] = False

        return Solution.find_mutation(end, start, available_mutations, 0)

    @staticmethod
    def find_mutation(start, end, available_mutations, depth):
        if Solution.can_mutate(start, end):
            return depth + 1

        best_mutation = -1
        for mutation in filter(lambda kvp: kvp[1], available_mutations.iteritems()):
            if Solution.can_mutate(start, mutation[0]):
                available_mutations[mutation[0]] = False
                mutations = Solution.find_mutation(mutation[0], end, available_mutations, depth + 1)

                if best_mutation == -1:
                    best_mutation = mutations

                if mutations != -1 and mutations < best_mutation:
                    best_mutation = mutations

                available_mutations[mutation[0]] = True

        return best_mutation

    @staticmethod
    def can_mutate(g1, g2):
        mismatch = 0
        for i in xrange(8):
            if g1[i] != g2[i]:
                mismatch += 1

        return mismatch == 1

