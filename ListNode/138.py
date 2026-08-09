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
                cur.next.random = cur.random.next
                cur = cur.next.next
        #3
        while cur.next :
            cur = dummy = Node(0 , head)
            cur.next = cur.next.next
            cur = cur.next
        return dummy.next