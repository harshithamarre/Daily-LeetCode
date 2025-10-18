[View Problem](https://leetcode.com/problems/two-sum)

# Arrays: (LC 1) Solution

```python
nums = list(map(int,input("Enter space seperated integers: ").split()))
target = int(input("Enter the target: "))
n = len(nums)

for i in range(n):
    for j in range(i + 1, n):
        r = nums[i] + nums[j]
        if r == target:
            print([i, j])
