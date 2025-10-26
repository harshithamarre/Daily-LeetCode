[View Problem](https://leetcode.com/problems/string-matching-in-an-array?envType=problem-list-v2&envId=string)

### Strings: (LC 1408) Solution
```python
def find_substrings(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break
    return result

words = input("Enter strings seperated with spaces: ").split()
print(find_substrings(words))
