#19
#删除链表倒数第n个节点
class Solution :
    def removeNthFromEnd(self , head : Optional[ListNode] , n : int ) -> Optional[ListNode] :
        dummy = ListNode(next=head)
        right = left = dummy

        for i in range(n) :
            right = right.next
        while right.next :
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
            
        









#删除链表节点，本质上通常是找“待删除节点的前一个节点
#遇到“倒数第 n 个节点”，想到双指针固定间距：先让 right 走 n 步，再让 left/right 一起走。
#可能删除头节点时优先考虑 dummy（哨兵节点）
#倒数第 n 个 → 双指针拉开 n；删除节点 → 找前驱；可能删 head → dummy。
#注意dummy的定义怎么写