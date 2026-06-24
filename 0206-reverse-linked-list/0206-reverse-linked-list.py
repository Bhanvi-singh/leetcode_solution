# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is  None or head.next is  None:
            return head
        current = head
        previous = None
        while current != None:
             front = current.next
             current.next = previous
             current.previous = front
             previous = current
             current = front
        return previous  