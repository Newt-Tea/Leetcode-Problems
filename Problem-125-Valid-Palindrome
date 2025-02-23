class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        #remove all non-alphanumeric characters
        s = ''.join(c for c in s if c.isalnum())
        sBack = s[::-1]
        if s == sBack:
            return True
        else: return False
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))