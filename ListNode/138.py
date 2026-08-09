#138
#随机链表的复制
class Solution :
    def copyRandomList(self , head :'Optional[Node]') -> 'Optional[Node]':
        #1 复制每个节点，把新节点直接插到原节点的后面
        cur = head
        while cur :
            cur.next = Node(cur.val , cur.next) #把cur.next变成cur一模一样的
            cur = cur.next.next #然后跳过克隆羊节点
        #2 遍历交错链表中的原链表节点
        cur = head
        while cur :
            if cur.random :
                cur.next.random = cur.random.next #把原来cur.random的next给克隆羊的random
            cur = cur.next.next #跳过克隆羊
        #3 删除交错链表中的原链表节点，剩下的节点即为新链表
        cur = dummy = Node(0 , head) #关键的赋值
        while cur.next :
            cur.next = cur.next.next #删除原节点
            cur = cur.next
        return dummy.next