[View Problem](https://leetcode.com/problems/set-mismatch?envType=problem-list-v2&envId=array)

### Arrays: (LC 645) Solution

```python
from collections import Counter

nums = list(map(int,input("Enter space separated integers: ").split()))
n = len(nums)
original_set = set(range(1, n + 1))

res = []

# Duplicate number

count = Counter(nums)

for num,freq in count.items():
    if freq == 2:
        res.append(num)
        break

# Missing number

missing = original_set - set(nums)      # List subtraction doesn't exist. Proceed with set subtraction
res.extend(missing)
print(res)
