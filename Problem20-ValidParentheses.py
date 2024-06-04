class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        parOpen = False 
        curlOpen = False
        bracOpen = False

        for char in s:
            if (char=='('):
                parOpen = True
            elif(char == '{'):
                curlOpen = True
            elif(char == '['):
                bracOpen = True
            elif(char == ')' and parOpen and prev == '('):
                parOpen = False
            elif(char == '}' and curlOpen and prev == '{'):
                curlOpen = False
            elif(char ==']' and bracOpen and prev == '['):
                bracOpen = False
            prev = char
            
        if(parOpen or curlOpen or bracOpen):
            return False
        else: return True

if __name__ == "__main__":
    answer = Solution()
    test1 = answer.isValid("()")
    test2 = answer.isValid("()[]{}")
    test3 = answer.isValid("(]")
    test4 = answer.isValid("([)")
    test5 = answer.isValid("{[]}")
    print(test1)
    print(test2)
    print(test3)
    print(test4)
    print(test5)