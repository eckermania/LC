class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """

        currCol = 0
        ballStart = 0
        lastCol = len(grid[0])-1
        lastRow = len(grid)-1

        outputList = []
        
        while ballStart <= lastCol:
            currRow = 0
            currCol = ballStart
            success = True

            while currRow <= lastRow:
                direction = grid[currRow][currCol]
              
                if (direction == -1 and currCol== 0) or (direction == 1 and currCol == lastCol):
                    success = False
                    break
                
                nextDirection = grid[currRow][currCol+direction]

                if direction != nextDirection:
                    success = False
                    break

                else:
                    currRow += 1
                    currCol += direction

            if success:
                outputList.append(currCol)
            else:
                outputList.append(-1)

            ballStart += 1
     
        return outputList

if __name__ == "__main__":
        
    newSol = Solution()
    grid1 = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    output1 = newSol.findBall(grid1)
    print(output1)
    # expected output: [1,-1,-1,-1,-1]
    
    grid2 = [[-1]]
    output2 = newSol.findBall(grid2)
    print(output2)
    # expected output: [-1]

    grid58 = [[-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1]]

    output58 = newSol.findBall(grid58)
    print(output58)
    # expected output: [-1,-1,-1,2,3,4,5,6,-1,-1,9,10,11,14,-1,-1,15,16,19,20,-1,-1,21,24,-1,-1,25,-1,-1,28,29,30,31,32,33,34,35,-1,-1,-1,-1,40,41,42,43,44,45,-1,-1,48,-1,-1,-1,-1,53,56,-1,-1,-1,-1,59,60,61,64,65,66,67,68,-1,-1,71,72,-1,-1,75,76,-1,-1,77,78,-1,-1,-1,-1,83,86,-1,-1,87,-1,-1,-1,-1,94,95,-1,-1,96,97,98]
