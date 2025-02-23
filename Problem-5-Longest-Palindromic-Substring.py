class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 1:
            return s
        # Place characters with multiple occurences in a dictionary
        multiChar = self.find_multiples(s)


        # Sort the dictionary by value
        multiChar = sorted(multiChar.items(), key=lambda x: x[1],reverse=True)

        #Build the longest possible Palindrome
        longestPalindrome = ""
        for key, value in multiChar:
            if value > 0 and value % 2 == 0:
                longestPalindrome = key * int(value/2) + longestPalindrome + key * int(value/2)
        return(longestPalindrome)

    def find_multiples(self, s):
        """
        s: str
        Finds multiple occurences of characters in a string and returns a dictionary
        """
        multiChar = {}
        for c in s:
            if c in multiChar:
                multiChar[c] += 1
            else:
                multiChar[c] = 1
        return multiChar

if __name__ == '__main__':
    s = Solution()
    s.longestPalindrome("aabccccdd")