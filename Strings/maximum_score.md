[View Problem](https://leetcode.com/problems/maximum-score-after-splitting-a-string?envType=problem-list-v2&envId=string)

### Strings: (LC 1422) Solution
```python
def all_splits(s):

    score = []
    
    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]

        left_zeros = left.count('0')
        right_ones = right.count('1')

        score.append(left_zeros + right_ones)
        
    print(f"Maximum score: {max(score)}")

s = input("Enter a string with 1's and 0's only: ")
all_splits(s)
