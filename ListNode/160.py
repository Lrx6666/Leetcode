##160相交链表
class Solution:
    def getIntersectionNode(self , headA : ListNode , 
                            headB : ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        while A != B:
            if A:
                A = A.next
            else:
                A = headB
            if B:
                B = B.next
            else:
                B = headA
        return A


# A = A.next if A else headB 这么写也等价
#思想是君住长江头我住长江尾
