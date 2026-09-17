# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k=[]
        h=head
        while h:
            k.append(h.val)
            h=h.next
        k=k[::-1]
        j=ListNode(0)
        m=j
        for i in k:
            m.next=ListNode(i)
            m=m.next
        return j.next