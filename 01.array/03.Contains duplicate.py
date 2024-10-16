
def containsDuplicate(nums):
    for i in range(len(nums)) :
        for j in range(i+1, len(nums)):
            if (nums[i] == nums[j]):
                return True
    return False

nums = [1,2,3,1]
# Output: true
result = containsDuplicate(nums)
print(result)

nums = [1,2,3,4]
# Output: false
result = containsDuplicate(nums)
print(result)

nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
result = containsDuplicate(nums)
print(result)
