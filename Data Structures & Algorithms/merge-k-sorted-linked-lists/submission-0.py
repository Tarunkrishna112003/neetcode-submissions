# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l=[]
        for f in lists:
            while f:
                l.append(f.val)
                f=f.next
        l.sort()
        g=ListNode(0)
        t=g
        for i in l:
            t.next=(ListNode(i))
            t=t.next
        return g.next



