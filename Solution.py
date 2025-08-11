class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        stringList = list(s)
        
        for i in range(len(stringList)):
            substringList = []
            for j in range(i, len(stringList)):
                if stringList[j] in substringList:
                    break
                substringList.append(stringList[j])
            maxLength = max(maxLength, len(substringList))
        
        return maxLength
