# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 不更改头指针,p1,p2一前一后
        if not head:
            return head
        p1,p2 = head,head.next
        while p2!=None:
            if p1.val == p2.val:
                p1.next = p2.next
                p2 = p2.next
            else:
                p2 = p2.next
                p1 = p1.next
        return head
