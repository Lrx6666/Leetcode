##438 找到字符串中所有字母的异位词
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p) ##用短的数组锚定每个字母出现的次数
        cnt_s = Counter()  ##长的，先空白
        ans = []

        for right, c in enumerate(s):
            cnt_s[c] += 1  # 右端点字母进入窗口先记
            left = right - len(p) + 1 ##长度=右-左+1  左=右-长度+1
            if left < 0:  # 窗口长度不足 len(p)直接跳
                continue
            if cnt_s == cnt_p:  # t 和 p 的每种字母的出现次数都相同
                ans.append(left)
            cnt_s[s[left]] -= 1  # 左端点字母离开窗口
        return ans

#先定right 对比counter 挪left