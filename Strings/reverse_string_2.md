[View Problem](https://leetcode.com/problems/reverse-string-ii?envType=problem-list-v2&envId=string)

### Strings: (LC 541) solution:

```python
s = input("Enter any string: ")
k = int(input("Enter any number: "))

result = []

# Note: Strings are immutable

for i in range(0, len(s), 2 * k):
    a = s[i:i + 2 * k]
    reversed_part = a[:k][::-1]
    remaining = a[k:]
    result.append(reversed_part + remaining)
print(''.join(result))
