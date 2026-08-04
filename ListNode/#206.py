#206 反转链表
class ListNode :
    def __init__(self , val = 0 , next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self , head : Optional[ListNode]) -> Optional[ListNode] :
        #初始化
        cur = head 
        pre = None
        #有活干的时候
        while cur :
            tmp = cur.next #把屁股暂存到tmp右手
            cur.next = pre # 翻转箭头指向
            pre = cur #暂存当前节点
            cur = tmp # 访问下一节点
        return pre

#确实是双指针好写多了，暴力解法很容易乱
#在操作之前总要先把屁股打理好，核心的两步就是调转箭头和移动cur指针，在这两步之前都需要把屁股打理好
    

     

            


