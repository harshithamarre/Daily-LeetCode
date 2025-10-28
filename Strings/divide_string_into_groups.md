[View Problem](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k?envType=problem-list-v2&envId=string)

### Strings: (LC 2138)

```python
s = input("Enter any string: ")
k = int(input("Enter group size: "))
fill = input("Enter a fill letter: ")

groups = []

for i in range(0,len(s),k):
    group = s[i:i+k]
    i += 1

    if len(group) < k:
        group += fill * (k - len(group))
    groups.append(group)
print(groups)
