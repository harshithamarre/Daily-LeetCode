# LC 389
# Problem Link: https://leetcode.com/problems/find-the-difference

s = input("Enter any string: ")
t = input("Enter any string: ")

s1 = sorted(s)
t1 = sorted(t)

for i in range(len(s)):
    if s1[i] != t1[i]:
        print(t1[i])
        break
    else:
        print(t1[-1])
        break
