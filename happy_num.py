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