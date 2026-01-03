# LC 2239
# Problem Link: https://leetcode.com/problems/find-closest-number-to-zero

nums = list(map(int,input("Enter integer array: ").split(',')))

closest = nums[0]

for num in nums:
    if abs(num) < abs(closest):
        closest = num

if closest < 0 and abs(closest) in nums:
    print(abs(closest))
else:
    print(closest)
