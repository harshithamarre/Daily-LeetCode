[View Problem](https://leetcode.com/problems/check-if-array-is-good?envType=problem-list-v2&envId=array)

### Arrays: (LC 2784) Solution

```python

from collections import Counter

def isGood(nums):
    n = max(nums)
    if len(nums) != n + 1:
        print("False")
    
    count = Counter(nums)
    
    # Check numbers 1 to n-1 appear once
    for i in range(1, n):
        if count[i] != 1:
            print("False")
    
    # Check number n appears twice
    if count[n] != 2:
        print("False")
    
    print("True")

nums = list(map(int,input("Enter the integer array: ").split(",")))
isGood(nums)
