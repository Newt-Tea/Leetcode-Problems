class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        long = max(word1, word2)
        short = min(word1, word2)
        result = ""
        i = 0

        for char in short:
            result += word1[i]
            result += word2[i]
            i += 1

if __name__ == "__main__":
    answer = Solution()
    test1 = answer.mergeAlternately("abc", "prq")
    test2 = answer.mergeAlternately("ab", "pqrs")
    test3 = answer.mergeAlternately("abcd", "pq")
    print(test1)
    print(test2)
    print(test3)