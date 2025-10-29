[View Problem](https://leetcode.com/problems/lucky-numbers-in-a-matrix?envType=problem-list-v2&envId=array)

### Arrays: (LC 1380) Solution

```python
# Arrays: (LC 1380)

import numpy as np

matrix = np.array([[3,7,8],[9,11,13],[15,16,17]])

row_min = [min(row) for row in matrix]
col_max = [max(col) for col in zip(*matrix)]
lucky = []

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
            lucky.append(matrix[i][j])
print(lucky)
