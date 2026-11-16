# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        def rec(prev,curr):
            if curr is None: return prev

            new_head=rec(curr,curr.next)
            curr.next=prev
            return new_head

        return rec(None,head)

        