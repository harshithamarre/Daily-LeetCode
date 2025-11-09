[View Problem](https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition?envType=problem-list-v2&envId=array)

### Arrays (LC 3392) Solution:

```python
nums = list(map(int, input("Enter space separated integers: ").split()))
cnt = 0

for i in range(len(nums)-2):
    first = nums[i]
    second = nums[i+1]
    third = nums[i+2]

    if (first + third) == (second/2):
        cnt += 1
print(cnt)
