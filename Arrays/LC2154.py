# LC 2154
# Problem Link: https://leetcode.com/problems/keep-multiplying-found-values-by-two

nums = list(map(int,input("Enter array of integers: ").split(',')))
original = int(input("Enter a number: "))

# num_set = set(nums)
while original in nums:
    original *= 2
print(original)
