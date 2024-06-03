class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        idx = 0
        idx2 = 0

        while(idx < len(nums)):
            while(idx2 < len(nums)):
                if((nums[idx] + nums[idx2]) == target):
                    result = [idx,idx2]
                    return (result)
                else: idx2 += 1
            idx2 = 0
            idx += 1

if __name__ == '__main__':
    result = Solution()
    print (result.twoSum([3,2,4], 6))

