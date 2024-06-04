class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xstr = str(x)
        ystr = ""
        for char in xstr:
            ystr = char + ystr

        if(ystr == xstr):
            return True
        else: return False

    
if __name__ == "__main__":
    answer = Solution()
    test1 = answer.isPalindrome(121)
    print(test1)