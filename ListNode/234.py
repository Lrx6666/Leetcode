## 234 回文链表
class ListNode :
    def __init__ (self . val = 0 , next = None) :
        self.val = val
        self.next = next
class Solution :
    #反转链表
    def reverseList (self , head : Optional[ListNode] ) -> Optional[ListNode] :
        pre = None
        cur = head
        while cur :
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
    #找中间节点
    def middle (self , head : Optional[ListNode]) ->Optional[ListNode] :
        cnt = 0
        cur = head
        while cur is not None :
            cnt += 1
            cur = cur.next
        steps = cnt // 2
        cur = head
        for i in range(steps) :
            cur = cur.next
        return cur
    