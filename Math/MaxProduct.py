# LC 628
# Problem Link: https://leetcode.com/problems/maximum-product-of-three-numbers

nums = list(map(int,input("Enter an integer array: ").split(',')))

# O(n^3)
'''
nums.sort()
n = len(nums)

max_prod = nums[0] * nums[1] * nums[2]

for i in range(n):
    for j in range(i + 1,n):
        for k in range(j + 1,n):
            product = nums[i] * nums[j] * nums[k]
            # if product < 0:
            #     print(product)
            #     break
            if product > max_prod:
                max_prod = product
print(max_prod)
'''

# O(n)

nums.sort()
n = len(nums)
res = max(nums[0] * nums[1] * nums[n-1], nums[-1] * nums[-2] * nums[-3])
print(res)
