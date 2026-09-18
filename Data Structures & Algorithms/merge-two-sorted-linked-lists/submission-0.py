# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        k=[]
        while list1:
            k.append(list1.val)
            list1=list1.next
        while list2:
            k.append(list2.val)
            list2=list2.next
        k.sort()
        cur=ListNode(0)
        dummy=cur
        for i in range(len(k)):
            dummy.next=ListNode(k[i])
            dummy=dummy.next
        return cur.next