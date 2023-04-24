# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,  = head, 
        curr = None
        if head and head.next:
            curr = head.next
        while curr:
            nxt = curr.next
            if prev.val == curr.val:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt
        return head