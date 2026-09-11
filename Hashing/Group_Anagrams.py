class Solution:    # main idea:两个字符串如果排序后相同，就是异位词。
    def groupAnagrams(self, strs):
        groups = {}   # 创建字典

        for word in strs:

            # 1. 把 word 排序（过程非常明确）
            letters = list(word)   # 拆成字母列表
            letters.sort()         # 排序
            key = "".join(letters) # 拼成字符串作 key

            # 2. 判断 key 是否已经在 groups 里
            if key not in groups:
                groups[key] = []   # 初始化空列表

            # 3. 把当前 word 放到对应 key 的列表里
            groups[key].append(word)

        # 4. 返回结果
        result = []
        for k in groups:
            result.append(groups[k])

        return result
