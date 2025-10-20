[View Problem](https://leetcode.com/problems/truncate-sentence?envType=problem-list-v2&envId=array)

### Arrays: (LC 1816) Solution

```python
s = input("Enter a sentence: ")
k = int(input("Enter no.of.words you want after truncating: "))

truncated = []
splitted = s.split()
print(splitted)
n = len(splitted)

i = 0
while i < k and k < n:
    truncated.append(splitted[i])
    i += 1
print(' '.join(truncated))

print('--'*5 + "or" + '--'*5)

res = splitted[:k]         # truncated = s.split()[:k]
print(' '.join(res))
