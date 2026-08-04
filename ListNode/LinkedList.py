class ListNode:
    def __init__(self, data):
        self.data = data #数据域
        self.next = None #指针域 通常初始赋值空

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2) #把链表串起来的写法
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    tmp = head #指针变量赋值
    tmp = tmp.next #指针变量移动
    tmp.next = None 
    #通过tmp指针变量更改节点的指针域：截断链表 
    # tmp为地址引用，与head指向相同地址，操作同一份数据
    tmp.next = ListNode(100) #通过tmp指针变量更改节点的指针域：增加节点

#封装一个增加节点方法
def insert_node(node , value):
    if node in None:
        return 
    #创建一个新节点
    new_node = ListNode(value)
    cur = node 
    while cur.next is not None:
        cur = cur.next
    #末尾节点的next指针域连接新节点
    cur.next = new_node

#打印链表
def print_node(node):
    cur =  node
    while cur in not None:
        print(cur.val , end = "\t")
        cur = cur.next
        
===============================================================================
#循环链表
class CircularListNode : 
    def __init__(self , x):
        self.val = x #链表的数据域
        self.next = None #链表的指针域

def append_node(head , vaL):
    if head is None:
        return
    cur = head 
    #移动指针变量到末尾节点
    while cur.next is not head:
        cur = cur.next
    #新节点追加到链表结尾
    new_node = CircularListNode(val)
    cur.next = new_node
    new_node.next = head

def print_node(head):
    if head is None:
        return
    cur = head.next
    if head is cur :#只有一个节点
        print(cur.val)
        return
    #1.打印头节点
    print(head.val , end = "\t")
    #2.打印中间节点
    while cur is not head:
        print (cur.val , end = "\t")
        cur = cur.next
    

def delete_node(head , node):
    if head is None or head.next is next:
        return
    cur = head 
    while cur.next.next is not head : #找到链表的倒数第二个节点
        cur = cur.next
    #删除最后一个节点
    cur.next = head 




 






if __name__ == '__main__' :
    #一个节点组成的循环链表
    head = CircularListNode(1)
    head.next = head

    #add a node
    newNode =  CircularListNode(2)
    head.next = newNode
    newNode.next = head

    #add a node
    tmp = CircularListNode(3)
    head.next.next = tmp
    tmp.next = head

    #delete a node eg. delete node 2
    head.next = head.next.next
    #deleta a node eg. delete node 3 (the last node)
    head.next.next = head #节点操作：指针域 = 节点名    

    =======================================================================
    #追加链表节点
    root =  CircularListNode(11)
    root.next = root #形成环状列表
    append_node (root , 12)

    #打印链表节点
    print_node(root)

    #删除链表节点
    delete_node(root)
    print_node(root)




