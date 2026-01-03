# LC 1051
# Problem Link: https://leetcode.com/problems/height-checker

heights = list(map(int,input("Enter the array: ").split(',')))

expected = sorted(heights)
cnt = 0

for i in range(len(expected)):
    if expected[i] != heights[i]:
        cnt += 1
print(cnt)
