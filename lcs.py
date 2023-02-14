# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        index = 0

        for letter in strs[0]:
            for word in range(1, len(strs)):
                if letter != strs[word][index]:
                    return prefix
                
            index += 1
            prefix += letter

        return prefix

        

if __name__ == "__main__":
    newSol = Solution()
    arr1 = ["flower","flow","flight"]
    print(newSol.longestCommonPrefix(arr1))
    #expected output: "fl"

    arr2 = ["dog","racecar","car"]
    print(newSol.longestCommonPrefix(arr2))