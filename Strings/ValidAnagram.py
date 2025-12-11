# LC 242
# Problem Link: https://leetcode.com/problems/valid-anagram

str1 = input("Enter first string: ")
str2 = input("Enter first string: ")

s1 = sorted(str1)
s2 = sorted(str2)

if s1 == s2:
    print("True")
else:
    print("False")
