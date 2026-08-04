## 234 回文链表
# 1. 先找到链表中间节点，将链表分成前半部分和后半部分；
# 2. 将后半部分链表进行反转，使其顺序与前半部分对应；
# 3. 使用两个指针分别遍历前半部分和反转后的后半部分，逐个比较节点值；
# 4. 如果存在节点值不同，则不是回文链表，恢复链表后返回 False；
# 5. 如果全部比较成功，则恢复链表结构并返回 True。
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
    def middleNode(self , head : Optional[ListNode]) ->Optional[ListNode] :
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
    #解
    def isPalindrome(self , head : Optional[ListNode]) -> bool :
        mid = self.middleNode(head)
        head2 = h2 = self.reverseList(mid)
        while head2 :
            if head.val != head2.val :
                self.reverseList(h2)
                return False
            head = head.next
            head2 = head2.next
        self.reverseList(h2)
        return True
