"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {None:None}

        cur = head
        while cur:
            if cur not in oldToCopy:
                newN = Node(cur.val)
                oldToCopy[cur] = newN
            cur = cur.next
        
        cur = head
        while cur:
            og_next = oldToCopy[cur.next]
            og_random = oldToCopy[cur.random]

            copy = oldToCopy[cur]
            copy.next = og_next
            copy.random = og_random

            cur = cur.next
        
        return oldToCopy[head]
