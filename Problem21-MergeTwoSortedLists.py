# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = []
        master = [list1, list2]
        long = max(len(list1), len(list2))
        if (long == list1):
            short = list2
        else:
            short = list1

        i = 0

        for item in long:
            result.append(min(long[i],short[i]))
            result.append(max(long[i],short[i]))