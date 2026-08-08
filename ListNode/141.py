# 141 快慢指针
class Solution :
    def hasCycle(self , head : Optional[ListNode]) -> bool :
        slow = fast = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            if fast is slow :
                return True


#遍历的话时间复杂度会高，如果记录访问历史应该用哈希表解
#O(1)就不能保存访问历史，考虑双指针