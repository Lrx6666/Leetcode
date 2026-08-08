# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        cur = dummy

        while cur.next and cur.next.next :
            node1 = cur.next
            node2 = cur.next.next
            node1.next = node2.next #A->C
            node2.next = node1 #B->A
            cur.next = node2 # cur->B
            cur = node1
        return dummy.next

#x.next = node1 让x指向节点1   x->1->2->3
#x.next = node1.next 让x指向节点1的下一个节点 x->2->3 此时会丢节点
#本题不用cur.next = cur.next.next也是一样的道理，会丢节点导致混乱
#本题里一个while的node1 node2是这一组要被交换的第一个。第二个节点
