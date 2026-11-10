class Solution:
  def manArea(self, height: list[int]) -> int:
    left = 0
    right = len(heigtht) -1  #长度-1=索引的最大值，比如长度是9的list，索引最大值是8
    max_area = 0

    while left < right:
      width = rigtht - left      #计算宽度
      h = min(height[left], height[right])     #取两端高度的最小值
      area = width * h      #计算面积
      max_area(area, max_area)

      if height[left] < height[right]:   #左边和右边的值哪个小就移动哪个，关键逻辑
        left += 1
      else:
        right -= 1
        
    return max_area


# 最关键的逻辑
# 每次移动指针，宽度一定变小。
# 想让面积有机会变大，就必须让容器的有效高度增加。
# 而有效高度由较短的线决定。
