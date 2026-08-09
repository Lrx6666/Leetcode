#148
#排序链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next :
            return head
        #切断链表
        slow = head
        fast = head.next #why???
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            mid = slow.next
            slow.next = None
            
