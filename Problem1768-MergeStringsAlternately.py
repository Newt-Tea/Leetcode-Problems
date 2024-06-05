class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        short = min(len(word1), len(word2))
        long = max(len(word1), len(word2))
        result = ""
        i = 0


        while(i < short):
            result += word1[i]
            result += word2[i]
            i += 1
        if(short == len(word1)):
            while(i < long):
                result += word2[i]
                i += 1
        else:
            while(i < long):
                result += word1[i]
                i += 1
        return result

if __name__ == "__main__":
    answer = Solution()
    test1 = answer.mergeAlternately("abc", "prq")
    test2 = answer.mergeAlternately("ab", "pqrs")
    test3 = answer.mergeAlternately("abcd", "pq")
    print(test1)
    print(test2)
    print(test3)