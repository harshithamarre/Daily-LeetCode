# LC 67
# Problem Link: https://leetcode.com/problems/add-binary

a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

'''
res = ""
carry = 0

a,b = a[::-1], b[::-1]

for i in range(max(len(a),len(b))):
    digitA = ord(a[i]) - ord("0") if i < len(a) else 0
    digitB = ord(b[i]) - ord("0") if i < len(b) else 0

    total = digitA + digitB + carry
    char = str(total % 2)
    res = char + res
    carry = total // 2

if carry:
    res = "1" + res
print(res)
'''

d1 = int(a,2)
d2 = int(b,2)

res = d1 + d2
print(bin(res)[2:])
