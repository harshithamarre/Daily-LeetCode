[View Problem](https://leetcode.com/problems/intersection-of-two-arrays)

### Arrays: (LC 349)

```python
nums1 = list(map(int,input("Enter space separated integers: ").split(',')))
nums2 = list(map(int,input("Enter space separated integers: ").split(',')))

intersection = []
unique = []

for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            intersection.append(nums1[i])
            break

for num in range(len(intersection)):
    if intersection[num] not in unique:
        unique.append(intersection[num])

print(unique)
