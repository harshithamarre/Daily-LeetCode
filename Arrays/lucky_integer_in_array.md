[View Problem](https://leetcode.com/problems/find-lucky-integer-in-an-array?envType=problem-list-v2&envId=array)

### Arrays: (LC 1394) Solution
```python
from collections import Counter
arr = list(map(int,input("Enter integer array: ").split(',')))

cnt = Counter(arr)
res = []

for num,freq in cnt.items():
    if num == freq:
        res.append(num)

if len(res) > 1:
    print(max(res))
elif len(res) == 1:
    print(res[0])       # Without indexing, returns a list
else:
    print(-1)
