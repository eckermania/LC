# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution(object):
    def spiralOrder(self, matrix, rowStart=0, rowEnd=None, colStart=0, colEnd=None, outputList=[]):
        """
        :type matrix: List[List[int]]
        :type rowStart: int
        :type rowEnd: int
        :type colStart: int
        :type colEnd: int
        :type outputList: List[int]
        :rtype: List[int]
        """
        if rowEnd is None:
          rowEnd = len(matrix) - 1
          colEnd = len(matrix[0]) - 1

        #All of matrix has been traversed
        if rowStart > rowEnd or colStart > colEnd:
            return outputList
        
        #From left to right, append current number in row to output list
        for i in range(colStart, colEnd + 1):
            outputList.append(matrix[rowStart][i])

        #From top to bottom, append current number in rightmost column
        for i in range(rowStart+1, rowEnd + 1):
            outputList.append(matrix[i][colEnd])

        #From right to left, append current number in bottom row
        if rowEnd != rowStart:
            for i in range(colEnd - 1, colStart -1, -1):
                outputList.append(matrix[rowEnd][i])

        #From bottom to top, append current number in leftmost column
        if colEnd != colStart:
            for i in range(rowEnd - 1, rowStart, -1):
              outputList.append(matrix[i][colStart])
        
        #Restart recursion with next inner layer of matrix
        return self.spiralOrder(matrix, rowStart+1, rowEnd - 1, colStart + 1, colEnd - 1, outputList)