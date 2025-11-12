[View Problem](https://leetcode.com/problems/majority-element?envType=problem-list-v2&envId=array)

## Arrays: (LC 169) Solution

### Approach:
I used Python's Counter from the collections module to efficiently count the frequency of each element in the array. Then, I iterated through the counter items and returned the first element whose frequency is greater than half the length of the array.

### Complexity:
- Time complexity: $$O(n)$$
- Space complexity: $$O(n)$$

### Code:
```python
from collections import Counter

nums = list(map(int,input("Enter array of integers: ").split(",")))
n = len(nums)

cnt = Counter(nums)
for num,freq in cnt.items():
    if freq > n//2:
        print(num)
```
