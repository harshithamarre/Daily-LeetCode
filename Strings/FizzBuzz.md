[View Problem](https://leetcode.com/problems/isomorphic-strings?envType=problem-list-v2&envId=string)

### Strings: (LC 412) Solution
```python
n = int(input("Enter any number: "))

answer = []
for i in range(1,n+1):
    if (i%3 == 0 and i%5 == 0):
        answer.append("FizzBuzz")
    elif i%3 == 0:
        answer.append("Fizz")
    elif i%5 == 0:
        answer.append("Buzz")
    else:
        answer.append(str(i))
print(answer)
