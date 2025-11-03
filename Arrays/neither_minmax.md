[View Problem](https://leetcode.com/problems/neither-minimum-nor-maximum)

### Arrays: (LC 2733) Solution

```python
import random

nums = list(map(int,input("Enter space separated integers: ").split()))

maximum = max(nums)
minimum = min(nums)

neither_minmax = []

if len(nums) > 2:
    for num in nums:
        if num != maximum and num != minimum:
            neither_minmax.append(num)
    print(random.choice(neither_minmax))
else:
    print(-1)
