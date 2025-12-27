# LC 3110
# Problem Link: https://leetcode.com/problems/score-of-a-string

s = input("Enter a string: ").lower()
res = 0

for i in range(len(s)-1):
    res += abs(ord(s[i]) - ord(s[i+1]))
print(res)
