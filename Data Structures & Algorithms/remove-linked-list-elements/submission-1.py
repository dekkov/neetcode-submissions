# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        prev = dummy
        cur = head
        while cur:
            if cur.val == val:
                nxt = cur.next
                prev.next = nxt
                cur = nxt
                continue
            
            else:
                prev = cur
                cur = cur.next
        return dummy.next
        
