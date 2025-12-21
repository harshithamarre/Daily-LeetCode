# LC 3783
# Problem Link: https://leetcode.com/problems/mirror-distance-of-an-integer

n = int(input("Enter any integer: "))
num = str(n)
rev = num[::-1]
reverse = int(rev)

mirror = abs(n - reverse)
print(mirror)
