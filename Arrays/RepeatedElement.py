# LC 961
# Problem Link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array?envType=daily-question&envId=2026-01-02

from collections import Counter

nums = list(map(int,input("Enter space separated integers: ").split(',')))
res = set(nums)
count = Counter(nums)
n = len(res) - 1

for num,freq in count.items():
    if freq == n:
        print(num)
