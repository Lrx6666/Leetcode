#2 两数相加
class Solution :
    def addTwoNumbers(self , l1 : Optional[ListNode] ,
                      l2 : Optional[ListNode] , carry = 0 )-> Optional[ListNode] :
        if l1 is None and l2 is None and carry == 0 : #carry是上一位产生的进位 递归边界 同时满足
            return None

        S = carry

        if l1 :
            s += l1.val 
            l1 = l1.next
        if l2 :
            s += l2.val
            l2 = l2.next

        node_value = s % 10
        next_node = self.addTwoNumbers(l1, l2, s // 10)

        return ListNode(node_value, next_node)
