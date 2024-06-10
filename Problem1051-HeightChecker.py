class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        diff = 0
        for num in range(len(heights)):
            if(heights[num] != expected[num]):
                diff += 1

        return diff

if __name__ == "__main__":
    answer = Solution()
    test1 = answer.heightChecker([1,1,4,2,1,3])
    test2 = answer.heightChecker([5,1,2,3,4])
    test3 = answer.heightChecker([1,2,3,4,5])
    print(test1)
    print(test2)
    print(test3)