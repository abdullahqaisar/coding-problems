class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        fast = head.next
        slow = head

        while fast != None and fast.next != None:
            if slow is fast: 
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False