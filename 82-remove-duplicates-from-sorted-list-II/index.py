from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(None, head)
        prev, cur, duplicatedVal = res, res.next, res.val
        
        while cur:
            if cur.next and cur.val == cur.next.val:
                duplicatedVal = cur.val
            
            if cur.val != duplicatedVal:
                prev = cur
                cur = cur.next
            else:
                while cur and cur.val == duplicatedVal:
                    cur = cur.next
                prev.next = cur
            
        return res.next