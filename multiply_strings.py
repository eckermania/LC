"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
This method would be useful if needed to process numbers (or results) that are larger than the 32 bits held by an int -
essentially mimicking the functionality of a big int
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == "0" or num2 == "0":
            return "0"

        # dict to proxy int() functionality
        charIntDict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        #reverse num strings to make them easier to traverse
        num1, num2 = num1[::-1], num2[::-1]

        #array to hold final output
        product = [0] * (len(num1) + len(num2))

        # num1 is the multiplier and num2 is the multiplicand - product will track the digits in reverse order 
        for index1 in range(len(num1)):
            for index2 in range(len(num2)):
                digit = charIntDict[num1[index1]] * charIntDict[num2[index2]]
                product[index1+index2] += digit
                product[index1+index2+1] += (product[index1+index2]//10)
                product[index1+index2] = product[index1 + index2] % 10

        # reverse the product and strip out leading zeros
        product = product[::-1]
        i = 0
        while product[i] == 0:
            i+=1

        result = ''
        for productIndex in range(i, len(product)):
            charIndex = list(charIntDict.values()).index(product[productIndex])
            result += list(charIntDict.keys())[charIndex]

        return result


if __name__ == "__main__":
    newSol= Solution()
    num1 = "2"
    num2 = "3"
    print(newSol.multiply(num1, num2))
    #expected: "6"

    num3 = "123"
    num4 = "456"
    print(newSol.multiply(num3, num4))
    #expected: "56088"