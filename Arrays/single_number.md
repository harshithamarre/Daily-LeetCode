[View Problem](https://leetcode.com/problems/single-number?envType=problem-list-v2&envId=array)

### Arrays: (LC 136) Solution

```python
from collections import Counter
nums = list(map(int,input("Enter space separated integers: ").split()))

count = Counter(nums)
for num,freq in count.items():
    if freq == 1:
        print(num)
