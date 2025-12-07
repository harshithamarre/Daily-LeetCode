### [View Problem](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range?envType=daily-question&envId=2025-12-07)

```python
low = int(input("Enter non-negative integer: "))
high = int(input("Enter non-negative integer: "))        
cnt = 0

'''
for i in range(low,high + 1):
    if i%2 != 0:
        cnt += 1
print(cnt)
'''

if high%2 == 0 and low%2 == 0:
    cnt = (high - low)//2
else:
    cnt = ((high - low)//2)+1
print(cnt)
