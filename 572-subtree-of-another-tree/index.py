from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(nodeA, nodeB):
            if nodeA is None or nodeB is None:
                return nodeA == nodeB
            elif nodeA.val != nodeB.val:
                return False
            else:
                return isIdentical(nodeA.left, nodeB.left) and isIdentical(nodeA.right, nodeB.right)
            
            
        queue = [root]
        while len(queue) > 0:
            curElem = queue.pop(0)
            # Handle current element
            if isIdentical(curElem, subRoot):
                return True
            if curElem.left:
                queue.append(curElem.left)
            if curElem.right:
                queue.append(curElem.right)
        
        return False
        