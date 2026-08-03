##3 无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self , s : str) -> int:
        dic , res , i = {} , 0 , -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max (i , dic[s[j]])
            dic[s[j]] = j
            res = max (res , j - i)
        return res

##左指针从-1开始，右指针的值放进字典，如果重复：左指针右移