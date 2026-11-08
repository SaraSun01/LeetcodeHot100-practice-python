class Solution:
  def movezeros(self, nums:list[int]) -> None:
    write = 0
 # 第一步：把非零元素依次移动到前面
    for read in range(len(sums)):
      if nums[read] !=0:
        nums[write]=nums[read]  # 把读指针位置的数字，写入写指针所在的位置。
        write += 1
# 第二步：把剩余位置全部填成 0
    while write < len(nums):
      nums[write] = 0
      write += 1

# read 负责寻找非零数字，write 负责确定非零数字应该放在哪里。
