[View Problem](https://leetcode.com/problems/majority-element?envType=problem-list-v2&envId=array)

### Arrays: (LC 169) Solution
```python
from collections import Counter

nums = list(map(int,input("Enter array of integers: ").split(",")))
n = len(nums)

cnt = Counter(nums)
for num,freq in cnt.items():
    if freq > n//2:
        print(num)
