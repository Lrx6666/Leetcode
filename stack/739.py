#739
#单调栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []  # todolist
        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j
            st.append(i)
        return ans

# 单调递减栈
# st 存“还没找到下一个更高温度”的天数下标
#
# 当前温度 t > 栈顶温度：
#   说明栈顶这一天等到了更暖的一天
#   pop 出来，并计算距离 i-j
#
# 用 while：
#   因为今天可能一次解决前面多天的问题
#
# 最后 st.append(i)：
#   今天也要等待未来更暖的一天
#
# 核心：
#   找右边第一个更大的元素 -> 想单调栈