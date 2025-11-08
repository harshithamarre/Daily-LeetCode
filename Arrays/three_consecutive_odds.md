[View Problem](https://leetcode.com/problems/three-consecutive-odds?envType=problem-list-v2&envId=array)

### Arrays: (LC 1550) Solution

```python
arr = list(map(int, input("Enter space separated integers: ").split()))
res = []

for i in range(len(arr) - 2):
    first = arr[i]
    second = arr[i + 1]
    third = arr[i + 2]
    res.append([first,second,third])

for i in res:
    if i[0]%2!=0 and i[1]%2!=0 and i[2]%2!=0:
        print("True")
        break
else:
    print("False")
