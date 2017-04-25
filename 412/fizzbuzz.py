#!/usr/bin/env python
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return list(map(Solution.fizz_buzz_number, xrange(1, n + 1)))

    @staticmethod
    def fizz_buzz_number(number):
        if (number % 3 == 0 and number % 5 == 0):
            return "FizzBuzz"
        elif (number % 3 == 0):
            return "Fizz"
        elif (number % 5 == 0):
            return "Buzz"
        else:
            return str(number)

solution = Solution()
print solution.fizzBuzz(3)
print solution.fizzBuzz(5)
print solution.fizzBuzz(4)
print solution.fizzBuzz(15)
