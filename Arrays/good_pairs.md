[View Problem](https://leetcode.com/problems/number-of-good-pairs?envType=problem-list-v2&envId=array)

## Arrays: (LC 1512) Solution

### Complexity
- Time complexity: $$O(n²)$$

- Space complexity: $$O(1)$$

### Code
```python []
class Solution(object):
    def numIdenticalPairs(self, nums):
        
        cnt = 0

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i] == nums[j]):
                    cnt += 1

        return cnt
```
