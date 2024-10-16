nums = [2,7,11,15]
target = 18

# Approach 1: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# result = twoSum(nums, target)
# print(result)
       
# Approach 2: One-pass Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
def twoSum2(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map:
            return [hash_map[complement], i]
        else:
            hash_map[nums[i]] = i


result2 = twoSum2(nums, target)
print(result2)