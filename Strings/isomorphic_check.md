[View Problem](https://leetcode.com/problems/isomorphic-strings?envType=problem-list-v2&envId=string)

### Strings: (LC 205) Solution
```python
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("The two strings are not isomorphic.")
else:
    s1_to_s2 = {}
    s2_to_s1 = {}
    is_isomorphic = True

    for i, j in zip(s1, s2):
        if i in s1_to_s2:
            if s1_to_s2[i] != j:
                is_isomorphic = False
                break
        else:
            s1_to_s2[i] = j  # store mapping

        if j in s2_to_s1:
            if s2_to_s1[j] != i:
                is_isomorphic = False
                break
        else:
            s2_to_s1[j] = i

    if is_isomorphic:
        print("The two strings are isomorphic.")
    else:
        print("The two strings are not isomorphic.")
