#142
#环形链表2 似乎和上一道题的区别是这个要返回链表节点上一个返回bool
class Solution :
    def detectCycle(self , head : Optional[ListNode]) -> Optional[ListNode] :
        fast = head
        slow = head 
        #找环模版（快慢指针）
        while fast is not None and fast.next is not None :
            slow = slow.next
            fast = fast.next.next
            if slow is fast :
                break
        else :
            return None
        #找入口
        pointer = head
        while pointer is not slow :
            pointer = pointer.next
            slow = slow.next
        return pointer
    
##必然在环入口相遇