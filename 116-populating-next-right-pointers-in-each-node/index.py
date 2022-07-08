from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        level = dict({ root: 0 })
        queue = [root]
        
        while len(queue) != 0:
            node = queue.pop(0)
            if len(queue) == 0 or level[queue[0]] != level[node]:
                node.next = None
            else:
                node.next = queue[0]
            
            if node.left and node.right:
                queue.append(node.left)
                queue.append(node.right)
                level[node.left] = level[node.right] = level[node] + 1
        
        return root