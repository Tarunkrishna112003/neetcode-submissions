# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = s2 = ""
        while l1:
            s1 = str(l1.val) + s1
            l1 = l1.next
        while l2:
            s2 = str(l2.val) + s2
            l2 = l2.next
            
        total = str(int(s1 or '0') + int(s2 or '0'))
        
        dummy = ListNode(0)
        curr = dummy
        # Rebuild list backwards from the sum string
        for ch in reversed(total):
            curr.next = ListNode(int(ch))
            curr = curr.next
            
        return dummy.next