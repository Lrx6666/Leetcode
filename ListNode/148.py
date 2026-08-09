#148
#排序链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from hot100.ListNode.LinkedList import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next :
            return head
        #1 切断链表
        slow = head
        fast = head.next #画图看速度路程就知道了
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        mid = slow.next #后半段第一个
        slow.next = None #前半段最后一个
        #2 定义前后段链表
        left = self.sortList(head)
        right = self.sortList(mid)
        #3 合并
        cur = ListNode(0)
        dummy = ListNode(0)
        while left and right :
            if left.val < right.val :
                cur.next = left
                left = left.next
            else :
                cur.next = right
                right = right.next
            cur = cur.next
            #left right里有一个为空了直接接到cur后面
            if left :
                cur.next = left
            else :
                cur.next = right

            return dummy.next


