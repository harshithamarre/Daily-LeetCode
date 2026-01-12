# LC 977
# Problem Link: https://leetcode.com/problems/squares-of-a-sorted-array

nums = list(map(int,input("Enter space separated integers: ").split(',')))

res = []

for i in range(len(nums)):
    res.append(nums[i]**2)

print(sorted(res))
