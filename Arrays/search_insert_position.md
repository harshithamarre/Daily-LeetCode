[View Problem](https://leetcode.com/problems/search-insert-position?envType=problem-list-v2&envId=array)

### Arrays: (LC 35) Solution

```python
nums = list(map(int,input("Enter space seperated integers: ").split()))
target = int(input("Enter the target: "))
n = len(nums)

for i in range(n):
    if nums[i] == target:
        print(i)
        break
else:
    nums.append(target)
    ordered = sorted(nums)
    m = len(ordered)
    for j in range(m):
        if ordered[j] == target:
            print(j)
            break
