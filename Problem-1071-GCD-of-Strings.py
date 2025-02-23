# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself 
# one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]

if __name__ == "__main__":
    print(Solution().gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
    print(Solution().gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
    print(Solution().gcdOfStrings("LEET", "CODE"))    # Output: ""
    print(Solution().gcdOfStrings("ABCDEF", "ABC"))   # Output: ""
    print("The strings are divided by the largest string")
