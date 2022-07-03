# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        firstPointer = head
        secondPointer = head
        
        for i in range(n):
            secondPointer = secondPointer.next
        
        if secondPointer == None:
            return head.next
            
        while secondPointer.next:
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next
        firstPointer.next = firstPointer.next.next
        
        return head