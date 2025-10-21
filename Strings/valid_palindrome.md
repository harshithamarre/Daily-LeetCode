[View Problem](https://leetcode.com/problems/valid-palindrome?envType=problem-list-v2&envId=string)

### Strings: (LC 125) Solution

```python
s = input("Enter any sentence: ")
lower_case = s.lower()
result = ""       # Strings are immutable

for char in s:
    if char.isalnum():
        result += char.lower()
print(result == result[::-1])
