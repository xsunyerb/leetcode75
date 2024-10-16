# O(n2) solution
def arrayProduct(nums):
    output = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        output.append(product)
    return output

nums = [1,2,3,4]
# Output: [24,12,8,6]
result = arrayProduct(nums)
print(result)

nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
result = arrayProduct(nums)
print(result)
