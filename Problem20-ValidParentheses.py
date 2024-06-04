class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for char in s:
            if (char=='('):
                parOpen = True
            elif(char == '{'):
                curlOpen = True
            elif(char == '['):
                bracOpen = True
            elif(char == ')' and parOpen):
                parOpen = False
            elif(char == '}' and curlOpen):
                curlOpen = False
            elif(char ==']' and bracOpen):
                bracOpen = False
            
            if(parOpen or curlOpen or bracOpen):
                return False
            else: return True

if __name__ == "__main__":
    answer = Solution()
    test1 = answer.isValid("()")
    test2 = answer.isValid("()[]{}")
    test3 = answer.isValid("(]")
    print(test1)
    print(test2)
    print(test3)