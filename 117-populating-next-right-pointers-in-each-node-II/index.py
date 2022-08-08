# Definition for a Node.
from typing import List

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    
    def show(self):
        print(convertNodeToArray(self))

def convertNodeToArray(root: Node):
    if root == None:
        return []

    queue = [root]
    array = []
    
    while len(queue) > 0:
        node = queue.pop(0)
        array.append(node.val if node else None)
        if node is not None and (node.left or node.right):
            queue.append(node.left)
            queue.append(node.right)
        
    return array

def convertArrayToNode(array: List):
    if len(array) == 0:
        return None
    nodeList = [Node(elem) if elem else None for elem in array]
    i = 0
    left = 1
    while left < len(array) - 1:
        if nodeList[i] == None:
            i += 1
            continue

        curNode = nodeList[i]
        right = left + 1
        curNode.left = nodeList[left]
        curNode.right = nodeList[right]

        left += 2
        i += 1

    return nodeList[0]

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        queue = [root, None]
        array = []
        
        while len(queue) > 0:
            firstElem = queue.pop(0)
            array.append(firstElem)

            if firstElem is None:
               if len(queue) > 0:
                    queue.append(None)
            else:
                if firstElem.left:
                    queue.append(firstElem.left)
                if firstElem.right:
                    queue.append(firstElem.right)
            
        for idx, node in enumerate(array):
            if node:
                node.next = array[idx + 1]
        
        return root

def connect(array: List) -> Node:
    root = convertArrayToNode(array)
    print('***************************')
    sls = Solution()
    result = sls.connect(root)
    # print(result)
    return result

connect([1,None,3,6,7,12,13,14,15])