[View Problem](https://leetcode.com/problems/plus-one?envType=problem-list-v2&envId=array)

### Arrays: (LC 66) Solution

```python
digits = list(map(int, input("Enter space separated integers: ").split()))

carry = 1
n = len(digits)

for i in range(n-1, -1, -1):
    total = digits[i] + carry
    digits[i] = total % 10 
    carry = total // 10 
    
    if carry == 0:
        break

if carry:
    digits.insert(0, 1)
print(digits)
