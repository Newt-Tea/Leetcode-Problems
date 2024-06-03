class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        large = ""
        for string in strs:
            if len(string) > len(large):
                large = string


        idx = 0
        match = False
        lastPre = ""
        result = ""
        while(idx < len(large)):
            if (len(strs) == 1):
                return strs[0]
            else:
                for string in strs: 
                    pre = string[0:idx]
                    if(pre == lastPre):
                        match = True
                    else: match = False
                    lastPre = pre
                if match == True:
                    result = pre
                if match == False:
                    return result
                idx += 1
        return result
        

if __name__ == "__main__":
    answer = Solution()
    test1 = answer.longestCommonPrefix(["flower","flow","flight"])
    test2 = answer.longestCommonPrefix(["dog","racecar","car"])
    test3 = answer.longestCommonPrefix(["a"])
    print(test1)
    print(test2)
    print(test3)