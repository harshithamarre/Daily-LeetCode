[View Problem](https://leetcode.com/problems/third-maximum-number)

### Arrays: (LC 414) Solution

```python
nums = list(input("Enter space separated integers: ").split())
distinct_nums = set(nums)
sorted_nums = sorted(distinct_nums)

if len(sorted_nums) >= 3:
    third_large = sorted_nums[-3]
    print(third_large)
else:
    large = sorted_nums[-1]
    print(large)
