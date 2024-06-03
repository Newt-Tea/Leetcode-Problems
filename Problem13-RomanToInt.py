class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        prevChar = ''
        for char in s:
            if(char == "I"):
                total += 1
            elif(char == "V"):
                total += 5
                if(prevChar == "I"):
                    total -= 2
            elif(char == "X"):
                total += 10
                if(prevChar == "I"):
                    total -= 2
            elif(char == "L"):
                total += 50
                if(prevChar == "X"):
                    total -= 20
            elif(char == "C"):
                total += 100
                if(prevChar == "X"):
                    total -= 20
            elif(char == "D"):
                total += 500
                if(prevChar == "C"):
                    total -= 200
            elif(char == "M"):
                total += 1000
                if(prevChar == "C"):
                    total -= 200
            else: print("Error: Invalid Input")
            prevChar = char
        return total

if __name__ == "__main__":
    answer = Solution()
    test1 = answer.romanToInt("III")
    test2 = answer.romanToInt("MCMXCIV")
    print(test1)
    print(test2)