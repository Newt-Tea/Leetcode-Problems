class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        while(num > 0):
            if(num >= 1000):
                result += "M"
                num -= 1000
            elif(num >= 500):
                result += "D"
                num -= 500
            elif(num >= 100):
                result += "C"
                num -= 100
            elif(num >= 50):
                result += "L"
                num -= 50
            elif(num >= 10):
                    result += "X"
                    num -= 10
            elif(num >= 5):
                result += "V"
                num -= 5
            else:
                result += "I"
                num -= 1

        return(result)

if __name__ == "__main__":
    answer = Solution()
    test1 = answer.intToRoman(3749)
    test2 = answer.intToRoman(58)
    print(test1)
    print(test2)