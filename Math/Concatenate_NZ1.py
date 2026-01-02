# LC 3754
# Problem Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i

n = int(input("Enter an integer: "))
num = str(n)
res = []
for i in num:
    if i != '0':
        res.append(int(i))

x = ''.join(str(d) for d in res)

if x:
    Sum = sum(res)
    print(int(x) * Sum)
else:
    print(0)
