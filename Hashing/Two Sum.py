class Solution:
    def twoSum(self, nums, target):
        # A dictionary to store numbers we have seen so far
        seen = {}

        # Loop through the list with index and value
        for i, num in enumerate(nums):     # enumerate() → 帮你同时获得 index（下标）和 value（值）
            # The number we need to find in order to reach the target
            complement = target - num

            # If the complement exists in the dictionary,
            # it means we have seen a number before such that:
            # seen[complement] + num == target
            if complement in seen:
                return [seen[complement], i]

            # Otherwise, store the current number and its index
            # for future lookups
            seen[num] = i
