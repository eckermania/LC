# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        output = self.buildOutput(n)

        numSet = set()

        # Sum the squares of n's digits
        while output > 1 and output not in numSet:
            numSet.add(output)

            output = self.buildOutput(output)

        return output == 1

    def buildOutput(self, num):
        newSum = 0
        for digit in str(num):
            newSum += int(digit)**2
        
        return newSum