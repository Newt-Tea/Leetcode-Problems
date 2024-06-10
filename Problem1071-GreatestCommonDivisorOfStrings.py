class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        short = min(len(str1),len(str2))

        if(len(str1) > len(str2)):
            longStr = str1
            shortStr = str2
        else:
            longStr = str2
            shortStr = str1
        result = shortStr

        for i in range(short):
            if(shortStr[i] == longStr[i]):
                result += longStr[i]
            else:
                break
        if(len(result) % len())
        return result

if __name__ == "__main__":
    answer = Solution()
    test1 = answer.gcdOfStrings("ABCABC", "ABC")
    test2 = answer.gcdOfStrings("ABABAB", "ABAB")
    test3 = answer.gcdOfStrings("LEET", "CODE")
    print(test1)
    print(test2)
    print(test3)