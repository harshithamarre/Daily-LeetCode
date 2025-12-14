# LC 3774
# Problem Link: https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements

nums = list(map(int,input("Enter array of integers: ").split(",")))
k = int(input("Enter an integer: "))

ordered = sorted(nums)

large = sum(ordered[-k:])
small = sum(ordered[:k])

print(abs(large - small))
