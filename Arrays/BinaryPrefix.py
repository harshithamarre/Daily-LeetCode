# LC 1018
# Problem Link: https://leetcode.com/problems/binary-prefix-divisible-by-5

nums = list(map(int,input("Enter the array: ").split(',')))

answer = []
curr = 0

for bit in nums:
    curr = (curr * 2 + bit) % 5
    if curr == 0:
        answer.append(True)
    else:
        answer.append(False)
print(answer)
