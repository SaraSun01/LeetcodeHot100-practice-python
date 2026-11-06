
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:    # 括号里nums是一个整数列表，预期返回整数
        num_set = set(nums) # 把输入列表转换成集合
        longest = 0  # 初始化最长序列长度

        for num in num_set:
            # 只从连续序列的起点开始
            if num - 1 not in num_set:  #如果前一个数不存在，那么它是起点,核心代码，保证时间复杂度
                current = num
                length = 1

                # 不断寻找下一个连续数字
                while current + 1 in num_set:
                    current += 1   # 数值+1，长度也+1
                    length += 1

                # 更新最长序列长度
                longest = max(longest, length)

        return longest

      
# 复杂度分析：
# 时间复杂度：O(n)，因为创建集合和遍历集合都是 O(n)，每个元素在向后查找连续序列时最多被访问一次（假设集合查询平均 O(1)）。
# 空间复杂度：O(n)，因为创建了一个 set 来存储数组中的元素
      
# print()：把内容显示出来。return：把结果交给调用函数的代码。
