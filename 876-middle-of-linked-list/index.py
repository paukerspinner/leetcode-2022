# Definition for singly-linked list.
from typing import Optional
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        firstPointer = head
        secondPointer = head

        while secondPointer and secondPointer.next != None:
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next.next

        return firstPointer