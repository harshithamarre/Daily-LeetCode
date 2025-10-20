[View Problem](https://leetcode.com/problems/number-of-senior-citizens?envType=problem-list-v2&envId=array)

### Arrays: (LC 2678) Solution

```python
details = list(input("Enter space separated integers: ").split())

cnt = 0

for passenger in details:
    age = int(passenger[11:13])
    if age > 60:
        cnt += 1
print(cnt)
